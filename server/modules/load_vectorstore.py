import os
import time
from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm
from pinecone import Pinecone, ServerlessSpec
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
PINECONE_ENV=os.getenv("PINECONE_ENV")
PINECONE_INDEX_NAME=os.getenv("PINECONE_INDEX_NAME")

os.environ["GOOGLE_API_KEY"]=GOOGLE_API_KEY

UPLOAD_DIR="./uploaded_docs"
os.makedirs(UPLOAD_DIR,exist_ok=True)


# initialize pinecone instance
pc=Pinecone(api_key=PINECONE_API_KEY)
spec=ServerlessSpec(cloud="aws",region=PINECONE_ENV)
existing_indexes=[i["name"] for i in pc.list_indexes()]


if PINECONE_INDEX_NAME not in existing_indexes:
    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=3072,
        metric="dotproduct",
        spec=spec
    )
    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        time.sleep(1)


index=pc.Index(PINECONE_INDEX_NAME)

# load,split,embed and upsert pdf docs content

def load_vectorstore(uploaded_files):
    embed_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    file_paths = []

    for file in uploaded_files:
        save_path = Path(UPLOAD_DIR) / file.filename
        with open(save_path, "wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        texts = [chunk.page_content for chunk in chunks]
        metadatas = []
        for chunk in chunks:
            meta = chunk.metadata.copy()
            meta["text"] = chunk.page_content 
            metadatas.append(meta)

        ids = [f"{Path(file_path).stem}-{i}" for i in range(len(chunks))]

        print(f"🔍 Embedding {len(texts)} chunks...")
        embeddings = embed_model.embed_documents(texts)

        print("📤 Uploading to Pinecone...")
        with tqdm(total=len(embeddings), desc="Upserting to Pinecone") as progress:
            index.upsert(vectors=zip(ids, embeddings, metadatas))
            progress.update(len(embeddings))

        print(f"Upload complete for {file_path}")


"""
# Ayarlar: Batch boyutu ve bekleme süresi
        BATCH_SIZE = 15  # Her seferinde 15 parça gönder (limit 100)
        
        print(f"🔍 {len(chunks)} parça işleniyor...")

        for i in range(0, len(chunks), BATCH_SIZE):
            batch_chunks = chunks[i : i + BATCH_SIZE]
            
            texts = [chunk.page_content for chunk in batch_chunks]
            metadatas = []
            for chunk in batch_chunks:
                meta = chunk.metadata.copy()
                meta["text"] = chunk.page_content 
                metadatas.append(meta)

            ids = [f"{Path(file_path).stem}-{j}" for j in range(i, i + len(batch_chunks))]

            # API Kotasını korumak için embedding işlemi
            try:
                embeddings = embed_model.embed_documents(texts)
                
                # Pinecone'a yükle
                index.upsert(vectors=zip(ids, embeddings, metadatas))
                print(f"✅ {i + len(batch_chunks)}/{len(chunks)} parça yüklendi.")
                
                # Her batch sonrası 1-2 saniye bekle (Hata riskini sıfırlar)
                time.sleep(1.5) 
                
            except Exception as e:
                print(f"⚠️ Hata oluştu: {e}")
                time.sleep(20) # Hata alırsan 20 sn bekle ve devam et
                # Burada istersen aynı batch'i tekrar deneyecek bir mantık kurabilirsin.

        print(f"✨ {file_path} için işlem tamamlandı.")
"""
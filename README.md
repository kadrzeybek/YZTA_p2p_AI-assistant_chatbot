# 🤖 P2P AI Assistant Chatbot

> **Retrieval-Augmented Generation (RAG) Tabanlı Akıllı Asistan**

Kullanıcıların kendi dokümanlarını (PDF, TXT, DOCX) yükleyerek yapay zeka ile doğrudan etkileşim kurabileceği bir RAG uygulaması.

---

## 🎯 Proje Hakkında

**P2P AI Assistant**, FastAPI backend ve Streamlit frontend entegrasyonu ile inşa edilmiş, LangChain ve vektör veritabanlarını kullanarak semantik arama ve belge analizi yapan bir chatbot sistemidir.

Sistem, kullanıcıların özel verilerine dayalı yanıtlar üretmesine olanak tanır. Genel amaçlı LLM modellerini özel dokümanlarınızla birleştirerek, belgesine özgü akıllı soru-cevap deneyimi sağlar.

---

## 🧠 Nasıl Çalışır?

```
┌─────────────┐
│   Kullanıcı │
│  Dokümanları│
└──────┬──────┘
       │
       ▼
┌─────────────────────────────┐
│  Doküman İşleme & Chunking  │ (Text parçalama)
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  Embedding & Vektörleme     │ (Google GenAI Embeddings)
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  Vektör Veritabanı          │ (Pinecone)
└──────────┬──────────────────┘
           │
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌────────┐   ┌───────────┐
│ Soru   │   │ Benzer    │
│Sorgula │──▶│ Dokümlar  │
└────────┘   │Getir      │
             └─────┬─────┘
                   │
                   ▼
            ┌─────────────────┐
            │ LLM ile Cevap   │
            │ Üretme(Llma 3.3)│
            └─────────────────┘
```

**Adım Adım Akış:**

1. **Doküman Yükleme** → PDF, TXT, DOCX dosyalarını sisteme yükle
2. **İşleme & Parçalama** → Metni anlamlı chunk'lara böl
3. **Vektörleştirme** → Her chunk'ı sayısal vektöre dönüştür
4. **Sorgulama** → Kullanıcı sorusuyla en alakalı chunks'ları bul
5. **Cevap Üretimi** → LLM, bağlam + soru ile yanıt oluştur

---

## 🏗️ Teknoloji Stack

### Backend
- **FastAPI** - Asenkron, yüksek performanslı API framework
- **LangChain** - LLM orchestration ve RAG pipeline
- **Pinecone** - Ölçeklenebilir vektör veritabanı
- **Groq** - Hızlı LLM inference
- **Google GenAI** - Embedding ve LLM modelleri

### Frontend
- **Streamlit** - Hızlı veri uygulaması geliştirme
- **Python** - UI bileşenleri ve API iletişimi

### Doküman İşleme
- **PyPDF** - PDF parsing
- **python-docx** - DOCX format desteği

---

## 📁 Proje Yapısı

```
P2P-Rag-test/
├── client/
│   ├── app.py                    # Streamlit ana uygulaması
│   ├── components/
│   │   ├── chatUI.py             # Chat mesajlaşma bileşeni
│   │   ├── upload.py             # Dosya yükleme bileşeni
│   │   └── history_download.py   # Chat geçmişi indirme
│   └── utils/
│       └── api.py                # Backend API haberleşmesi
│
├── server/
│   ├── main.py                   # FastAPI uygulaması
│   ├── logger.py                 # Logging konfigürasyonu
│   ├── config.py                 # Sunucu ayarları
│   ├── middlewares/
│   │   └── expection_handlers.py # Exception handling
│   ├── routes/
│   │   ├── upload_files.py       # Dosya yükleme endpoint'i
│   │   └── ask_question.py       # Soru-cevap endpoint'i
│   ├── modules/
│   │   ├── llm.py                # LLM model ayarları
│   │   ├── load_vectorstore.py   # Vektör DB yönetimi
│   │   ├── pdf_handlers.py       # PDF işleme
│   │   └── query_handlers.py     # RAG query işleme
│   ├── requirements.txt
│   └── uploaded_docs/            # Yüklenen dokümanlar
│
└── README.md                     # Bu dosya
```

---

## ⚙️ Kurulum & Çalıştırma

### 1️⃣ Depoyu Klonla

```bash
git clone https://github.com/kadrzeybek/YZTA_p2p_AI-assistant_chatbot.git
cd YZTA_p2p_AI-assistant_chatbot
```

### 2️⃣ Ortam Değişkenlerini Ayarla

`.env` dosyası oluştur:

```env

# Google Generative AI
GOOGLE_API_KEY=your_key_here

# Groq API
GROQ_API_KEY=your_key_here

# Pinecone
PINECONE_API_KEY=your_key_here
PINECONE_ENV=your_env_here
PINECONE_INDEX_NAME=chatbotindex

### 3️⃣ Backend Kurulumu

```bash
cd server
python -m venv venv
source venv/bin/activate  # Mac/Linux
# veya
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

**Sunucuyu Başlat:**
```bash
uvicorn main:app --reload --port 8000
```

API şu adreste çalışacak: `http://localhost:8000`

### 4️⃣ Frontend Kurulumu

**Yeni terminal açarak:**

```bash
cd client
pip install streamlit requests python-dotenv

streamlit run app.py
```

Uygulama açılacak: `http://localhost:8501`

---

## 🚀 Kullanım

### Adım 1: Doküman Yükle
- Sol sidebar'dan `.pdf`, `.docx`, `.txt` vb. dosyaları seç
- "Upload DB" butonuna tıkla
- İşlem tamamlanmasını bekle

### Adım 2: Soru Sor
- Chat input alanına sorunuzu yazın
- Asistan ilgili dokümanlardan bilgi çekerek cevap verecek

---

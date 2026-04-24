📚 YZTA P2P AI Assistant Chatbot
Bu proje, yüklediğiniz dokümanları (PDF, TXT, DOCX) saniyeler içinde analiz eden ve bu belgelerdeki bilgilere dayanarak sorularınızı cevaplayan bir yapay zeka asistanıdır.

✨ Temel Özellikler
Doküman Sorgulama: Kendi dosyalarınızı yükleyin ve içeriği hakkında soru sorun.

Akıllı Cevaplar: Yapay zeka, sadece dosyanızdaki bilgileri kullanarak doğru yanıtlar üretir.

Hızlı ve Modern: FastAPI ve Streamlit ile geliştirilmiş kullanıcı dostu arayüz.

Geniş Format Desteği: PDF, Word (DOCX) ve Metin (TXT) dosyalarıyla tam uyum.

🛠 Kullanılan Teknolojiler
Backend: FastAPI & LangChain

Yapay Zeka: OpenAI GPT & Embeddings

Vektör Veritabanı: FAISS

Arayüz: Streamlit

📁 Proje Klasör Yapısı
Plaintext

├── client/          # Kullanıcı arayüzü (Streamlit)
├── server/          # Yapay zeka ve API merkezi (FastAPI)
└── requirements.txt # Gerekli kütüphaneler
🚀 Hızlı Başlangıç
Gereksinimleri Yükleyin:

Bash

pip install -r requirements.txt
API Anahtarını Tanımlayın:
.env dosyası oluşturup OPENAI_API_KEY bilginizi ekleyin.

Sistemi Çalıştırın:

Backend: uvicorn server.app:app --reload

Frontend: streamlit run client/app.py



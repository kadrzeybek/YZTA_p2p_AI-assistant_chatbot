# 📚 Chat with Your Documents (RAG based  AI Assistant)

## 🚀 Proje Hakkında

Bu proje, kullanıcıların yüklediği dokümanlar (PDF, TXT, DOCX) üzerinden yapay zeka ile etkileşim kurmasını sağlayan bir **Retrieval-Augmented Generation (RAG)** uygulamasıdır.

Sistem, yüklenen dokümanları analiz eder, anlamlı parçalara ayırır ve bu içerikler üzerinden kullanıcı sorularına **kaynak temelli (source-grounded)** cevaplar üretir.

---

## 🎯 Amaç

Bu projenin amacı:

* Büyük dil modelleri (LLM) ile gerçek bir uygulama geliştirmek
* RAG (Retrieval-Augmented Generation) mimarisini uygulamak
* Doküman işleme, embedding ve bilgi erişim süreçlerini deneyimlemek
* Kullanıcıya güvenilir ve kaynak gösteren cevaplar sunmak

---

## 🧠 Nasıl Çalışır?

Uygulama aşağıdaki adımları izler:

1. 📂 Kullanıcı doküman yükler (PDF, TXT, DOCX)
2. 🧹 Metin çıkarılır ve temizlenir
3. ✂️ Metin küçük parçalara (chunks) bölünür
4. 🔢 Her parça embedding vektörüne dönüştürülür
5. 🗄️ Vektör veritabanına kaydedilir (FAISS)
6. ❓ Kullanıcı soru sorar
7. 🔍 En ilgili doküman parçaları bulunur
8. 🤖 LLM yalnızca bu bağlama göre cevap üretir
9. 📄 Cevap ile birlikte kaynaklar döndürülür

---

## 🏗️ Kullanılan Teknolojiler

### Backend

* FastAPI
* LangChain
* FAISS (Vector Database)
* OpenAI API (LLM + Embeddings)

### Frontend

* Streamlit

### Doküman İşleme

* PyPDF (PDF parsing)
* python-docx (DOCX parsing)

---

## 📁 Proje Yapısı

```bash
client/
├── app.py
├── components/
│   ├── chatUI.py
│   ├── uploader.py
│   └── history_download.py
└── utils/
    └── api.py

server/
├── app.py
├── routes/
│   ├── upload.py
│   └── ask.py
├── services/
│   ├── parser.py
│   ├── chunker.py
│   ├── vectorstore.py
│   └── rag.py
```

---

## ⚙️ Kurulum

### 1. Repo'yu klonla

```bash
git clone https://github.com/your-repo-name.git
cd your-repo-name
```

---

### 2. Backend kurulumu

```bash
cd server
pip install -r requirements.txt
```

`.env` dosyası oluştur:

```env
OPENAI_API_KEY=your_api_key_here
```

Backend’i başlat:

```bash
uvicorn app:app --reload
```

---

### 3. Frontend kurulumu

```bash
cd client
pip install -r requirements.txt
streamlit run app.py
```

---

## 💡 Kullanım

1. Sidebar’dan dokümanları yükle
2. "Upload to DB" butonuna bas
3. Chat kısmından soru sor
4. AI cevabı ve kullanılan kaynakları incele
5. İstersen chat geçmişini indir

---

## 🧪 Örnek Kullanım

**Yüklenen dosya:** `project_report.pdf`

**Soru:**

```text
Bu projenin amacı nedir?
```

**Cevap:**

```text
Bu projenin amacı kullanıcıların kendi dokümanları üzerinden yapay zeka ile etkileşim kurabilmesini sağlamaktır.
```

**Kaynak:**

```text
project_report.pdf
```

---

## 📊 Özellikler

* ✅ PDF, TXT, DOCX desteği
* ✅ Çoklu doküman yükleme
* ✅ RAG tabanlı cevap üretimi
* ✅ Kaynak gösterimi (source citation)
* ✅ Chat geçmişi indirme
* ✅ Basit ve kullanıcı dostu arayüz

---

## ⚠️ Sınırlamalar

* Çok büyük dosyalarda performans düşebilir
* Embedding kalitesi kullanılan modele bağlıdır
* Chunking stratejisi daha geliştirilebilir

---

## 🔮 Geliştirme Fikirleri

* Semantic chunking
* Reranking (daha iyi retrieval)
* Çoklu dil desteği
* Daha gelişmiş prompt engineering
* Kalıcı vector database (Chroma / Qdrant)

---

## 👥 Ekip

Bu proje P2P programı kapsamında ekip çalışması olarak geliştirilmiştir.

---

## 🎥 Demo

👉 (Demo video linki buraya eklenecek)

---

## 📌 Not

Bu proje bir yarışmadan ziyade öğrenme odaklı bir süreçte geliştirilmiştir. Amaç sadece çalışan bir sistem üretmek değil, aynı zamanda modern AI sistemlerinin nasıl kurulduğunu deneyimlemektir.

📚 YZTA P2P AI Assistant Chatbot
RAG Based Intelligence System
🚀 Proje Hakkında
YZTA P2P AI Assistant, kullanıcıların yüklediği dokümanlar (PDF, TXT, DOCX) üzerinden yapay zeka ile etkileşim kurmasını sağlayan, yüksek performanslı bir Retrieval-Augmented Generation (RAG) uygulamasıdır. Bu sistem, genel amaçlı yapay zeka modellerini senin özel verilerinle besleyerek, dokümanlarındaki bilgileri anlayan ve buna göre aksiyon alan bir asistan sunar.

🎯 Amaç
FastAPI ve LangChain entegrasyonu ile modern bir AI backend mimarisi inşa etmek.

Vektör veritabanı kullanarak semantik arama  süreçlerini optimize etmek.

Kullanıcının kendi yerel verisiyle konuşabileceği, verimli ve hızlı bir chatbot deneyimi sağlamak.

🧠 Nasıl Çalışır?
Sistem, görsellerde belirtilen teknolojik akışı temel alır:

Doküman Yükleme: Kullanıcı PDF, TXT veya DOCX formatındaki belgelerini sisteme aktarır.

İşleme ve Parçalama: Metinler temizlenir ve anlamlı "chunk"lara bölünür.

Vektörleştirme: Her metin parçası OpenAI embedding modelleri ile sayısal vektörlere dönüştürülür.

Sorgulama: Kullanıcı soru sorduğunda, sadece sorusuyla en alakalı bilgi parçaları FAISS üzerinden çağrılır.

Üretim: LLM (GPT), kendisine sunulan bu özel bağlamı kullanarak en doğru cevabı üretir.

🏗️ Kullanılan Teknolojiler
Backend
FastAPI: Asenkron, hızlı ve güvenilir API yönetimi.

LangChain: LLM ve RAG süreçlerinin orkestrasyonu.

FAISS (Vector Database): Yüksek hızlı vektör arama ve depolama.

OpenAI API: Gelişmiş dil modelleri ve embedding işlemleri.

Frontend
Streamlit: Veri odaklı ve kullanıcı dostu arayüz tasarımı.

Doküman İşleme
PyPDF / python-docx: Farklı formatlardaki metinleri ayıklama motorları.

📁 Proje Yapısı
Plaintext

client/
├── app.py             # Streamlit ana giriş noktası
├── components/
│   ├── chatUI.py      # Mesajlaşma arayüzü bileşeni
│   └── uploader.py    # Sürükle-bırak dosya yükleme bileşeni
└── utils/
    └── api.py         # Backend haberleşme katmanı

server/
├── app.py             # FastAPI ana sunucu
├── routes/
│   ├── upload.py      # Dosya işleme ve vektörleme kanalı
│   └── ask.py         # Soru-Cevap (RAG) kanalı
└── services/
    ├── parser.py      # Dosya formatı ayrıştırıcı
    ├── vectorstore.py # Vektör veritabanı yönetimi
    └── rag_engine.py  # LLM ve Bağlam birleştirici
⚙️ Kurulum
Depoyu Klonlayın:

Bash

git clone https://github.com/kullanici-adiniz/yzta-p2p-ai-chatbot.git
cd yzta-p2p-ai-chatbot
Backend Kurulumu:

Bash

cd server
pip install -r requirements.txt
Frontend Kurulumu:

Bash

cd client
pip install -r requirements.txt
streamlit run app.py
📊 Temel Özellikler
✅ Hızlı Veri İşleme: Çok sayfalı dokümanlarda bile saniyeler içinde sonuç.

✅ Minimalist Tasarım: Odak noktası sadece chat ve veri olan modern arayüz.

✅ Format Çeşitliliği: PDF'den DOCX'e kadar geniş dosya desteği.

✅ Akıllı Sorgulama: Sadece kelime eşleşmesi değil, sorunun anlamını anlayan retrieval yapısı.

🔮 Geliştirme Yol Haritası
Kalıcı veritabanı sistemlerine (Pinecone, ChromaDB) geçiş.

Gelişmiş prompt mühendisliği ile daha spesifik cevaplar.

Birden fazla doküman arasında çapraz sorgu yapabilme yeteneği.

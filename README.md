# Smart Adaptive Learning Companion (SALC) - Student Activity Analysis

# Deskripsi
Proyek ini merupakan bagian dari pengembangan sistem **Smart Adaptive Learning Companion (SALC)** yang fokus pada analisis pola perilaku belajar siswa. Dengan memanfaatkan data aktivitas harian seperti jam belajar, tingkat kehadiran, dan penyelesaian tugas, proyek ini bertujuan untuk memberikan rekomendasi materi secara adaptif dan mendeteksi risiko penurunan nilai sejak dini. Analisis ini membantu pengajar dan sistem untuk memahami kapan seorang siswa membutuhkan intervensi khusus berdasarkan pola belajar dan penggunaan teknologi (EduTech) mereka, guna memastikan setiap siswa mencapai performa akademik yang optimal.

# Fitur Dashboard
- **Comprehensive Activity Metrics:** Ringkasan statistik utama meliputi Total Siswa, Rata-rata Jam Belajar, dan Persentase Penyelesaian Tugas.
- **Advanced Predictive Analysis:** Visualisasi tren *Assignment Completion* dan korelasi fitur terhadap *Final Grade* untuk deteksi dini kegagalan.
- **Engagement & Performance Mapping:** Analisis hubungan antara tingkat keterlibatan (*Engagement*) dengan performa akademik (*Final Grade*).
- **Risk & Digital Readiness Assessment:** Evaluasi tingkat risiko siswa (*Risk Level*) dan kesiapan digital (*Digital Readiness*) untuk strategi intervensi yang tepat.
- **Automated Adaptive Recommendations:** Sistem peringatan otomatis berbasis data untuk mengidentifikasi siswa yang membutuhkan bantuan segera.
- **Interactive Data Explorer:** Tabel interaktif yang memungkinkan eksplorasi mendalam terhadap seluruh fitur dataset secara langsung di dashboard.
- **Dynamic Filtering:** Filter sidebar berdasarkan *Learning Style* untuk analisis data yang lebih personal dan tersegmentasi.

# Setup Environment - Anaconda
conda create --name salc-activity python=3.14
conda activate salc-activity
pip install -r requirements.txt

# Setup Environment - Shell/Terminal
# Pastikan Anda berada di folder utama proyek (Aktivitas_Belajar)
cd dashboard
pipenv install
pipenv shell
pip install -r requirements.txt

# Run streamlit app
# Menjalankan aplikasi dari dalam folder dashboard
streamlit run Dashboard_AktivitasBelajar.py
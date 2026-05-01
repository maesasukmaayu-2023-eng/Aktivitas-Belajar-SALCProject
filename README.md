# 🎓 Smart Adaptive Learning Companion (SALC) - Student Activity Analysis

# Deskripsi
Proyek ini merupakan bagian dari pengembangan sistem **Smart Adaptive Learning Companion (SALC)** yang fokus pada analisis pola perilaku belajar siswa. Dengan memanfaatkan data aktivitas harian seperti jam belajar, tingkat kehadiran, dan penyelesaian tugas, proyek ini bertujuan untuk memberikan rekomendasi materi secara adaptif dan mendeteksi risiko penurunan nilai sejak dini. Analisis ini membantu pengajar dan sistem untuk memahami kapan seorang siswa membutuhkan intervensi khusus berdasarkan pola belajar dan penggunaan teknologi (EduTech) mereka, guna memastikan setiap siswa mencapai performa akademik yang optimal.

# Fitur Dashboard
- **Analisis Aktivitas Siswa:** Metrik real-time untuk memantau rata-rata jam belajar dan tingkat kehadiran.
- **Prediktor Penurunan Nilai:** Visualisasi tren *Assignment Completion* sebagai indikator utama deteksi dini risiko kegagalan.
- **Segmentasi Gaya Belajar:** Eksplorasi hubungan antara cara belajar siswa dengan efektivitas penggunaan teknologi pendidikan.
- **Rekomendasi Adaptif:** Sistem notifikasi otomatis bagi siswa yang berada di bawah ambang batas aktivitas normal.
- **Filter Interaktif:** Kemudahan dalam memfilter data berdasarkan kategori gaya belajar untuk analisis yang lebih spesifik.

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
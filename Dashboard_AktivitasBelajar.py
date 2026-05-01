import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Konfigurasi Halaman
st.set_page_config(page_title="SALC Dashboard", layout="wide")

# 1. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data_AktivitasBelajar.csv")
    return df

df = load_data()

# --- SIDEBAR ---
st.sidebar.header("Filter Dashboard")
# Filter Gaya Belajar
learning_style_options = df['LearningStyle'].unique()
selected_style = st.sidebar.multiselect("Pilih Gaya Belajar:", 
                                        options=learning_style_options, 
                                        default=learning_style_options)

# Filter Data berdasarkan sidebar
filtered_df = df[df['LearningStyle'].isin(selected_style)]

# --- MAIN PAGE ---
st.title("🎓 Smart Adaptive Learning Companion (SALC) - Student Activity Analysis")
st.markdown("Dashboard ini menganalisis pola belajar siswa untuk memberikan rekomendasi adaptif.")

# --- BARIS 1: METRIK UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Siswa", len(filtered_df))
with col2:
    st.metric("Rata-rata Jam Belajar", f"{round(filtered_df['StudyHours'].mean(), 1)} Jam")
with col3:
    st.metric("Penyelesaian Tugas", f"{round(filtered_df['AssignmentCompletion'].mean(), 1)}%")

st.divider()

# --- BARIS 2: PERTANYAAN BISNIS 1 (Segmentasi) ---
st.header("1. Segmentasi Pola Belajar & Tingkat Kelulusan")
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Gaya Belajar vs Jam Belajar")
    fig, ax = plt.subplots()
    sns.barplot(data=filtered_df, x='LearningStyle', y='StudyHours', hue='FinalGrade', palette='viridis', ax=ax)
    st.pyplot(fig)

with col_b:
    st.subheader("Pengaruh EduTech terhadap Kelulusan")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='EduTech', hue='FinalGrade', palette='magma', ax=ax)
    st.pyplot(fig)

# --- BARIS 3: PERTANYAAN BISNIS 2 (Prediktor Dini) ---
st.header("2. Deteksi Dini: Prediktor Penurunan Nilai")
st.markdown("Melihat tren bagaimana penyelesaian tugas mempengaruhi Grade akhir.")

# Line Plot Tren (Sesuai permintaan Anda sebelumnya)
fig_line, ax_line = plt.subplots(figsize=(10, 4))
trend_data = filtered_df.groupby('FinalGrade')['AssignmentCompletion'].mean().reset_index()
sns.lineplot(data=trend_data, x='FinalGrade', y='AssignmentCompletion', marker='o', color='teal', ax=ax_line)
ax_line.set_title("Tren Penurunan Penyelesaian Tugas terhadap Grade")
st.pyplot(fig_line)

# --- BARIS 4: REKOMENDASI ADAPTIF OTOMATIS ---
st.divider()
st.header("🤖 Rekomendasi Adaptif Sistem")
low_assignment = filtered_df[filtered_df['AssignmentCompletion'] < 70]
if not low_assignment.empty:
    st.warning(f"⚠️ Perhatian! Ada {len(low_assignment)} siswa dengan penyelesaian tugas di bawah 70%. Dibutuhkan intervensi segera!")
else:
    st.success("✅ Semua siswa dalam jalur belajar yang aman.")
# Proyek Analisis Data - Dicoding

## Penulis

- **Nama:** Muhammad Daffa Saptrian
- **Email:** dafsap03@gmail.com
- **Username Dicoding:** dafsap29

## Persiapan Lingkungan - Shell/Terminal

Untuk memulai proyek ini, lakukan langkah-langkah berikut di terminal:

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Struktur Berkas

- `Proyek_Analisis_Data.ipynb`: Jupyter Notebook/google colaboratory yang berisi analisis data.
- `dashboard/`: Folder yang berisi aplikasi dashboard berbasis Streamlit.

## Menjalankan Dashboard Streamlit

Jupyter Notebook dapat dibuka langsung melalui GitHub atau dijalankan di lingkungan yang mendukung Python.
Untuk menjalankan dashboard Streamlit secara lokal, ikuti langkah berikut:

```
cd dashboard
streamlit run dashboard.py
```

## Menjalankan Dashboard di Command Prompt

Pastikan Anda sudah berada di dalam folder `dashboard` sebelum menjalankan aplikasi Streamlit:

```
cd dashboard
streamlit run dashboard.py
```

Dengan menjalankan perintah di atas, dashboard akan otomatis terbuka di browser Anda.

## Menjalankan Streamlit di Localhost

1. Unduh dataset dalam format `.csv` yang dibutuhkan.
2. Jalankan kode dalam `dashboard.py` untuk melakukan Exploratory Data Analysis (EDA).
3. Instal Streamlit melalui command prompt dengan perintah:

```
pip install streamlit
```

4. Setelah instalasi selesai, navigasikan ke folder `dashboard` dan jalankan:

```
cd dashboard
streamlit run dashboard.py
```

5. Dashboard akan terbuka di browser secara lokal.

## Fitur Dashboard Streamlit

Dashboard yang dibuat mencakup fitur berikut:

1. Tampilan interaktif data mentah dan statistik ringkas.
2. Visualisasi data untuk menjawab pertanyaan bisnis utama:
   - Bagaimana tren penggunaan sepeda sepanjang tahun 2011?
   - Bagaimana pola pengaruh cuaca terhadap jumlah pengguna sepeda di tahun 2011?
   - Apakah ada perbedaan pola penggunaan sepeda pada hari kerja dan akhir pekan di 2011? Jika iya bagaimana polanya?

## Kebutuhan dan Instalasi

Proyek ini membutuhkan library berikut agar dapat berjalan dengan optimal:

- matplotlib==3.10.0
- matplotlib-inline==0.1.7
- numpy==2.2.3
- Pandas 2.2.3
- Seaborn 0.13.2
- Streamlit 1.43.2

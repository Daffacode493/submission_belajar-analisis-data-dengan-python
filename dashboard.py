import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime

# Mengatur gaya tampilan seaborn
sns.set_theme(style='whitegrid')

# Membaca dataset dari file CSV
data_path = "all_data.csv"
df = pd.read_csv(data_path)

# Membersihkan dataset
drop_columns = ['instant', 'temp', 'atemp', 'hum', 'windspeed']
df.drop(columns=drop_columns, inplace=True)

df['yr'] = df['yr'].map({0: '2011', 1: '2012'})
df['mnth'] = df['mnth'].map({1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'Mei', 6: 'Jun',
                              7: 'Jul', 8: 'Agt', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Des'})
df['season'] = df['season'].map({1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'})
df['weekday'] = df['weekday'].map({0: 'Minggu', 1: 'Senin', 2: 'Selasa', 3: 'Rabu', 4: 'Kamis', 5: 'Jumat', 6: 'Sabtu'})
df['weathersit'] = df['weathersit'].map({1: 'Cerah', 2: 'Berawan', 3: 'Hujan/Salju', 4: 'Buruk'})

# Konversi tanggal ke format datetime
df['dteday'] = pd.to_datetime(df['dteday'])

df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']] = df[
    ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']].astype('category')

# Sidebar untuk input rentang tanggal
st.sidebar.header("Filter Rentang Tanggal")
start_date = st.sidebar.date_input("Pilih Tanggal Awal", value=datetime.date(2012, 1, 1))
end_date = st.sidebar.date_input("Pilih Tanggal Akhir", value=datetime.date(2012, 12, 31))

# Memfilter data sesuai rentang tanggal yang dipilih
filtered_df = df[(df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))]

def rent_per_month(df):
    monthly_df = df.groupby('mnth').agg({'cnt': 'sum'}).reset_index()
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agt', 'Sep', 'Okt', 'Nov', 'Des']
    monthly_df['mnth'] = pd.Categorical(monthly_df['mnth'], categories=month_order, ordered=True)
    return monthly_df

def season_weather_avg(df):
    return df.groupby(['season', 'weathersit']).agg({'cnt': 'mean'}).reset_index()

# Header aplikasi
st.title("Analisis Penggunaan Sepeda Tahun 2011")

# Data jumlah penyewa sepeda per bulan
monthly_data = rent_per_month(filtered_df)

st.subheader("Jumlah Penyewa Sepeda per Bulan")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=monthly_data, x='mnth', y='cnt', palette='viridis', ax=ax)
ax.set_title(f'Total Penyewa Sepeda ({start_date} - {end_date})')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penyewa')
st.pyplot(fig)

if not monthly_data.empty:
    peak_month = monthly_data.loc[monthly_data['cnt'].idxmax()]
    st.write(f"Bulan dengan pengguna terbanyak: **{peak_month['mnth']}**, dengan **{peak_month['cnt']}** penyewa.")
else:
    st.write("Tidak ada data dalam rentang tanggal yang dipilih.")

# Pilihan bulan spesifik
st.subheader("Detail Penggunaan Sepeda per Bulan")
available_months = list(monthly_data['mnth'].cat.categories)
selected_month = st.selectbox("Pilih Bulan:", available_months)

month_data = monthly_data[monthly_data['mnth'] == selected_month]
if not month_data.empty:
    st.write(f"Jumlah penyewa pada bulan **{selected_month}**: **{month_data['cnt'].values[0]}**")
else:
    st.write(f"Tidak ada data untuk bulan **{selected_month}**.")

# Analisis penggunaan sepeda berdasarkan cuaca dan musim
st.subheader("Pengaruh Cuaca dan Musim terhadap Penggunaan Sepeda")
season_weather_data = season_weather_avg(filtered_df)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=season_weather_data, x='weathersit', y='cnt', hue='season', palette='coolwarm', ax=ax2)
ax2.set_title("Rata-Rata Pengguna Sepeda Berdasarkan Cuaca & Musim")
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Pengguna")
st.pyplot(fig2)

if not season_weather_data.empty:
    peak_weather = season_weather_data.loc[season_weather_data['cnt'].idxmax()]
    st.write(f"Kondisi dengan pengguna terbanyak: **{peak_weather['weathersit']}** saat musim **{peak_weather['season']}**, rata-rata **{peak_weather['cnt']:.2f}** penyewa.")
else:
    st.write("Tidak ada data untuk rentang tanggal yang dipilih.")

# Pilihan kondisi cuaca
st.sidebar.subheader("Pilih Kondisi Cuaca")
available_weather = list(season_weather_data['weathersit'].unique())
selected_weather = st.sidebar.selectbox("Pilih kondisi cuaca:", available_weather)

weather_data = season_weather_data[season_weather_data['weathersit'] == selected_weather]
if not weather_data.empty:
    st.sidebar.write(f"**Detail Pengguna untuk {selected_weather}:**")
    for _, row in weather_data.iterrows():
        st.sidebar.write(f"- Musim **{row['season']}**: {row['cnt']:.2f} pengguna rata-rata")
else:
    st.sidebar.write("Tidak ada data untuk kondisi ini.")
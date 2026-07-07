# =========================================================
# Program Perhitungan Biaya Parkir - Kasus Bisnis Digital
# =========================================================

import streamlit as st

# Tampilan tabel tarif di atas web
st.text("""| Kode | Jenis Kendaraan | Tarif 2 Jam Awal | Per Jam Berikutnya |
| mtr  | Motor           | 3000             | 1000               |
| mbl  | Mobil           | 5000             | 2000               |
| bus  | Bus             | 10000            | 5000               |
===================================================================""")

# --- SEMUA INPUT TERMINAL DIUBAH JADI INPUT WEB ---
nama = st.text_input("nama pemilik     :")
nopol = st.text_input("no polisi        :")
kode = st.text_input("masukkan kode    :").lower()

# # Kondisi Penentuan Jenis Kendaraan dan Tarif (LOGIKA ASLI LU)
if kode == "mtr":
    jenis = 'Motor'
    tarif_awal = 3000
    tarif_per_jam = 1000
elif kode == "mbl":
    jenis = 'Mobil'
    tarif_awal = 5000
    tarif_per_jam = 2000
else:
    jenis = 'Bus'
    tarif_awal = 10000
    tarif_per_jam = 5000

# Input durasi diganti jadi number_input Streamlit
durasi = st.number_input('masukkan durasi parkir (jam) :', min_value=0, step=1, value=0)

# Perhitungan Durasi dan Biaya Parkir (LOGIKA ASLI LU)
if durasi > 2:
    biaya_parkir = tarif_awal + ((durasi - 2) * tarif_per_jam)
else:
    biaya_parkir = tarif_awal

# Kondisi Tiket Hilang (Denda) - Diubah jadi pilihan Klik y/t di web
hilang = st.radio("tiket hilang? (y/t) :", ["t", "y"])
if hilang == "y":
    denda = 20000
else:
    denda = 0

total_bayar = biaya_parkir + denda

# Tampilkan total bayar dulu sebelum user memasukkan uang
st.markdown("---")
st.subheader(f"total denda yang didapat : {denda}")
st.subheader(f"total bayar             : {total_bayar}")
st.markdown("---")

# Input uang bayar di web
byr = st.number_input('masukkan uang bayar     :', min_value=0, step=1000, value=0)
kembalian = (byr - total_bayar)

# Jika user sudah membayar, langsung munculkan kembalian dan struknya
if byr > 0:
    st.write(f"uang kembali            : {kembalian}")
    st.write("=========terima kasih=========")
    
    # --- STRUK PARKIR AKHIR (VERSI WEB) ---
    st.text("""===================================
           struk parkir
===================================""")
    st.text(f"nama pemilik    : {nama}")
    st.text(f"no polisi       : {nopol}")
    st.text(f"kode            : {kode}")
    st.text(f"jenis kendaraan : {jenis}")
    st.text(f"durasi parkir   : {durasi} jam")
    st.text(f"biaya parkir    : {biaya_parkir}")
    st.text(f"denda tiket     : {denda}")
    st.text("-----------------------------------")
    st.text(f"total bayar     : {total_bayar}")
    st.text(f"u.bayar         : {byr}")
    st.text(f"u.kembali       : {kembalian}")
    st.text("-----------------------------------")
    st.success("Semoga Selamat Sampai Tujuan")
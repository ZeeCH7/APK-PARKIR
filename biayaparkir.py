import streamlit as st

# --- 1. SETTING HALAMAN (LAYOUT LEBAR) ---
st.set_page_config(page_title="XYZ Parkir — Kalkulator Biaya", layout="wide")

# --- 2. HEADER APLIKASI ---
st.title("🔵 APK PARKIR")
st.subheader("Sistem Perhitungan Parkir Otomatis")
st.write("Masukkan data transaksi kendaraan untuk menghitung biaya parkir, denda, dan kembalian secara otomatis.")
st.markdown("---")

# --- 3. MEMBAGI LAYOUT: KIRI (INPUT) & KANAN (STRUK) ---
kolom_input, kolom_blank, kolom_struk = st.columns([5, 1, 5])

with kolom_input:
    st.subheader("📋 INPUT TRANSAKSI")
    
    # Menampilkan info tarif biar rapi
    st.info("💡 **INFO TARIF:**\n* **MTR (Motor):** Rp 3.000 (2 Jam Awal) | +Rp 1.000 /jam berikutnya\n* **MBL (Mobil):** Rp 5.000 (2 Jam Awal) | +Rp 2.000 /jam berikutnya\n* **BUS (Bus):** Rp 10.000 (2 Jam Awal) | +Rp 5.000 /jam berikutnya")
    
    # Input field nama dan nopol (KOSONG DI AWAL, BIAR GAK OTOMATIS KEISI)
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        nama = st.text_input("Nama pemilik :", value="")
    with sub_col2:
        nopol = st.text_input("No. polisi :", value="")
        
    pilihan_jenis = st.selectbox("Jenis kendaraan :", ["MTR — Motor / Roda Dua", "MBL — Mobil / Roda Empat", "BUS — Bus / Kendaraan Besar"])
    
    # Logika konversi selectbox ke variabel rumus asli lu
    if "MTR" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mtr", "Motor", 3000, 1000
    elif "MBL" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mbl", "Mobil", 5000, 2000
    else:
        kode, jenis, tarif_awal, tarif_per_jam = "bus", "Bus", 10000, 5000

    durasi = st.number_input("Durasi parkir (jam) :", min_value=0, step=1, value=0)
    
    hilang_input = st.radio("Tiket hilang?", ["Tidak", "Ya (+Rp 20.000)"], horizontal=True)
    denda = 20000 if "Ya" in hilang_input else 0
    
    # Hitung biaya dasar parkir (LOGIKA ASLI LU)
    if durasi > 2:
        biaya_parkir = tarif_awal + ((durasi - 2) * tarif_per_jam)
    else:
        # Jika durasi masih 0 jam, biaya parkir 0 dulu biar pas di awal gak langsung bayar
        biaya_parkir = tarif_awal if durasi > 0 else 0
        
    total_bayar = biaya_parkir + denda
    
    byr = st.number_input("Uang bayar :", min_value=0, step=1000, value=0)
    kembalian = byr - total_bayar

# --- 4. LOGIKA TAMPILAN STRUK DI KOLOM KANAN (OTOMATIS / REAL-TIME) ---
with kolom_struk:
    st.subheader("🧾 NOTA / STRUK PEMBAYARAN")
    
    # Struk otomatis muncul atau ter-update secara Live jika user sudah mengisi durasi atau nama
    if durasi > 0 or nama != "" or nopol != "":
        with st.container(border=True):
            st.header("📄 STRUK PARKIR DIGITAL")
            st.markdown("##### Perusahaan Parkir XYZ")
            st.markdown("---")
            
            # Tampilan data memakai text bawaan yang rapi
            st.write(f"👤 **Nama Pemilik** : {nama if nama != '' else '-'}")
            st.write(f"🔢 **No. Polisi** : {nopol if nopol != '' else '-'}")
            st.write(f"🔠 **Kode / Jenis** : {kode.upper()} / {jenis}")
            st.write(f"⏱️ **Durasi Parkir** : {durasi} Jam")
            st.markdown("---")
            
            st.write(f"💵 **Biaya Parkir** : Rp {biaya_parkir:,}")
            st.write(f"⚠️ **Denda Tiket** : Rp {denda:,}")
            st.markdown("---")
            
            # Menampilkan Total, Bayar, Kembali secara real-time
            m1, m2, m3 = st.columns(3)
            m1.metric("TOTAL BAYAR", f"Rp {total_bayar:,}")
            m2.metric("UANG BAYAR", f"Rp {byr:,}")
            m3.metric("KEMBALIAN", f"Rp {kembalian:,}")
            
            st.markdown("---")
            st.success("✨ Semoga Selamat Sampai Tujuan ~ Terima Kasih ✨")
            
        # Peringatan kalau uangnya kurang (hanya muncul kalau user udah coba bayar)
        if byr > 0 and kembalian < 0:
            st.error("🚨 Uang yang dimasukkan kurang, bos!")
        elif byr > 0 and kembalian >= 0:
            st.balloons() # Efek animasi sukses terbang pas lunas
    else:
        st.info("🖨️ Silakan ketik nama/nopol atau naikkan durasi jam di sebelah kiri. Nota struk akan otomatis terhitung secara LIVE di sini.")
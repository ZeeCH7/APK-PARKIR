import streamlit as st

# --- 1. SETTING HALAMAN HALUS (LAYOUT LEBAR) ---
st.set_page_config(page_title="XYZ Parkir — Kalkulator Biaya", layout="wide")

# --- 2. HEADER APLIKASI ---
st.title("🔵 PERUSAHAAN PARKIR XYZ")
st.subheader("Sistem Perhitungan Parkir Otomatis")
st.write("Masukkan data transaksi kendaraan untuk menghitung biaya parkir, denda, dan kembalian secara otomatis.")
st.markdown("---")

# --- 3. MEMBAGI LAYOUT: KIRI (INPUT) & KANAN (STRUK) ---
kolom_input, kolom_blank, kolom_struk = st.columns([5, 1, 5])

with kolom_input:
    st.subheader("📋 INPUT TRANSAKSI")
    
    # Menampilkan info tarif biar rapi
    st.info("💡 **INFO TARIF:**\n* **MTR (Motor):** Rp 3.000 (2 Jam Awal) | +Rp 1.000 /jam berikutnya\n* **MBL (Mobil):** Rp 5.000 (2 Jam Awal) | +Rp 2.000 /jam berikutnya\n* **BUS (Bus):** Rp 10.000 (2 Jam Awal) | +Rp 5.000 /jam berikutnya")
    
    # Input field nama dan nopol bersebelahan
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        nama = st.text_input("Nama pemilik :", value="Farhan")
    with sub_col2:
        nopol = st.text_input("No. polisi :", value="F 1234 ABC")
        
    pilihan_jenis = st.selectbox("Jenis kendaraan :", ["MTR — Motor / Roda Dua", "MBL — Mobil / Roda Empat", "BUS — Bus / Kendaraan Besar"])
    
    # Logika konversi selectbox ke variabel rumus asli lu
    if "MTR" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mtr", "Motor", 3000, 1000
    elif "MBL" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mbl", "Mobil", 5000, 2000
    else:
        kode, jenis, tarif_awal, tarif_per_jam = "bus", "Bus", 10000, 5000

    durasi = st.number_input("Durasi parkir (jam) :", min_value=0, step=1, value=3)
    
    hilang_input = st.radio("Tiket hilang?", ["Tidak", "Ya (+Rp 20.000)"], horizontal=True)
    denda = 20000 if "Ya" in hilang_input else 0
    
    # Hitung biaya dasar parkir (LOGIKA ASLI LU KAGAK BERUBAH)
    if durasi > 2:
        biaya_parkir = tarif_awal + ((durasi - 2) * tarif_per_jam)
    else:
        biaya_parkir = tarif_awal
        
    total_bayar = biaya_parkir + denda
    
    byr = st.number_input("Uang bayar :", min_value=0, step=1000, value=5000)
    kembalian = byr - total_bayar

    # Tombol utama bergaya Primary (warna biru bawaan streamlit)
    tombol_cetak = st.button("🖨️ Hitung & Cetak Struk", type="primary", use_container_width=True)

# --- 4. LOGIKA TAMPILAN STRUK DI KOLOM KANAN ---
with kolom_struk:
    st.subheader("🧾 NOTA / STRUK PEMBAYARAN")
    
    if tombol_cetak or byr > 0:
        # Menggunakan st.container ber-border biar mirip kotak kertas struk
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center;'>📄 STRUK PARKIR DIGITAL</h3>", unsafe_allowed_html=True)
            st.markdown("<p style='text-align: center; color: gray;'>Perusahaan Parkir XYZ</p>", unsafe_allowed_html=True)
            st.markdown("---")
            
            # Tampilan data memakai text bawaan yang rapi
            st.write(f"👤 **Nama Pemilik** : {nama}")
            st.write(f"🔢 **No. Polisi** : {nopol}")
            st.write(f"🔠 **Kode / Jenis** : {kode.upper()} / {jenis}")
            st.write(f"⏱️ **Durasi Parkir** : {durasi} Jam")
            st.markdown("---")
            
            st.write(f"💵 **Biaya Parkir** : Rp {biaya_parkir:,}")
            st.write(f"⚠️ **Denda Tiket** : Rp {denda:,}")
            st.markdown("---")
            
            # Menampilkan Total, Bayar, Kembali dengan widget Metric yang modern
            m1, m2, m3 = st.columns(3)
            m1.metric("TOTAL BAYAR", f"Rp {total_bayar:,}")
            m2.metric("UANG BAYAR", f"Rp {byr:,}")
            m3.metric("KEMBALIAN", f"Rp {kembalian:,}")
            
            st.markdown("---")
            st.success("✨ Semoga Selamat Sampai Tujuan ~ Terima Kasih ✨")
            
        # Peringatan kalau uangnya kurang
        if kembalian < 0:
            st.error("🚨 Uang yang dimasukkan kurang, bos!")
        else:
            st.balloons() # Efek animasi sukses
    else:
        st.info("🖨️ Silakan isi data di sebelah kiri lalu klik tombol untuk memunculkan nota di sini.")
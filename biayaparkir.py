import streamlit as st

# --- 1. SETTING HALAMAN & CSS INJEKSI (SULAP DARK THEME) ---
st.set_page_config(page_title="XYZ Parkir — Kalkulator Biaya", layout="wide")

# Trik CSS tingkat dewa buat maksa Streamlit jadi bertema Dark & bergaya mirip SS lu
st.markdown("""
    <style>
        /* Mengubah background utama jadi gelap */
        .stApp {
            background-color: #0d1b2a;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        
        /* Mengubah styling untuk card input data */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #1b263b;
            border-radius: 15px;
            padding: 20px;
            border: 1px solid #2e3d52;
        }
        
        /* Mengubah gaya tombol Hitung & Cetak Struk */
        div.stButton > button {
            background-color: #00b4d8 !important;
            color: #0d1b2a !important;
            font-weight: bold !important;
            font-size: 16px !important;
            border-radius: 10px !important;
            border: none !important;
            height: 50px !important;
            width: 100% !important;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background-color: #90e0ef !important;
            box-shadow: 0px 0px 15px rgba(0, 180, 216, 0.6);
        }
        
        /* Desain Struk Putih Gaya Kasir */
        .struk-container {
            background-color: #f8f9fa;
            color: #212529;
            padding: 25px;
            border-radius: 4px;
            font-family: 'Courier New', Courier, monospace;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            border-top: 5px dashed #ced4da;
            border-bottom: 5px dashed #ced4da;
        }
    </style>
""", unsafe_allowed_html=True)

# --- 2. HERO HEADER ---
st.markdown("<p style='color: #00b4d8; font-size: 13px; font-weight: bold; letter-spacing: 1px;'>🔵 PERUSAHAAN PARKIR XYZ • SISTEM OTOMATIS</p>", unsafe_allowed_html=True)
st.markdown("<h1 style='font-size: 45px; margin-top: -10px;'>Biaya <span style='color: #00b4d8;'>Parkir</span></h1>", unsafe_allowed_html=True)
st.markdown("<p style='color: #a3b18a; margin-top: -15px;'>Masukkan data transaksi kendaraan untuk menghitung biaya parkir, denda, dan kembalian secara otomatis.</p>", unsafe_allowed_html=True)
st.markdown("<br>", unsafe_allowed_html=True)

# --- 3. MEMBAGI LAYOUT: KIRI (INPUT) & KANAN (STRUK) ---
kolom_input, kolom_blank, kolom_struk = st.columns([5, 1, 5])

with kolom_input:
    st.markdown("<h4 style='color: #00b4d8; margin-bottom: 20px;'>INPUT TRANSAKSI</h4>", unsafe_allowed_html=True)
    
    # Mini info tarif di atas input
    st.code("MTR: 3.000 / +1.000   |   MBL: 5.000 / +2.000   |   BUS: 10.000 / +5.000")
    
    # Input field berjejer
    sub_col1, sub_col2 = st.columns(2)
    with sub_col1:
        nama = st.text_input("Nama pemilik :", value="Farhan")
    with sub_col2:
        nopol = st.text_input("No. polisi :", value="F 1234 ABC")
        
    pilihan_jenis = st.selectbox("Jenis kendaraan :", ["MTR — Motor / Roda Dua", "MBL — Mobil / Roda Empat", "BUS — Bus / Kendaraan Besar"])
    
    # Logika konversi selectbox ke variabel asli lu
    if "MTR" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mtr", "Motor", 3000, 1000
    elif "MBL" in pilihan_jenis:
        kode, jenis, tarif_awal, tarif_per_jam = "mbl", "Mobil", 5000, 2000
    else:
        kode, jenis, tarif_awal, tarif_per_jam = "bus", "Bus", 10000, 5000

    durasi = st.number_input("Durasi parkir (jam) :", min_value=0, step=1, value=3)
    
    hilang_input = st.radio("Tiket hilang?", ["Tidak", "Ya (+Rp 20.000)"], horizontal=True)
    denda = 20000 if "Ya" in hilang_input else 0
    
    # Hitung biaya dasar parkir (LOGIKA ASLI LU)
    if durasi > 2:
        biaya_parkir = tarif_awal + ((durasi - 2) * tarif_per_jam)
    else:
        biaya_parkir = tarif_awal
        
    total_bayar = biaya_parkir + denda
    
    byr = st.number_input("Uang bayar :", min_value=0, step=1000, value=5000)
    kembalian = byr - total_bayar

    # Tombol pemicu cetak struk
    tombol_cetak = st.button("Hitung & Cetak Struk")

# --- 4. LOGIKA TAMPILAN STRUK DI KOLOM KANAN ---
with kolom_struk:
    if tombol_cetak or byr > 0:
        # Template HTML Struk Kasir Putih
        st.markdown(f"""
            <div class="struk-container">
                <h3 style="text-align: center; margin-bottom: 5px; font-weight: bold;">STRUK PARKIR</h3>
                <p style="text-align: center; font-size: 12px; margin-top: 0;">Perusahaan Parkir XYZ</p>
                <p>------------------------------------------</p>
                <p><b>Nama pemilik</b>  <span style="float: right;">{nama}</span></p>
                <p><b>No. polisi</b>   <span style="float: right;">{nopol}</span></p>
                <p><b>Kode</b>         <span style="float: right;">{kode.upper()}</span></p>
                <p><b>Jenis kendaraan</b> <span style="float: right;">{jenis}</span></p>
                <p><b>Durasi parkir</b> <span style="float: right;">{durasi} jam</span></p>
                <p>------------------------------------------</p>
                <p><b>Biaya parkir</b>  <span style="float: right;">Rp {biaya_parkir:,}</span></p>
                <p><b>Denda tiket</b>   <span style="float: right;">Rp {denda:,}</span></p>
                <p>------------------------------------------</p>
                <h4 style="margin: 10px 0;"><b>TOTAL BAYAR</b> <span style="float: right;"><b>Rp {total_bayar:,}</b></span></h4>
                <p><b>Uang bayar</b>    <span style="float: right;">Rp {byr:,}</span></p>
                <p><b>Uang kembali</b>  <span style="float: right;">Rp {kembalian:,}</span></p>
                <p>------------------------------------------</p>
                <p style="text-align: center; font-size: 12px; margin-bottom: 0;">Semoga Selamat Sampai Tujuan<br>~ Terima Kasih ~</p>
            </div>
        """, unsafe_allowed_html=True)
        
        if kembalian < 0:
            st.warning("⚠️ Uang bayar kurang bos!")
        else:
            st.balloons()
    else:
        # Tampilan awal kalau belum klik cetak / isi uang
        st.markdown("""
            <div style="border: 2px dashed #2e3d52; border-radius: 10px; padding: 50px; text-align: center; color: #64748b; margin-top: 50px;">
                🖨️ Silakan isi data di sebelah kiri lalu klik "Hitung & Cetak Struk" untuk memunculkan nota pembayaran.
            </div>
        """, unsafe_allowed_html=True)
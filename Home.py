import streamlit as st

# 1. Konfigurasi Halaman & Tab Browser (Chrome)
st.set_page_config(
    page_title="SWIM - AI English Assistant",
    page_icon="assets/swim.png",  # Logo swim.png dipasang di tab Chrome di sini
    layout="wide"
)

# 2. Header: Logo (Kiri) & Judul Utama (Kanan)
col_logo, col_title = st.columns([1, 5])

with col_logo:
    # Menampilkan logo swim.png di halaman utama
    st.image("assets/swim.png", width=90)

with col_title:
    # Judul persis seperti sketsa
    st.markdown(
        """
        <h2 style='margin-top: 10px; font-weight: 700; font-size: clamp(1.4rem, 4vw, 2.2rem);'>
            Speaking & Writing Improvement Mate
        </h2>
        """, 
        unsafe_allow_html=True
    )

# 3. Subtitle / Deskripsi di Bawah Header
st.write("Improve your English with AI-powered writing and speaking feedback")

# Garis Pemisah
st.markdown("---")

# 4. Petunjuk Penggunaan
st.info("👈 **Get Started:** Select **Writing Evaluation** or **Speaking Evaluation** from the sidebar menu to begin!")

import textwrap
import streamlit as st


def render_sidebar():
    with st.sidebar:
        # Pendorong ke bawah
        st.markdown(
            "<div style='flex-grow: 1; height: 30vh;'></div>",
            unsafe_allow_html=True,
        )

        # Hapus semua tab/spasi di awal baris di dalam string multiline ini
        html_content = textwrap.dedent("""
<div style="border-top: 1px solid #E2E8F0; padding-top: 15px; margin-top: 20px;">
    <div style="font-size: 22px; font-weight: 800; background: linear-gradient(90deg, #1D4ED8 0%, #06B6D4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; letter-spacing: 0.5px;">
        SWIM
    </div>
    <div style="font-size: 11px; color: #64748B; margin-top: 4px; font-weight: 500; line-height: 1.3;">
        Speaking & Writing Improvement Mate
    </div>
    <div style="font-size: 10px; color: #94A3B8; margin-top: 12px;">
        © 2026 SWIM • Developed by Hastisf.
    </div>
</div>
        """)

        st.markdown(html_content, unsafe_allow_html=True)


render_sidebar()

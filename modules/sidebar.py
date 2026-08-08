import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.markdown(
            """
            <div style="
                margin-top:-5px;
                margin-bottom:15px;
            ">
                <div style="
                    font-size:20px;
                    font-weight:700;
                    color:#0F172A;
                ">
                    SWIM
                </div>

                <div style="
                    font-size:12px;
                    color:#64748B;
                    margin-top:8px;
                    line-height:1.4;
                ">
                    Speaking & Writing Improvement Mate
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

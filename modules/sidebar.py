import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.markdown(
            """
            <div style="
                margin-top:30px;
                margin-bottom:20px;
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
                    margin-top:3px;
                    line-height:1.4;
                ">
                    Speaking & Writing Improvement Mate
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

import streamlit as st


def render_sidebar():
    with st.sidebar:

        st.image("assets/swim.png", width=70)

        st.markdown(
            """
            <div style="
                margin-top:-10px;
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
                ">
                    AI English Assistant
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                border-top:1px solid #E2E8F0;
                margin:10px 0 20px 0;
            "></div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="
                color:#64748B;
                font-size:12px;
                line-height:1.5;
            ">
                Improve your English skills with
                AI-powered writing and speaking feedback.
            </div>
            """,
            unsafe_allow_html=True
        )

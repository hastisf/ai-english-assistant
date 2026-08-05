import pandas as pd
import streamlit as st
from modules.database import get_all_evaluations

st.markdown(
    """
    <h2 style='font-size: clamp(1.4rem, 4vw, 2.2rem); font-weight: 700; margin-bottom: 0.5rem;'>
        📜 Evaluation History
    </h2>
    """, 
    unsafe_allow_html=True
)
rows = get_all_evaluations()

if rows:
  df = pd.DataFrame(
      rows,
      columns=[
          "ID",
          "Evaluation Type",
          "User Input / Transcript",
          "Overall Score",
          "Created At",
      ],
  )
  st.dataframe(df, use_container_width=True)

  # Export to CSV
  csv = df.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="📥 Export to CSV",
      data=csv,
      file_name="evaluation_history.csv",
      mime="text/csv",
  )
else:
  st.info("No evaluation history found yet.")

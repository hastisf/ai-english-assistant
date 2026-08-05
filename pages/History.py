import pandas as pd
import streamlit as st
from modules.database import get_all_evaluations

st.title("📜 Evaluation History")

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

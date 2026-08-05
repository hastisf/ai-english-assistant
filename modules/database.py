import sqlite3

DB_PATH = "database/history.db"


def init_db():
  """Membuat tabel jika belum ada."""
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            eval_type TEXT,
            user_input TEXT,
            overall_score INTEGER,
            feedback_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
  conn.commit()
  conn.close()


def save_evaluation(
    eval_type: str, user_input: str, overall_score: int, feedback_json: str
):
  init_db()
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT INTO evaluations (eval_type, user_input, overall_score, feedback_json)
        VALUES (?, ?, ?, ?)
    """,
      (eval_type, user_input, overall_score, feedback_json),
  )
  conn.commit()
  conn.close()


def get_all_evaluations():
  init_db()
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()
  cursor.execute(
      "SELECT id, eval_type, user_input, overall_score, created_at FROM"
      " evaluations ORDER BY created_at DESC"
  )
  rows = cursor.fetchall()
  conn.close()
  return rows

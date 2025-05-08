# init_db.py
import sqlite3

# Connect to database (creates chatbot.db if it doesn't exist)
conn = sqlite3.connect('database/chatbot.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS faq (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL
    )
''')

# Sample data
faq_entries = [
    ("What courses are offered?", "We offer B.Tech, M.Tech, MBA, BBA, B.Sc, and diploma programs."),
    ("How can I apply for admission?", "You can apply online at our university portal."),
    ("What is the eligibility for B.Tech?", "You need at least 60% in 12th grade with PCM."),
    ("What is the fee structure?", "The tuition fee for B.Tech is ₹90,000 per year."),
    ("Where can I find the exam schedule?", "Check the student portal under 'Exam Section'.")
]

# Insert data into table
cursor.executemany('INSERT INTO faq (question, answer) VALUES (?, ?)', faq_entries)

# Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database created and sample data inserted.")

import streamlit as st
import pandas as pd
import mysql.connector

# Cache DB connection
@st.cache_resource
def get_connection():
    return mysql.connector.connect(
        host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
        user='3dNgmvyBKujEW7H.root',
        password='wXyH5deMR3jzRbao',
        database='placement_db')

conn = get_connection()
cursor = conn.cursor(dictionary=True)

st.title("🎓 Placement Eligibility Filter App")

st.sidebar.header("🔍 Eligibility Criteria")
min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 200, 50)
min_communication = st.sidebar.slider("Min Communication Score", 0, 100, 75)
status = st.sidebar.selectbox("Placement Status", ["All", "Ready", "Placed", "Not Ready"])

query = f"""
SELECT s.student_id, s.name, p.problems_solved, ss.communication, pl.placement_status
FROM Students s
JOIN Programming p ON s.student_id = p.student_id
JOIN SoftSkills ss ON s.student_id = ss.student_id
JOIN Placements pl ON s.student_id = pl.student_id
WHERE p.problems_solved >= {min_problems}
  AND ss.communication >= {min_communication}
"""

if status != "All":
    query += f" AND pl.placement_status = '{status}'"

cursor.execute(query)
data = cursor.fetchall()
df = pd.DataFrame(data)

st.subheader("📋 Eligible Students")
st.dataframe(df, use_container_width=True)

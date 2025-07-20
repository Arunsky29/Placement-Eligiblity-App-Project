import mysql.connector
import pandas as pd

# ---- DATABASE CONNECTION ----
def connect_to_tidb():
    return mysql.connector.connect(
       host='gateway01.ap-southeast-1.prod.aws.tidbcloud.com',
       port=4000,
       user='3dNgmvyBKujEW7H.root',
       password='wXyH5deMR3jzRbao',
       database='placement_db')

# ---- QUERY AND DISPLAY ----
def run_query(query, conn):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    return df

# ---- ALL 10 INSIGHTS ----
def show_insights(conn):

    print("\n1 Top 5 Students by Project Score:")
    print(run_query("""
        SELECT s.name, p.latest_project_score
        FROM Students s
        JOIN Programming p ON s.student_id = p.student_id
        ORDER BY p.latest_project_score DESC
        LIMIT 5
    """, conn))

    print("\n2 Average Soft Skills by Batch:")
    print(run_query("""
        SELECT s.course_batch,
               ROUND(AVG(ss.communication),2) AS avg_communication,
               ROUND(AVG(ss.presentation),2) AS avg_presentation
        FROM Students s
        JOIN SoftSkills ss ON s.student_id = ss.student_id
        GROUP BY s.course_batch
    """, conn))

    print("\n3 Placement Status Count:")
    print(run_query("""
        SELECT placement_status, COUNT(*) AS count
        FROM Placements
        GROUP BY placement_status
    """, conn))

    print("\n4 Average & Max Placement Package by Company:")
    print(run_query("""
        SELECT company_name,
               ROUND(AVG(placement_package),2) AS avg_package,
               MAX(placement_package) AS max_package
        FROM Placements
        WHERE placement_status = 'Placed' AND placement_package IS NOT NULL
        GROUP BY company_name
        ORDER BY avg_package DESC
    """, conn))

    print("\n5 Gender Count per Batch:")
    print(run_query("""
        SELECT course_batch, gender, COUNT(*) AS count
        FROM Students
        GROUP BY course_batch, gender
        ORDER BY course_batch, gender
    """, conn))

    print("\n6 Avg Problems Solved per Programming Language:")
    print(run_query("""
        SELECT language, ROUND(AVG(problems_solved), 2) AS avg_solved
        FROM Programming
        GROUP BY language
        ORDER BY avg_solved DESC
    """, conn))

    print("\n7 Most Common Student City:")
    print(run_query("""
        SELECT city, COUNT(*) AS count
        FROM Students
        GROUP BY city
        ORDER BY count DESC
        LIMIT 1
    """, conn))

    print("\n8 Students with 0 Internships:")
    print(run_query("""
        SELECT s.student_id, s.name
        FROM Students s
        JOIN Placements p ON s.student_id = p.student_id
        WHERE p.internships_completed = 0
    """, conn))

    print("\n9 Batch with Highest Avg Mock Interview Score:")
    print(run_query("""
        SELECT s.course_batch, ROUND(AVG(p.mock_interview_score), 2) AS avg_mock_score
        FROM Students s
        JOIN Placements p ON s.student_id = p.student_id
        GROUP BY s.course_batch
        ORDER BY avg_mock_score DESC
        LIMIT 1
    """, conn))

    print("\n10 Students who Cleared > 3 Interview Rounds:")
    print(run_query("""
        SELECT s.name, p.interview_rounds_cleared
        FROM Students s
        JOIN Placements p ON s.student_id = p.student_id
        WHERE p.interview_rounds_cleared > 3
        ORDER BY p.interview_rounds_cleared DESC
    """, conn))


# ---- MAIN ENTRY ----
def main():
    print("Connecting to TiDB Cloud...")
    conn = connect_to_tidb()
    print("Connected!\n")

    show_insights(conn)

    conn.close()
    print("\n Connection closed.")

if __name__ == "__main__":
    main()

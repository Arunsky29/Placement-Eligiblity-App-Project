# Placement-Eligiblity-App-Project

A data-driven Streamlit application to filter, analyze, and visualize student placement readiness using synthetic data and SQL insights.
---

## 🚀 Features

✅ Dynamic filtering of eligible students  
✅ TiDB Cloud integration with MySQL  
✅ Object-Oriented Python codebase  
✅ 10 SQL insights for decision-making  
✅ Fully modular design using Faker, Streamlit, and Pandas

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Faker** – for generating student data  
- **MySQL / TiDB Cloud** – relational database  
- **Streamlit** – UI and dashboard  
- **Pandas** – data manipulation  
- **OOP Principles** – for database interaction  

---

## 📦 Dataset Schema

### 1. `Students`
- `student_id`, `name`, `age`, `gender`, `email`, `phone`, `enrollment_year`, `course_batch`, `city`, `graduation_year`

### 2. `Programming`
- `programming_id`, `student_id`, `language`, `problems_solved`, `assessments_completed`, `mini_projects`, `certifications_earned`, `latest_project_score`

### 3. `SoftSkills`
- `soft_skill_id`, `student_id`, `communication`, `teamwork`, `presentation`, `leadership`, `critical_thinking`, `interpersonal_skills`

### 4. `Placements`
- `placement_id`, `student_id`, `mock_interview_score`, `internships_completed`, `placement_status`, `company_name`, `placement_package`, `interview_rounds_cleared`, `placement_date`

---

## 📊 SQL Insights (10 Total)

1. Top 5 students by project score  
2. Average soft skills by batch  
3. Placement status count  
4. Avg & max package by company  
5. Gender count per batch  
6. Avg problems solved per language  
7. Most common student city  
8. Students with 0 internships  
9. Batch with highest avg mock score  
10. Students who cleared > 3 interview rounds

---

## 🧪 How to Run

### ▶️ 1. Run SQL Insight Script (Optional)

```bash
python placement_insights.py

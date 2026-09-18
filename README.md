🎓 Student Performance Prediction System

A Machine Learning and Streamlit-based application that predicts a student's exam score using academic, behavioral, and environmental factors.

📌 Project Overview

The Student Performance Prediction System uses Machine Learning to analyze factors that can influence student exam performance and predict the expected exam score.

The project also provides an interactive Streamlit dashboard for data analysis and model performance evaluation.

🚀 Features

- Student exam score prediction
- Interactive Streamlit dashboard
- Hours Studied vs Exam Score analysis
- Attendance vs Exam Score analysis
- Previous Scores vs Exam Score analysis
- Motivation Level analysis
- Parental Involvement analysis
- Access to Resources analysis
- Machine Learning model evaluation
- MAE, RMSE and R² metrics
- Sidebar navigation

🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn
- Joblib
- Jupyter Notebook
- Git & GitHub

🤖 Machine Learning

The project uses a Linear Regression model to predict the student's exam score.

Model Performance

Metric| Score
MAE| 0.45
RMSE| 1.80
R² Score| 0.788

The R² score indicates that the model explains approximately 78.8% of the variation in the exam scores on the evaluation data.

📂 Project Structure

student-performance-prediction/
│
├── data/
│   └── Student_Performance_Factors.csv.csv
│
├── notebooks/
│   └── 01_data_analysis.ipynb
│
├── src/
│   ├── main.py
│   ├── visualization.py
│   ├── feature_columns.pkl
│   └── student_performance_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore

▶️ How to Run

1. Clone the repository

git clone https://github.com/praveen-S90/student-performance-prediction.git

2. Open the project

cd student-performance-prediction

3. Install dependencies

pip install -r requirements.txt

4. Run the Streamlit application

streamlit run src/main.py

The application will open in your browser.

📊 Dashboard

The application contains four main sections:

- 🏠 Home
- 🎯 Prediction
- 📊 Analysis
- 🤖 Model Performance

🎯 Project Objective

The main objective of this project is to demonstrate how Machine Learning can be used to analyze student-related factors and predict academic performance through an interactive dashboard.

🔮 Future Improvements

- Try Random Forest and other advanced regression models
- Improve prediction accuracy
- Add more interactive visualizations
- Deploy the Streamlit application online
- Add downloadable prediction reports
- Add model comparison charts

👨‍💻 Author

Praveen Hunashyal

GitHub: "praveen-S90" (https://github.com/praveen-S90)

## Recent Project Modifications

The project was enhanced with the following features:

### 1. SQLite Database Integration
- Added SQLite database to store prediction results.
- Database file: `data/student_predictions.db`
- Database logic is implemented in `src/database.py`.

### 2. Prediction History
- Every exam-score prediction is automatically saved to the database.
- The Streamlit dashboard displays previous predictions in a table.

### 3. Delete Prediction History
- Added an option to delete stored prediction records.
- Users can clear the prediction history directly from the dashboard.

### 4. Custom CSS Styling
- Added `static/style.css`.
- Custom CSS is used to improve the appearance of the Streamlit dashboard.

### 5. GitHub Version Control
- Project is maintained using Git and GitHub.
- `.gitignore` is configured to keep the local SQLite database out of the repository.

## Current Project Architecture

Student Input
↓
Streamlit Dashboard
↓
Machine Learning Model
↓
Predicted Exam Score
↓
SQLite Database
↓
Prediction History

## Project Structure

```text
datascience_project/
├── data/
│   ├── Student_Performance_Factors.csv.csv
│   └── student_predictions.db
├── notebooks/
│   └── 01_data_analysis.ipynb
├── src/
│   ├── database.py
│   ├── main.py
│   ├── visualization.py
│   ├── feature_columns.pkl
│   └── student_performance_model.pkl
├── static/
│   └── style.css
├── .gitignore
├── README.md
└── requirement.txt
**Important:** Since `student_predictions.db` is ignored by Git, it exists on your computer but won't be uploaded to GitHub. You can mention it in the README as a **local database file**.

If you want, I can also give you a **complete final README.md** combining your original README + all these modifications, ready to replace the current file.
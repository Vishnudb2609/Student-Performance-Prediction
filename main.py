import streamlit as st
import pandas as pd
import joblib
import os
# your other imports...
# Load custom CSS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(BASE_DIR, "static", "style.css")

with open(CSS_PATH, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

from database import create_table, save_prediction, get_predictions,delete_predictions

create_table()


st.sidebar.title("📊 Student Performance")
st.sidebar.write("Student Exam Score Prediction")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🎯 Prediction", "📊 Analysis", "🤖 Model Performance"]
)
if page == "🏠 Home":
    st.subheader("🏠 Welcome")
    
    st.write(
        "This project predicts student exam scores using "
        "Machine Learning and analyzes the factors affecting performance."
    )
    
    st.info("Use the sidebar to explore Prediction, Analysis, and Model Performance.")



# -----------------------------
# Load model and feature columns
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "Student_Performance_Factors.csv.csv"
)
df_dashbord=pd.read_csv(DATA_PATH)

model = joblib.load(
    os.path.join(BASE_DIR, "student_performance_model.pkl")
)

feature_columns = joblib.load(
    os.path.join(BASE_DIR, "feature_columns.pkl")
)





# -----------------------------
# Page title
# -----------------------------

st.title("🎓 Student Performance Prediction System")

st.write(
    "This dashboard uses Machine Learning to predict a student's "
    "exam score based on academic, behavioral, and environmental factors."
)

st.markdown("---")

st.write(
    "Enter the student's details below to predict the expected exam score."
)

# -----------------------------
# Student inputs
# -----------------------------
student_name = st.text_input("👤 Student Name")

hours_studied = st.number_input(
    "Hours Studied", 0, 24, 5
)

attendance = st.number_input(
    "Attendance (%)", 0, 100, 80
)

previous_scores = st.number_input(
    "Previous Scores", 0, 100, 70
)

sleep_hours = st.number_input(
    "Sleep Hours", 0, 24, 7
)

tutoring_sessions = st.number_input(
    "Tutoring Sessions", 0, 20, 2
)

# Categorical inputs

parental_involvement = st.selectbox(
    "Parental Involvement",
    ["Low", "Medium", "High"]
)

access_to_resources = st.selectbox(
    "Access to Resources",
    ["Low", "Medium", "High"]
)

motivation_level = st.selectbox(
    "Motivation Level",
    ["Low", "Medium", "High"]
)

# -----------------------------
# Prediction
# -----------------------------
if page == "🎯 Prediction":
    st.subheader("🎯 Student Exam Score Prediction")
if st.button("Predict Exam Score"):


    # Create input dataframe
    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Previous_Scores": [previous_scores],
        "Sleep_Hours": [sleep_hours],
        "Tutoring_Sessions": [tutoring_sessions],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Motivation_Level": [motivation_level]
    })

    # Convert categorical columns using the same method
    input_data = pd.get_dummies(input_data)

    # Make sure input has exactly the same columns as training data
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Prediction
    prediction = model.predict(input_data)[0]

    st.success(
        f"🎯 Predicted Exam Score: {prediction:.2f}"
    
    )
    save_prediction(
    student_name,
    hours_studied,
    attendance,
    previous_scores,
    prediction
)

    if prediction >= 80:
        st.success("🌟 Excellent predicted performance!")

    elif prediction >= 60:
        st.info("👍 Good predicted performance.")

    elif prediction >= 40:
        st.warning("📚 Average predicted performance.")

    else:
        st.error("⚠️ Low predicted performance.")
        st.markdown("---")
        # -----------------------------
# Prediction History
# -----------------------------
if page == "🎯 Prediction":
    if st.button("🗑️ Delete Prediction History"):
      delete_predictions()
      st.success("Prediction history deleted successfully!")
      st.rerun()

    predictions = get_predictions()

    if predictions:
        history_df = pd.DataFrame(
            predictions,
            columns=[
                "ID",
                "student name",
                "Hours Studied",
                "Attendance",
                "Previous Scores",
                "Predicted Score"
            ]
        )

        st.dataframe(history_df, width="stretch")
    else:
        st.info("No prediction history available.")

if page == "🤖 Model Performance":
    st.subheader("🤖 Model Performance")

    st.write("Linear Regression Model")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("MAE", "0.45")

    with col2:
        st.metric("RMSE", "1.80")

    with col3:
        st.metric("R² Score", "0.788")

    st.info(
        "The model explains approximately 78.8% "
        "of the variation in student exam scores."
    )
if page == "📊 Analysis":
    st.subheader("📊 Student Performance Analysis")
    st.write(
        "Explore the relationship between different student factors "
        "and exam scores."
    )

st.markdown("---")
if page=="analysis":
 st.subheader("📈 Hours Studied vs Exam Score")

 st.scatter_chart(
    df_dashbord,
    x="Hours_Studied",
    y="Exam_Score"
)
st.markdown("---")

st.subheader("📈 Attendance vs Exam Score")

st.scatter_chart(
    df_dashbord,
    x="Attendance",
    y="Exam_Score"
)
st.markdown("---")

st.subheader("📈 Previous Scores vs Exam Score")

st.scatter_chart(
    df_dashbord,
    x="Previous_Scores",
    y="Exam_Score"
)
st.markdown("---")

st.subheader("📊 Motivation Level vs Exam Score")

st.bar_chart(
     df_dashbord.groupby("Motivation_Level")["Exam_Score"].mean()
)
st.markdown("---")

st.subheader("📊 Parental Involvement vs Exam Score")

st.bar_chart(
    df_dashbord.groupby("Parental_Involvement")["Exam_Score"].mean()
)
st.markdown("---")

st.subheader("📊 Access to Resources vs Exam Score")

st.bar_chart(
    df_dashbord.groupby("Access_to_Resources")["Exam_Score"].mean()
)
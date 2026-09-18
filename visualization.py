import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load student data
data = pd.read_csv("data/students.csv")
# Create Result column
data["Result"] = data["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Create Grade column
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

data["Grade"] = data["Marks"].apply(get_grade)

# ===== BAR CHART =====

plt.figure(figsize=(8, 5))

sns.barplot(x="Name", y="Marks", data=data)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()
# ===== AGE VS MARKS =====

plt.figure(figsize=(8, 5))

sns.scatterplot(x="Age", y="Marks", data=data, s=100)

plt.title("Age vs Marks")
plt.xlabel("Age")
plt.ylabel("Marks")

plt.show()
# ===== MARKS DISTRIBUTION =====

plt.figure(figsize=(8, 5))

sns.histplot(data["Marks"], bins=5, kde=True)

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()

# ===== RESULT DISTRIBUTION =====

plt.figure(figsize=(6, 5))

result_counts = data["Result"].value_counts()

plt.bar(result_counts.index, result_counts.values)

plt.title("Student Result Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")

plt.show()
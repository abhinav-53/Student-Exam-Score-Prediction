🎓 Student Exam Score Predictor
This project is a machine learning web application built using Python and Streamlit that predicts a student's final exam score (G3) based on key academic and behavioral features such as:

Study time

Absences

First period grade (G1)

Second period grade (G2)

📂 Dataset
The project uses two datasets from the UCI Student Performance Data Set:

student-mat.csv: Data related to Mathematics performance

student-por.csv: Data related to Portuguese performance


🧠 Model
Algorithm: Random Forest Regressor

Training Features: studytime, absences, G1, G2

Target Variable: G3 (Final exam grade)

Model Evaluation:

R² Score (Accuracy)

Root Mean Squared Error (RMSE)

Mean Absolute Error (MAE)

🧾 Web Application
The app provides:

User Input: Via sidebar sliders for entering student-specific data

Predicted G3 Score: Based on trained model

Real-Time Insights: How the input values compare with dataset averages and impact score prediction

Feature Importance Chart: Visual representation of which factors influenced the prediction

🔧 Technologies Used
Python

Streamlit

Scikit-learn

Pandas

Seaborn & Matplotlib

R (for data merging)


📌 Educational Use

This tool helps educators and students understand how study habits, attendance, and prior performance affect final exam scores. It can be used to detect at-risk students early and plan targeted interventions.




 📋 Instructions to Run the Application

 ✅ Step 1: Install Required Python Packages

```bash
pip install flask flask-cors scikit-learn numpy streamlit
```

✅ Step 2: Start the Backend Server

```bash
python app.py
```

 ✅ Step 3: Train or Load the Machine Learning Model

```bash
python model.py
```

 ✅ Step 4: Launch the Streamlit Frontend

```bash
streamlit run app.py
```


<img width="457" alt="image" src="https://github.com/user-attachments/assets/4fdabcad-42aa-443b-b50a-7f54058328a9" />
<img width="460" alt="image" src="https://github.com/user-attachments/assets/3e8e14e1-b07f-4723-a784-af4d0e10b5f0" />
<img width="414" alt="image" src="https://github.com/user-attachments/assets/8a4163f9-50d3-4c2c-b8f1-976fbfe76a69" />
<img width="414" alt="image" src="https://github.com/user-attachments/assets/6c408742-4f63-46ef-a37f-0b00fbe0ed33" />



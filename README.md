
# 🎓 Student Exam Score Predictor

This project is a machine learning web application built using Python and Streamlit that predicts a student's final exam score (G3) based on key academic and behavioral features.

---

## 📋 Instructions to Run the Application

### ✅ Step 1: Install Required Python Packages

```bash
pip install flask flask-cors scikit-learn numpy streamlit
```

### ✅ Step 2: Start the Backend Server

```bash
python app.py
```

### ✅ Step 3: Train or Load the Machine Learning Model

```bash
python model.py
```

### ✅ Step 4: Launch the Streamlit Frontend

```bash
streamlit run app.py
```
<img width="457" alt="image" src="https://github.com/user-attachments/assets/63790e2f-1961-4bf3-82d1-d5cc02bb45ab" />
<img width="460" alt="image" src="https://github.com/user-attachments/assets/b36f326d-36e9-4115-874c-cf24b4b5fe04" />
<img width="414" alt="image" src="https://github.com/user-attachments/assets/fbf9c952-6085-4542-9d40-5d2d17b32048" />
<img width="414" alt="image" src="https://github.com/user-attachments/assets/a90ccd39-d6ac-4e66-a3b5-8a4d178c3514" />


---

## 📂 Dataset

The project uses two datasets from the UCI Student Performance Data Set:

- `student-mat.csv`: Data related to Mathematics performance  
- `student-por.csv`: Data related to Portuguese performance

---

## 🧠 Model

- **Algorithm**: Random Forest Regressor  
- **Training Features**: `studytime`, `absences`, `G1`, `G2`  
- **Target Variable**: `G3` (Final exam grade)

### Model Evaluation Metrics:
- **R² Score (Accuracy)**: 0.8402  
- **Root Mean Squared Error (RMSE)**: 1.8102  
- **Mean Absolute Error (MAE)**: 1.1234  

---

## 🖥️ Web Application Features

- **User Input**: Via sidebar sliders for entering student-specific data  
- **Predicted G3 Score**: Based on trained model  
- **Real-Time Insights**: Compare entered values with dataset averages  
- **Feature Importance Chart**: Shows which features influenced the prediction

---

## 🧰 Tech Stack 

- Python
- R (for data merging)
- Streamlit  
- Scikit-learn  
- Pandas  
- Seaborn & Matplotlib  


---


## 📌 Educational Use

This tool helps educators and students understand how study habits, attendance, and prior performance affect final exam scores. It can be used to detect at-risk students early and plan targeted interventions.



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

---

## 📂 Dataset

The project uses two datasets from the UCI Student Performance Data Set:

- `student-mat.csv`: Data related to Mathematics performance  
- `student-por.csv`: Data related to Portuguese performance

These datasets were merged using shared student identifiers with R:

```r
d3 = merge(d1, d2, by = c("school", "sex", "age", "address", "famsize", 
                          "Pstatus", "Medu", "Fedu", "Mjob", "Fjob", 
                          "reason", "nursery", "internet"))
```

This resulted in a refined dataset of 382 unique students with combined records.

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

## 🧰 Technologies Used

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- Seaborn & Matplotlib  
- R (for data merging)

---

## 🚀 Getting Started

To run the app locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Educational Use

This tool helps educators and students understand how study habits, attendance, and prior performance affect final exam scores. It can be used to detect at-risk students early and plan targeted interventions.


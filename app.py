import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Set Streamlit page config
st.set_page_config(page_title="Student Exam Score Predictor", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>🎓 Student Exam Score Predictor</h1>", unsafe_allow_html=True)

# Load the trained regression model
with open("regressor.pkl", "rb") as f:
    model = pickle.load(f)

# Sidebar: Input features
st.sidebar.header("📊 Enter Student Details")
def get_input():
    studytime = st.sidebar.slider("Study Time (1 = low, 4 = high)", 1, 4, 2)
    absences = st.sidebar.slider("Absences", 0, 50, 5)
    G1 = st.sidebar.slider("First Exam Score (G1)", 0, 20, 10)
    G2 = st.sidebar.slider("Second Exam Score (G2)", 0, 20, 10)
    return pd.DataFrame([{
        "studytime": studytime,
        "absences": absences,
        "G1": G1,
        "G2": G2
    }])

input_df = get_input()

# Main prediction section
st.subheader("📈 Predicted Final Exam Score")

if st.button("🧾 Predict"):
    predicted_score = model.predict(input_df)[0]
    st.success(f"📘 Estimated Final Exam Score (G3): **{predicted_score:1f}**")

    # Educational insight
     # Educational insight (real-time based on input and model)

    # Average values for comparison (from training data)
    train_df = pd.read_csv("train_features.csv")
    mean_values = train_df[input_df.columns].mean()

    st.markdown("#### 📌 Impact Analysis:")

    insight_lines = []
    for col in input_df.columns:
        val = input_df[col].values[0]
        mean_val = mean_values[col]
        if val > mean_val:
            impact = "🔼 likely increased"
        elif val < mean_val:
            impact = "🔽 likely decreased"
        else:
            impact = "➖ neutral"
        
        insight_lines.append(f"- **{col}** = {val} (avg: {mean_val:.2f}) → {impact} the predicted score")

    st.markdown("\n".join(insight_lines))

    st.markdown("""
    ---
    These comparisons are made against average student data and provide a real-time interpretation of how each entered value may have influenced the predicted final score (G3). 
    """)


    try:
        importances = model.feature_importances_
        feature_names = input_df.columns
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values(by='Importance', ascending=False)

        # Plot using seaborn
        plt.figure(figsize=(8, 4))
        sns.barplot(data=importance_df, x='Importance', y='Feature', palette='viridis')
        plt.title("Real-Time Feature Importance")
        st.pyplot(plt.gcf())
        plt.clf()

    except AttributeError:
        st.warning("⚠️ The model doesn't support feature_importances_. It might not be a tree-based model.")

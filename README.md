# 💳 FraudShield

**FraudShield** is a machine learning–powered system that detects **credit card fraud** using transaction data. It applies anomaly detection techniques to identify suspicious patterns in real-time, helping financial institutions reduce risk and protect customers from fraud.

This project leverages statistical analysis, ML classification models, and data visualization to interpret transaction behaviors and predict fraudulent activities.

---

## 📌 Features

- 🕵️‍♀️ **Fraud Detection Using ML**: Detects abnormal credit card transactions using machine learning models like Logistic Regression, Random Forest, XGBoost, etc.
- 📊 **Highly Imbalanced Data Handling**: Employs techniques like **OverSampling**, **undersampling**, and **cost-sensitive learning** to improve accuracy on rare fraud cases.
- 🧮 **Explainable AI**: Uses SHAP or feature importance plots to explain model decisions for transparency and trust.
- 📉 **ROC-AUC Optimized**: Evaluates model using precision-recall curves, F1-score, and AUC-ROC metrics to account for data imbalance.
- 💾 **Clean Preprocessing Pipeline**: Includes missing value handling, scaling, and feature engineering.
- 🧪 **Model Comparison Dashboard**: Visual comparison of accuracy, recall, and false positive rate across different classifiers.
- 🌐 **Web Deployment Ready**: Compatible with Flask/Streamlit for deploying fraud prediction as a web tool or API.

---

## 🧰 Tech Stack

- **Python**, **NumPy**, **Pandas** – for data manipulation and preprocessing  
- **Scikit-learn**, **XGBoost** – for model building and evaluation  
- **Matplotlib**, **Seaborn** – for visualizations  
- **Streamlit/Flask** *(optional)* – for model deployment  

---

## 🧪 Example Use Case

1. Input: Transaction data with features such as amount, time, and anonymized variables (V1–V28)  
2. Output:  
   - `0` → Legitimate Transaction  
   - `1` → Fraudulent Transaction  
   - Probability Score and Explanation (optional)

---

## 📸 Screenshot 
![WhatsApp Image 2025-05-25 at 13 04 55_7cf071b4](https://github.com/user-attachments/assets/b66c6bf9-6ef9-4a3a-9f9c-577d5acf2258)


---

## 🔒 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Neha Shetty**  
Final Year Student | Information Science and Engineering | CIT  
🔗 [GitHub](https://github.com/nehagithubrit) • [LinkedIn](www.linkedin.com/in/nehashetty225)

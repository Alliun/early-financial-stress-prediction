# Early Financial Stress Prediction System

## 📌 Project Overview
The **Early Financial Stress Prediction System** is a machine learning–based application designed to identify early signs of financial distress in customers **before loan delinquency occurs**.  
Unlike traditional banking systems that react only after missed payments, this system enables **proactive risk detection**, helping financial institutions reduce losses and maintain customer trust.

---

## 🎯 Problem Statement
Banks face increasing delinquency risk due to economic uncertainty, yet most existing systems intervene only after a customer has already missed a payment. Such reactive approaches result in higher recovery costs, reduced recovery rates, and damaged customer relationships.  
This project aims to address this gap by predicting early financial stress using historical financial data and machine learning techniques.

---

## 🧠 Solution Approach
The system analyzes customer-level financial data such as:
- Monthly income
- Monthly expenses
- EMI obligations
- Savings balance  

Using supervised machine learning classification models, customers are categorized into:
- **Low Stress**
- **Medium Stress**
- **High Stress**

This enables early warning and preventive intervention.

---

## 🛠️ Technology Stack
- **Programming Language:** Python  
- **Database:** MySQL  
- **Libraries:**  
  - pandas  
  - numpy  
  - matplotlib / seaborn  
  - scikit-learn  
- **Tools:**  
  - Jupyter Notebook / VS Code  

---

## 🗄️ Database Design (Initial Phase)

### Tables Used:
1. **customers** – Stores basic customer details  
2. **monthly_financials** – Stores monthly income, expenses, EMI, and savings  
3. **stress_labels** – Stores financial stress levels for model training  

The database is designed to be minimal and scalable for future extensions.

---

## 🤖 Machine Learning Techniques
The following supervised learning algorithms are used:
- Logistic Regression (baseline model)
- Decision Tree Classifier
- Random Forest Classifier  
- (Optional) Gradient Boosting / XGBoost

These models are trained to classify financial stress levels based on engineered financial features.

---

## 🔁 Feedback and Retraining Mechanism
- New monthly data is continuously collected
- Model predictions are compared with actual outcomes
- Prediction errors are logged
- The model is periodically retrained using updated data to improve accuracy and adaptability

---

## 📊 Prediction Scope
- **Individual-Level Predictions:** Financial stress level for each customer
- **Aggregated Insights:** Stress trends across customer segments such as income group, employment type, or region

---

## 📁 Project Structure

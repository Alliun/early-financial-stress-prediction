'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV files
customers = pd.read_csv('D:\Rup\Codes\PROJECTS\early-financial-stress-prediction\data\customers.csv')
monthly = pd.read_csv('D:\Rup\Codes\PROJECTS\early-financial-stress-prediction\data\monthly_financials.csv')
labels = pd.read_csv('D:\Rup\Codes\PROJECTS\early-financial-stress-prediction\data\stress_labels.csv')

# Print data to confirm loading
print("Customers:")
print(customers)
print("\nMonthly Financials:")
print(monthly)
print("\nStress Labels:")
print(labels)

# Merge monthly data with stress labels
data = pd.merge(
    monthly,
    labels,
    on=['customer_id', 'month'],
    how='inner'
)

print("\nMerged Dataset (ML Ready):")
print(data)

# Feature engineering: financial ratios
data['emi_to_income'] = data['emi_amount'] / data['monthly_income']
data['expense_to_income'] = data['monthly_expense'] / data['monthly_income']
data['savings_to_income'] = data['savings_balance'] / data['monthly_income']

print("\nDataset with Financial Ratios:")
print(data[['customer_id', 'month',
            'emi_to_income',
            'expense_to_income',
            'savings_to_income',
            'stress_level']])

# Convert stress labels to numbers
mapping = {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2}
data['stress_num'] = data['stress_level'].map(mapping)

print("\nConverted Labels:")
print(data[['stress_level', 'stress_num']])

# Traing the model with Decision tree classifier
features = data[['emi_to_income', 'expense_to_income', 'savings_to_income']]
target = data['stress_num']
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier()
model.fit(features, target)

print("\nModel trained successfully!")

# Test prediction on new sample
sample = [[0.45, 0.88, 0.40]]  
# format = [emi_ratio, expense_ratio, savings_ratio]

prediction = model.predict(sample)

# convert back to text label
reverse_map = {0:'LOW', 1:'MEDIUM', 2:'HIGH'}

print("\nPrediction result (numeric):", prediction[0])
print("Predicted Stress Level:", reverse_map[prediction[0]])'''

import pandas as pd

data = pd.read_csv(r"data/aggregated_financials.csv")

# Create behavioral ratios
data["emi_ratio"] = data["total_emi"] / data["total_income"]
data["expense_ratio"] = data["total_expense"] / data["total_income"]
data["net_savings_ratio"] = (
    (data["total_income"] - data["total_expense"]) / data["total_income"]
)

print(data)
def compute_stress(node_index):
    neighbors = G[node_index]
    weighted_score = 0
    total_weight = 0

    for neighbor in neighbors:
        weight = G[node_index][neighbor]["weight"]
        stress_score = (
            features[neighbor][0] * 0.5 +   # emi ratio weight
            features[neighbor][1] * 0.3 -   # expense ratio weight
            features[neighbor][2] * 0.2     # savings ratio reduces stress
        )
        weighted_score += weight * stress_score
        total_weight += weight

    final_score = weighted_score / total_weight

    if final_score > 0.6:
        return "HIGH"
    elif final_score > 0.3:
        return "MEDIUM"
    else:
        return "LOW"







import pandas as pd
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

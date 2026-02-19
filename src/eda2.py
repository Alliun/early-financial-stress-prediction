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

import networkx as nx
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

# Create feature matrix
features = data[["emi_ratio", "expense_ratio", "net_savings_ratio"]].values

# Create graph
G = nx.Graph()

# Add nodes
for i in range(len(features)):
    G.add_node(i)

# Compute similarity matrix
dist_matrix = euclidean_distances(features)

# Add weighted edges
for i in range(len(features)):
    for j in range(i + 1, len(features)):
        weight = 1 / (1 + dist_matrix[i][j])
        G.add_edge(i, j, weight=weight)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the data into a pandas DataFrame
data = pd.read_csv("customer_data.csv")

# Explore the data using visualizations
sns.pairplot(data, diag_kind="hist")
plt.show()

# Scale the data to prepare it for clustering
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Fit the KMeans algorithm to the data
kmeans = KMeans(n_clusters=3)
kmeans.fit(data_scaled)

# Assign the cluster labels to each customer
data["cluster_labels"] = kmeans.labels_

# Plot the results
sns.scatterplot(x="Age", y="Spending Score (1-100)", hue="cluster_labels", data=data)
plt.show()

# Analyze the characteristics of each cluster
cluster_data = data.groupby(["cluster_labels"]).mean()
print(cluster_data)

# CUSTOMER SEGMENTATION 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Load dataset
df = pd.read_csv("Mall Customers.csv")

# 2. Clean column names
df.columns = df.columns.str.strip()

print("Columns:", df.columns)
print("\nFirst 5 rows:")
print(df.head())

# 3. Handle missing values
df = df.dropna()

# 4. Encode categorical columns
le = LabelEncoder()

for col in ['Gender', 'Education', 'Marital Status']:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# 5. Select features
features = ['Gender', 'Age', 'Education', 'Marital Status',
            'Annual Income (k$)', 'Spending Score (1-100)']

X = df[features]

# 6. Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 7. Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Save elbow graph
plt.figure()
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Clusters")
plt.ylabel("WCSS")
plt.savefig("elbow.png")
plt.close()

# 8. Apply KMeans
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 9. Print clustered data
print("\nClustered Data:")
print(df.head())

# 10. Visualization (save instead of show)
plt.figure()
plt.scatter(df['Annual Income (k$)'],
            df['Spending Score (1-100)'],
            c=df['Cluster'])

plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segments")
plt.savefig("clusters.png")
plt.close()

# 11. Save output file
df.to_csv("output.csv", index=False)

print("\nDone!")
print(" Files created:")
print(" - output.csv (final data)")
print(" - elbow.png (elbow graph)")
print(" - clusters.png (segmentation graph)")
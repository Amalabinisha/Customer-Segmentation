# Customer Segmentation using K-Means Clustering

## Project Overview
This project performs customer segmentation using the Mall Customer Dataset.  
The main objective is to group customers based on their behavior and spending patterns using the K-Means Clustering algorithm.

---

## Objective
- Perform data preprocessing
- Encode categorical features
- Apply K-Means clustering
- Visualize customer segments
- Generate business insights

---

## Dataset
Dataset Name: Mall Customers Dataset

### Columns Used
- CustomerID
- Gender
- Age
- Education
- Marital Status
- Annual Income (k$)
- Spending Score (1-100)

---

## Technologies Used
- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Steps Performed

### 1. Data Loading
The dataset is loaded using Pandas.

### 2. Data Cleaning
- Removed extra spaces from column names
- Removed missing values

### 3. Encoding Categorical Data
Categorical columns:
- Gender
- Education
- Marital Status

These columns were converted into numerical format using LabelEncoder.

### 4. Feature Selection
Selected features:
- Gender
- Age
- Education
- Marital Status
- Annual Income (k$)
- Spending Score (1-100)

### 5. Feature Scaling
StandardScaler was used to normalize the dataset.

### 6. Elbow Method
The Elbow Method was used to determine the optimal number of clusters.

### 7. K-Means Clustering
K-Means algorithm was applied with:
- Number of clusters = 5

### 8. Visualization
Customer clusters were visualized using:
- Annual Income
- Spending Score

---

## Output Files
The following files are generated:

- output.csv → Final clustered dataset
- elbow.png → Elbow method graph
- clusters.png → Customer segmentation graph

---

## Business Insights
- Customers are grouped based on spending behavior.
- High-income customers with high spending can be targeted for premium products.
- Low-spending customers may require promotional offers.
- Segmentation helps businesses improve marketing strategies.

---

## Conclusion
Customer segmentation helps businesses understand customer behavior and improve decision-making.  
K-Means clustering successfully grouped customers into meaningful segments based on income and spending score.

---


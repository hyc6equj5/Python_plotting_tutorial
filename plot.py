import pandas as pd
import matplotlib.pyplot as plt

# Load CSV Data
file_path = "scientific_data.csv"  # Replace with your actual CSV file
df = pd.read_csv(file_path)

# Display first few rows of the dataset
print(df.head())

# Drop rows with missing values (if necessary)
# df = df.dropna()

# Define columns to plot
x_column = "Time"   # Replace with your actual column name
y_column = "Value"  # Replace with your actual column name

# Line Plot
plt.figure(figsize=(8, 5))
plt.plot(df[x_column], df[y_column], marker="o", linestyle="-", color="b", label="Measurement")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title("Scientific Data Line Plot")
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 5))
plt.scatter(df[x_column], df[y_column], color="r", label="Observations")
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.title("Scientific Data Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()

# Histogram
plt.figure(figsize=(8, 5))
plt.hist(df[y_column], bins=20, color="g", alpha=0.7, label="Frequency")
plt.xlabel(y_column)
plt.ylabel("Count")
plt.title("Distribution of Values")
plt.legend()
plt.grid(True)
plt.show()

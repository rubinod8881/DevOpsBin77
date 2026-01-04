import pandas as pd
import matplotlib.pyplot as plt

# Data for our financial practice
data = {
    "Name": ["Binod Prasad", "Rubi Prasad", "Aayushman Prasad"],
    "Age": [44, 37, 16],
    "Savings": [5000, 7500, 1200]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Show the data
print("--- Financial Data Table ---")
print(df)

# Quick calculation: Average Age
print(f"\nAverage Age: {df['Age'].mean():.1f}")
df.plot(x="Name",y="Savings",kind="bar",title="Employee Salary")
plt.show()

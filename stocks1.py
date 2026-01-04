import matplotlib.pyplot as plt

# Sample Financial Data: Monthly Savings
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
savings = [1200, 1500, 1300, 1800, 2100]

plt.figure(figsize=(8, 5))
plt.plot(months, savings, marker='o', color='green', linestyle='--')

# Adding Financial Labels
plt.title('Monthly Savings Growth')
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.grid(True)

# Show the plot
plt.show()
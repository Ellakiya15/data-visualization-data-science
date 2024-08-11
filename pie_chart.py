import matplotlib.pyplot as plt

# Sample data
sizes = [10, 20, 30, 40]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'lightskyblue', 'lightcoral', 'lightgreen']
explode = (0.1, 0, 0, 0)  # explode the 1st slice

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', shadow=False, startangle=140)

# Add title
plt.title('Sample Pie Chart')

# Show the plot
plt.show()

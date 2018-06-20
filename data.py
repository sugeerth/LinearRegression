import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)

# Reading Data
data = pd.read_csv('head.csv')
print(data.shape)
print data.head()
print data.info()

x = data["Head Size(cm^3)"]
y = data["Brain Weight(grams)"]

mean_x = np.mean(x)
mean_y = np.mean(y)

m = len(x)

# Using the formula to calculate b1 and b2
numerator = 0
denominator = 0

for i in range(m):
	numerator += (x[i] - mean_x) * (y[i] - mean_y)
	denominator += (x[i] - mean_x) ** 2
	b1 = numerator / denominator
	b0 = mean_y - (b1 * mean_x)

# Print coefficients
print(b1, b0)


max_x = np.max(x) + 100
min_x = np.min(x) - 100

# Calculating line values x and y
x1 = np.linspace(min_x, max_x, 1000)
y1 = b0 + b1 * x1

# Ploting Line
plt.plot(x1, y1, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(x, y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

matrix = np.random.uniform(-3, 15, size=(7, 3))

avg_each = [round(sum([x[i] for x in np.array(matrix)]) / len(DAYS), 2) for i in range(3)]
maxim = [round(max(x[0], x[1], x[2]), 2) for x in np.array(matrix)]
minimum = [round(min([x[i] for x in np.array(matrix)]), 2) for i in range(3)]
minimum_day = [[DAYS[j] for j in range(7) if minimum[i] == round(float(matrix[j][i]), 2)] for i in range(3)]
avg_between = [round((sum(x) / 3), 2) for x in matrix]

print(avg_each)
print(maxim)
print(minimum)
print(minimum_day)
print(avg_between)

plt.plot(DAYS, avg_between)

plt.xlabel('Days')
plt.ylabel('in Celsius')
plt.title('Average Temperature Of Cities')

plt.show()

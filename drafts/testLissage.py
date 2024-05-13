import matplotlib.pyplot as plt

def smooth(values, w_size=5):
    new_values = []
    for i in range(len(values)):
        window = values[max(0, i - (w_size - 1) // 2):min(i + w_size // 2 + 1, len(values))]
        new_values.append(sum(window) / len(window))
    return new_values

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 5, 8, 4, 2, 5, 7, 9, 6, 3]

# Smooth the data
smoothed_y = smooth(y)

print(smoothed_y)

# Plot the original and smoothed data
plt.plot(x, y, label='Original')
plt.plot(x, smoothed_y, label='Smoothed')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Smoothing Example')
plt.legend()
plt.grid(True)
plt.show()
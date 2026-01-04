import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 100)
y = x ** 2

noise_levels = [0.1, 0.5, 1.0]
absolute_noise_levels = [50, 200]

plt.figure()

plt.scatter(x, y, label='y=x^2', alpha=0.7)

for sigma in noise_levels:
    epsilon = np.random.normal(0, sigma, size=len(x))
    y_noise = y + y * epsilon
    plt.scatter(x, y_noise, label=f"noise σ={sigma}", alpha=0.6)

for sigma in absolute_noise_levels:
    epsilon = np.random.normal(0, sigma, size=len(x))
    y_noise = y + epsilon
    plt.scatter(x, y_noise, label=f"absolute noise σ={sigma}", alpha=1)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Влияние абсолютного и относительного шума на числовую зависимость")
plt.show()
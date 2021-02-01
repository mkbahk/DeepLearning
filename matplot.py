import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6.4, 0.1)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)

print(x)

print(s, "\n\n")
print(c, "\n\n")
print(t)

plt.plot(x, s)
plt.show()

plt.plot(x, c)
plt.show()

plt.plot(x, t)
plt.show()

y1 =  np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle='--', label='cos')
plt.xlabel("x")
plt.ylabel('y')
plt.title("sin & cos")
plt.legend()
plt.show()

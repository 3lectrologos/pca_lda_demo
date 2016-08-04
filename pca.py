import numpy as np
import matplotlib.pylab as plt

m1 = np.asarray([-0.5, 0])
s1 = np.asarray([[0.03, 0], [0, 0.6]])
x1 = np.random.multivariate_normal(m1, s1, 50)
m2 = np.asarray([0.5, 0])
s2 = np.asarray([[0.03, 0], [0, 0.6]])
x2 = np.random.multivariate_normal(m2, s2, 50)

x11 = x1.copy()
x11[:, 0] = 0
x21 = x2.copy()
x21[:, 0] = 0
x12 = x1.copy()
x12[:, 1] = 0
x22 = x2.copy()
x22[:, 1] = 0

ALPHA = 0.6
MSIZE = 8
LWIDTH = 3


def after():
    plt.axis('equal')
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.show()


plt.plot(x1[:, 0], x1[:, 1], 'bo', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'rs', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot(x1[:, 0], x1[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([0, 0], [-5, 5], 'g-', linewidth=LWIDTH)
plt.plot(x1[:, 0], x1[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([0, 0], [-5, 5], 'g-', linewidth=LWIDTH)
plt.plot(x11[:, 0], x11[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
plt.plot(x21[:, 0], x21[:, 1], 'ks', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([-5, 5], [0, 0], 'm-', linewidth=LWIDTH)
plt.plot(x1[:, 0], x1[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([-5, 5], [0, 0], 'm-', linewidth=LWIDTH)
plt.plot(x12[:, 0], x12[:, 1], 'ko', markersize=MSIZE, alpha=ALPHA)
plt.plot(x22[:, 0], x22[:, 1], 'ks', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([0, 0], [-5, 5], 'g-', linewidth=LWIDTH)
plt.plot(x1[:, 0], x1[:, 1], 'bo', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'rs', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([0, 0], [-5, 5], 'g-', linewidth=LWIDTH)
plt.plot(x11[:, 0], x11[:, 1], 'bo', markersize=MSIZE, alpha=ALPHA)
plt.plot(x21[:, 0], x21[:, 1], 'rs', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([-5, 5], [0, 0], 'm-', linewidth=LWIDTH)
plt.plot(x1[:, 0], x1[:, 1], 'bo', markersize=MSIZE, alpha=ALPHA)
plt.plot(x2[:, 0], x2[:, 1], 'rs', markersize=MSIZE, alpha=ALPHA)
after()

plt.plot([-5, 5], [0, 0], 'm-', linewidth=LWIDTH)
plt.plot(x12[:, 0], x12[:, 1], 'bo', markersize=MSIZE, alpha=ALPHA)
plt.plot(x22[:, 0], x22[:, 1], 'rs', markersize=MSIZE, alpha=ALPHA)
after()
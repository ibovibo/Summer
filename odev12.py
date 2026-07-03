import numpy as np

zago = np.random.randint(0, 100, size=100)

mask = zago % 2 == 0

mask2 = zago[zago % 2 == 0]


print(zago[mask])
print(mask2)
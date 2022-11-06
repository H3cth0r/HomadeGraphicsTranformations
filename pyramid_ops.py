
import transformations as tf
import math

x = 3.3
A = tf.Point((-1.812, -6.824 + (math.sqrt(3)/3)*x, 5.247))
B = tf.Point((-1.812 - (x/2), -6.824 - (math.sqrt(3)/6)*x, 5.247))
C = tf.Point((-1.812 + (x/2), -6.824 - (math.sqrt(3)/6)*x, 5.247))
D = tf.Point((-1.812, -6.824, 5.247 - math.sqrt(2/3)*x))
M = tf.Point((-1.812, -6.824, 5.247 - (math.sqrt(3)/6)*x))

A.debugModeOn = True
B.debugModeOn = True
C.debugModeOn = True
D.debugModeOn = True
D.debugModeOn = True
M.debugModeOn = True

print(A.coords)
print(B.coords)
print(C.coords)
print(D.coords)
print(M.coords)

res = [0, 0, 0]
for i in range(3):
	res[i] = A.coords[i] + B.coords[i] + C.coords[i] + D.coords[i]
for i in range(3):
	res[i] /= 4

centroid = tf.Point(tuple(res))
print(centroid.coords)
centroid.debugModeOn = True

pimid = tf.Objeto()
pimid.vertix.append(A)
pimid.vertix.append(B)
pimid.vertix.append(C)
pimid.vertix.append(D)

pimid.centroid = centroid

pimid.faces.append((2, 1, 0))
pimid.faces.append((2, 1, 3))
pimid.faces.append((2, 0, 3))
pimid.faces.append((0, 1, 3))

for i in pimid.vertix:
    i.rotateOnPivotY(pimid.centroid.coords, -15)
    print("=================================")

"""
for j in range(15):
    for i in pimid.vertix:
        i.rotateOnPivotY(pimid.centroid.coords, 1)
        print("=================================")
"""
import transformations as tf

factor = 1.43
A = (2, 1, 3)
B = (4, 3, 1)
C = (3, 2, 4)

Q = tf.Point(A)
print("======")
print("Scale on factor")
Q.scaleOnFactor(factor)
print("======")
Q.translate(B)

res = tf.Point(C)
print("rotate on pivot")
res.rotateOnPivotX(Q.coords, 45)

#p.translate((1, 1, 2))
#p.scale((2, 3, 3))
#p.rotateOnX(90)
#p.rotateOnY(90)
#p.rotateOnZ(90)

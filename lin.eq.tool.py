import numpy
import copy
equations = []

equations_solving = 2
for i in range(0,equations_solving):
    apo = input("Equation coefs ("+str(i+1)+"):").split(" ")
    apo = [float(eval(i)) for i in apo]
    equations.append(apo)

Asec = copy.deepcopy(equations)
del Asec[0][2]
del Asec[1][2]
A = numpy.array(Asec)
B = numpy.array([[equations[0][2]],[equations[1][2]]])
ans = numpy.linalg.solve(A,B)

ptags = ["x","y"]
for i in range(0,len(ans)):
    print(ptags[i]+":",ans[i][0])
    
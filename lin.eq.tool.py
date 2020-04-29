import numpy
import copy
equations = []
for i in range(0,2):
    apo = input("Equation coefs ("+str(i+1)+"):").split(" ")
    apo = [int(i) for i in apo]
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
    
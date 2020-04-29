import numpy
import copy

equations = []

equations_solving = 2
for i in range(0,equations_solving):
    apo = input("Equation coefs ("+str(i+1)+"):").split(" ")
    equations.append(apo)

def equalization_eq(eq):
    for i in range(0,len(eq)):
        for I in range(0,len(eq[i])):
            cs = False
            try:
                eq[i][I] = eval(str(eq[i][I]))
                cs = True
            except:
                if cs == False:
                    s0s = eq[i][I].replace("(x","(1x").replace("(y","(1y")
                    s1s = s0s.replace("(","").replace(")","").split("/")
                    s1s[0] = list(s1s[0])
                    eq[i][I] = s1s

                      
       
    tswaps = []
    for i in range(0,len(eq)):
        for I in range(0,len(eq[i])-1):
            
            if str(type(eq[i][I])) == "<class \'list\'>":
                for j in range(0,len(eq[i][I])):

                    if str(type(eq[i][I][j])) == "<class \'list\'>":

                        if eq[i][I][j][0] == "-":
                            if eq[i][I][j][1] == "x" or eq[i][I][j][1]=="y":
                                eq[i][I][j][0] = "-1"
                            else:
                                eq[i][I][j][0]+=eq[i][I][j][1]
                                del eq[i][I][j][1]

                coe_swap_v = 1
                for _ in range(1,len(eq[i][I])):
                    coe_swap_v*=eq[i][I][1]
                    del eq[i][I][1]
                tswaps.append(float(coe_swap_v))
            else:
                tswaps.append(1)
        tswaps.reverse()

        
        for I in range(0,len(eq[i])-1):
            if str(type(eq[i][I])) == "<class \'list\'>":
               eq[i][I] = eq[i][I][0]
               
               vt = ""
               if eq[i][I].count("x") == 1:
                   vt = "x"
               else:
                   vt = "y"

               if eq[i][I][len(eq[i][I])-1] == vt:
                   eq[i][I].extend("+0")

               idx = 0
               if eq[i][I].count("+") == 1:
                   idx = eq[i][I].index("+")
               else:
                   idx = eq[i][I].index("-")
              
               
               ms = ""
               for _ in range(0,idx):
                   if eq[i][I][0] != vt:
                       ms += eq[i][I][0]
                   del eq[i][I][0]
               eq[i][I].insert(0,float(ms))

               idx=1
               evs=""
               for _ in range(idx,len(eq[i][I])):
                   evs+=eq[i][I][idx]
                   del eq[i][I][idx]
               eq[i][I].insert(1,eval(evs))

        

        for I in range(0,len(eq[i])-1):
            if str(type(eq[i][I])) == "<class \'list\'>":
                for j in range(0,len(eq[i][I])):
                    eq[i][I][j] *= tswaps[I]
            else:
                eq[i][I] *= tswaps[I]

        tval = 1
        for tvv in tswaps:
            tval *= tvv

        eq[i][len(eq[i])-1] *= tval
        for I in range(0,len(eq[i])):
            if str(type(eq[i][I])) == "<class \'list\'>":
                eq[i][len(eq[i])-1]+= -1*eq[i][I][len(eq[i][I])-1]
                del eq[i][I][len(eq[i][I])-1]
                eq[i][I] = eq[i][I][0]
                
        tswaps.clear()

        

equalization_eq(equations)  

Asec = copy.deepcopy(equations)
del Asec[0][2]
del Asec[1][2]
A = numpy.array(Asec)
B = numpy.array([[equations[0][2]],[equations[1][2]]])
ans = numpy.linalg.solve(A,B)

ptags = ["x","y"]
for i in range(0,len(ans)):
    print(ptags[i]+":",ans[i][0])
    
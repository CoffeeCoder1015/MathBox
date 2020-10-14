import cmath

mode = "deg"

init_cord = []
init_cord.append(float(input("x:")))
init_cord.append(float(input("y:")))
cmplx_cord = complex(init_cord[0],init_cord[1])

if mode == "deg":
    rotation = float(input("Rotate degrees:")) * cmath.pi/ 180
elif mode == "rad":
    rotation = float(input("Rotate degrees:"))

rotProc = complex(cmath.cos(rotation).real,cmath.sin(rotation).real)

ans = rotProc*cmplx_cord

print("x:",round(ans.real,8),"y:",round(ans.imag,8))



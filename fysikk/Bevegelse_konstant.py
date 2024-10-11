v=5.0
s=0.0
t=0.0

dt=0.1
t_slutt=3.0

while t < t_slutt:
    s=s+v*dt
    t=t+dt
    print("t=",f"{t:.1f}", "s=", s) 
    print("-----------------")

print("t=", f"{t:.1f}", "s=", s, "v=", v) 
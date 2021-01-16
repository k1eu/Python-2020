x = 10
v = 0
a = -9.81
t = 0
dt = 0.01

while x > 0:
    x += v * dt
    v += a * dt
    t += dt
    print(f't={t:.3f}\tx={x:.6f}\tv={v:.3f}')

if abs(v) > 0.1:
    print('crash')
else:
    print('landed')
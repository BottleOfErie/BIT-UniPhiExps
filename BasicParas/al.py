import numpy

D = 25.231
H = 33.046
d = 14.734
h = 22.140
m=35.58
u_D = 0.013
u_H = 0.016
u_d = 0.021
u_h = 0.016
u_m = 0.03
v = numpy.pi*D*D*H/4-numpy.pi*d*d*h/4
print(f'体积:{v}')
vbqdd = numpy.sqrt((numpy.pi*D*H*u_D/2)**2+(numpy.pi*D*D*u_H/4)**2+(numpy.pi*d*h*u_h)**2+(numpy.pi*d*d*u_d/4)**2)
print(f'体积不确定度:{vbqdd}')
ans = m/v
print(f'密度:{ans}')
bqdd = numpy.sqrt((u_m/v)**2+(m*vbqdd/(v*v))**2)
print(f'密度不确定度:{bqdd}')

import numpy
m=0.47
r1=0.105
r2=0.12
u_m=0.0006
u_r1=0.00001
u_r2=0.00001
zdgl = 0.5*m*(r1**2+r2**2)
zdglp = format(zdgl, '.5E')
print(f'转动惯量:{zdglp}')
bqdd = numpy.sqrt((((r1**2+r2**2)/2)*u_m)**2+(m*r1*u_r1)**2+(m*r2*u_r2)**2)
bqddp = format(bqdd, '.5E')
print(f'不确定度:{bqddp}')

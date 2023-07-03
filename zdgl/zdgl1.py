import numpy
m=0.025
g=9.8015
r=0.025
b1=2.62894
b2=-0.2475
u_m=0.0003
u_r=0.00001
u_b1=0.00393
u_b2=0.00199
zdgl = m*g*r/(b1-b2)
zdglp = format(zdgl, '.5E')
print(f'转动惯量:{zdglp}')
bqdd = numpy.sqrt((u_m/m)**2+(u_r/r)**2+(u_b1/(b1-b2))**2+(u_b2/(b1-b2))**2)
print(f'不确定度%:{bqdd}')
bqddp = format(zdgl*bqdd, '.5E')
print(f'不确定度:{bqddp}')

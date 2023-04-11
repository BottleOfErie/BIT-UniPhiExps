import numpy
l = 200.06
m = 32.80
d = 4.943
f = 566.45
u_l = 0.01
u_m = 0.01
u_d = 0.002
u_f = 2.835
T = 1.003
ysml = 1.6067*l*l*l*m*f*f/(d*d*d*d)*T
ysmlp = format(ysml, '.3E')
print(f'杨氏模量:{ysmlp}')
bqdd = numpy.sqrt(16*(u_d/d)**2+(u_m/m)**2+9*(u_l/l)**2+4*(u_f/f)**2)
print(f'不确定度%:{bqdd}')
bqddp = format(ysml*bqdd, '.3E')
print(f'不确定度:{bqddp}')

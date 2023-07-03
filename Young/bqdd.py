import numpy

k = 3
delta = 0.0004
lst = [8.25,8.103,7.887,7.752,6.815]
ave = numpy.average(lst)
print(f'Average:{ave}')
out = 0
alpha = 0
beta = 0
for i in lst:
    out += (i-ave)**2
if (len(lst) < 2):
    print("No enough elements")
else:
    out /= len(lst)-1
    print(f'实验标准误差:{numpy.sqrt(out)}')
    out /= len(lst)
    alpha = numpy.sqrt(out)
    print(f'Alpha:{alpha}')
    beta = delta/k
    print(f'Beta:{beta}')
    print(f'C:{numpy.sqrt(alpha*alpha+beta*beta)}')

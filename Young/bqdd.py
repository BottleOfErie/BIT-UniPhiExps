import numpy

k = numpy.sqrt(3)
delta = 0.02
lst = [33.04,33.02,33.06,33.1,33.04,33.04,33.02]
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

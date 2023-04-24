import numpy

lst = [33.04,33.02,33.06,33.1,33.04,33.04,33.02]
ave = numpy.average(lst)
out = 0
for i in lst:
    out += (i-ave)**2
if (len(lst) < 2):
    print("No enough elements")
else:
    out /= len(lst)-1
    print(f'实验标准误差:{numpy.sqrt(out)}')

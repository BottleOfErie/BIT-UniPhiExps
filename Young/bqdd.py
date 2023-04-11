import numpy

k = 2
delta = 2
lst = [676.94, 675.05, 670.09, 667.53]
ave = numpy.average(lst)
out = 0
alpha = 0
beta = 0
for i in lst:
    out += (i-ave)**2
if (len(lst) < 2):
    print("No enough elements")
else:
    out /= len(lst)-1
    alpha = numpy.sqrt(out)
    print(f'Alpha:{alpha}')
    beta = delta/k
    print(f'Beta:{beta}')
    print(f'C:{numpy.sqrt(alpha*alpha+beta*beta)}')

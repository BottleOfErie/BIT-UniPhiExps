import numpy

m_1=11
m_2=21.1
m_3=9.06
u_m=0.05/numpy.sqrt(1.645)
water=0.997795
ans=m_1*water/(m_2-m_3)
print(f'密度:{ans}')
bqddp = numpy.sqrt((u_m/m_1)**2+(u_m/(m_2-m_3))**2+(u_m/(m_3-m_2))**2)
print(f'相对不确定度:{bqddp}')
print(f'不确定度:{ans*bqddp}')

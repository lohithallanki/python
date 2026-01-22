import numpy as np
a = np.array([3,12,7,25,5,18,2])
print("Original Array:")
print(a)
a_m = a.copy()
a_m[a_m>10]=10
print("\n Array after applying condition(values >10 set to 10):")
print(a_m)
a_m1 = a.copy()
a_m1[a_m1<10]=0
print("\n Array after applying condition(values <10 set to 0):")
print(a_m1)

a_m2 = np.where(a>10,10,a)
print("\n values >10 set to 10:")
print(a_m2)
a_m3 = np.where(a<10,0,a)
print("\nvalues <10 set to 0:")
print(a_m3)

a_m4 = np.where(a>10,10,np.where(a<10,0,a))
print("\nvalues >10 set to 10 and <10 set to 0:")
print(a_m4)

a_m5 = np.where(a<10,10,np.where(a<5,0,np.where(a==5,1,a)))
print("\narray after using multiple where():")
print(a_m5)

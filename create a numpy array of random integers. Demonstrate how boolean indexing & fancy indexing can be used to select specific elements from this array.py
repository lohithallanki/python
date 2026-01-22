import numpy as np

#create a numpy array of random integers
arr = np.random.randint(1,20,size=10)
print("Original Array:")
print(arr)

#boolean indexing
bool_selected = arr[arr > 10]
print("\n Elements > (Boolean Indexing):")
print(bool_selected)

#select even numbers
even_selected = arr[arr % 2 == 0]
print("\n Even numbers (Boolean Indexing):")
print(even_selected)

#Fancy indexing
#select elements at specific positions
indices = [0,3,5]
fancy_selected = arr[indices]
print("\n Elements at positions 0,3 and 5(Fancy Indexing):")
print(fancy_selected)

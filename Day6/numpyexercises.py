# Coding Exercise 1:

# 1. Import np
import numpy as np

# 2. Create an array of 10 zeros
a = np.zeros(10)
print(a)

# 3. Create an array of 10 ones
a = np.ones(10)
print(a)

# 4. Create an array of 10 fives
a = np.ones(10) * 5
print(a)

# 5. Create an array of integers from 10 to 50
a = np.arange(10,51,1)
print(a)


# 6. Create an array of even integers from 10 to 50
a = np.arange(10,51,2)
print(a)


# 7. Create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(0, 9).reshape(3,3)
print(a)

# 8. Create a 3x3 identity matrix
a = np.identity(3)
print(a)

# 9. Use numpy to randomly generate a number between 0 and 1
b = np.random.random(1)[0]
print(b)
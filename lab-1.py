# ID No: 620120311
# Lab No: 1

# Question 1:
def hello():
    print("ECSE3038 - Engineering IoT Systems")

# Question 2: ((INCOMPLETE))
# 1. pwd must be > 7 characters 
# 2. pwd must be alphanumeric
# 3. pwd must have 2 or more numbers
def validatePassword(pwd):
    check = 0 

    if len(pwd) > 7 and pwd.isalnum():  
        for element in pwd:
            if element.isdigit():
                check += 1
        if check >= 2: 
            return True
        else: 
            return False
    
    else: 
        return False

# Question 3:
# 1. num must be > 1
# 2. add all values in range 1 - num
def sumUpToN(num):
    sum = 0
    num += 1
    
    if num < 1:
        return -1

    else:
        for index in range(num):
            sum += index    
        return sum

hello()
print(validatePassword("hbhjdbj7"))
print(sumUpToN(6))
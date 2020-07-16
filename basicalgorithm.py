# generate fibbonacci
def fib(n):
    x = 0
    y = 1
    fibbonacci = []
    while (x < n):
        fibbonacci.append(x)
        collect = x + y
        x = y 
        y = collect
    return fibbonacci
# show fibbonacci result
print(fib(255))

# generate odd number
def oddnumber(n):
    x = 1
    odd = []
    while (x < n):
        odd.append(x)
        x = x + 2
    return odd
# show the odd number
print(oddnumber(20))

# generate the even number
def evennumber(n):
    x = 0
    even = []
    while (x < n):
        x = x + 2
        even.append(x)
    return even
# show even number
print(evennumber(20))

# find min value from array
def findmin(array_input):
    n = len(array_input)
    i = 0
    minumum = array_input[0]
    while (i < n-1):
        if (minumum < array_input[i+1]):
            minumum = minumum
        else:
             minumum = array_input[i+1]  
        i = i + 1
    return minumum 
# show minimum number
data = [2,1,0]
print("Minimum value:",findmin(data))

# find max value from array
def findmax(array_input):
    n = len(array_input)
    i = 0
    maximum = array_input[0]
    while (i < n-1):
        if (maximum > array_input[i+1]):
            maximum = maximum
        else:
             maximum = array_input[i+1]  
        i = i + 1
    return maximum 
# show maximum number
data = [2,1,4]
print("Maximum value:",findmax(data))

# find a number inside array
def findnumber(number, array_input):
    n = len(array_input)
    i = 0
    getnumber = 0
    getindex = 0
    while (i < n):
        if (number == array_input[i]):
            getnumber = number
            getindex = i 
            return getnumber, getindex
        else:
            getnumber = 0
        i = i + 1
# show result
arraydata = [1,2,3,4,5]
num,id = findnumber(2,arraydata)
print("Find Number:",num)
print("Find Index Number:",id)

# fast find number inside array
def fastfindnum(number, array_input):
    if number in array_input:
        index = array_input.index(number)
        return 'Yes', index
    else:
        index = 'No Index'
        return 'No', index

arraydata = [1,2,3,4,5]
res,idx = fastfindnum(6,arraydata)
print("Result:", res)
print("Index:", idx)

# Password verification without using regex
def checkpass(input_pass):
    n = len(input_pass)
    checksym = '!@#$%^&*()'
    checknum = '1234567890'
    if n < 8:
        print("Password at least has 8 characters")
    else:
        print('Password is good')
    
    i = 0
    countsym = 0
    getcountsym = 0
    while (i < n):
        if (input_pass[i] in checksym):
            countsym = countsym + 1
            getcountsym = countsym
        else:
            countsym = 0
        i = i + 1
    
    if getcountsym < 2:
        print("Password at least has 2 characters of symbol")
    else:
        print('Password is good')

    j = 0
    countnum = 0
    getcountnum = 0
    while (j < n):
        if (input_pass[j] in checknum):
            countnum = countnum + 1
            getcountnum = countnum
        else:
            countnum = 0
        j = j + 1
    
    if getcountnum < 2:
        print("Password at least has 2 numbers")
    else:
        print('Password is good')

password = '!@cdd10a'
checkpass(password)

# sort array from minimum to maximum
def mintomax(array_input):
    m = len(array_input)
    i = 0
    result = []
    while (i < m):
        save = array_input[0]
        n = len(array_input)
        j = 0
        while (j < n-1):
            if save < array_input[j+1]:
                save = save
            else:
                save = array_input[j+1]
            j = j + 1
        
        # find index of save number
        k = 0
        while (k < n):
            if save == array_input[k]:
                idn = k
            k = k + 1

        array_input = array_input[0:idn] + array_input[idn+1:]
        n = len(array_input) 
        result.append(save)
        i = i + 1
    return result

d = [3,1,5,2,7,4,3]
print(mintomax(d))

# sort array from maximum to minimum
def maxtomin(array_input):
    m = len(array_input)
    i = 0
    result = []
    while (i < m):
        save = array_input[0]
        n = len(array_input)
        j = 0
        while (j < n-1):
            if save > array_input[j+1]:
                save = save
            else:
                save = array_input[j+1]
            j = j + 1
        
        # find index of save number
        k = 0
        while (k < n):
            if save == array_input[k]:
                idn = k
            k = k + 1

        array_input = array_input[0:idn] + array_input[idn+1:]
        n = len(array_input) 
        result.append(save)
        i = i + 1
    return result


d = [3,1,5,2,7,4,3]
print(maxtomin(d))




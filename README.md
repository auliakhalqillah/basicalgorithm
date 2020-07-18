# Basic Algorithms
A collected codes of basic algorithms by using Python. This repository is used to help who want to understand about basic algorithms. In this repository, you get basic algorithms such as:
1. Fibbonacci series
2. Odd number series
3. Even number series
4. Finding minimum value
5. Finding maximum value
6. Finding a number inside an array
7. Password verification without using regex (regular expression)
8. Sorting a number in array from minimum to maximum
9. Sorting a number in array from maximum to minimum

## 1. Fibbonacci Series
Fibbonacci series is a sequence number that each number is the sum of the two numbers (previous number and current number), starting from 0 and 1, where 0 is previous number and 1 is current number. So,

`F0 = 0, F1 = 1`

and

`F(n) = F(i) + F(i+1)`

for `n > 1`. An example Fibbonacci series is:

`0 1 1 2 3 5 8 13 21 34 ...`

An algorithm of Fibbonacci series is:

1.	Set initial number i = 0, x = 0 and y = 1
2.	Set the maximum iteration, n
3.	Do while i is less than n
4.	Sum the x and y and store it to a variable, such as collect
5.	Update the new x equal to y
6.	Update the new y equal to collect
7.	Repeat the proses 3 – 7. The process will stop when i is greater than n

## 2. Odd Number Series
Odd number or odd number series is a sequence number that if a number divided by two, the result is fraction. The odd number series can be written as:

`1 3 5 7 9 11 13 ...`

Let’s take a look from a normal number series bellow,

`1 2 3 4 5 6 7 8 9 10 12 13 14 ...`

From 1 to 3 has two interval point (3-1 = 2), from 3 to 5 either and so on. So, the odd numbers have an two interval between a numbers. It’s means, for each odd number is added by two to get a new odd number. The algorithm of odd number is

`Xodd = Xodd + 2`

where `Xodd` starting by 1.

An algorith of odd number series is:

1.	Set initial number of x = 1
2.	Set maximum number of odd number series, n
3.	Do while x is less than n
4.	Sum the x by 2 and it will become new x for next iteration (x = x + 2)
5.	Repeat the process 3 – 4. The process will stop when the x is greater than n

## 3. Even Number Series
Even number series is oposite from odd number series. It has same iterval, but the initial value of `Xeven` starting by 2.

## 4. Finding Minimum Value
An algorithm for finding minimum value of an array is:

1.	Set length of an array, n
2.	Set initial iteration i = 0
3.	Set initial minimum value from first index of array, minimum = array(1)
4.	Do while i is less than n-1
5.	If the minimum less than the next array(i+1), save the minimum. Otherwise, update minimum to next array(i+1)
6.	Repeat the process 4 – 5 for next iteration

## 5. Finding Maximum Value
For finding maximum value is oposite from finding minimum value. Just change the the condition "less than" to "greater than" on point of 4 (Finding Minimum Value).

## 6. Finding Number Inside Array
An algorithm to finding a number inside an aray is:

1.	Set a length of an array, n
2.	Set initial iteration, i = 0
3.	Set a number that want to find, number = [a number]
4.	Set a  chamber of number variable, getnumber = 0
5.	Set a chamber of index variabel, getindex = 0
6.	Do while i less than n
7.	If number equal to array(i), save the number into getnumber, save the index of i into getindex and stop the process. Otherwise, set getnumber equal to 0.
8.	Repeat process 6 – 7. The process will stop when index of i is greater than a length of array n

## 7. Password Verification
An algorithm concept of password verification is close to finding number inside array. It is applied for each condition, to verification symbol in password and to verification number in password.

## 8. Sorting Number
An algorithm concept of sorting number (minimum to maximum and maximum to minimum) uses the concept of finding minimum number (minimum to maximum) or maximum number (maximum to minimum). For each result of finding number is merged to a another variable as collected result of sorting number. 

# Tested
Tested on Python 3.7.7

# Contact
eamil: auliakhalqillah.mail@gmail.com or personal@auliakhalqillah.com

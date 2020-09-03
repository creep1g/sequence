'''
Algorithm that generates the first n numbers in
the following sequence 1,2,3,6,11,20,37......

The algorithm uses three numbers on each iteration
First we start with numbers 0, 1, 2,
we add them: 0 + 1 + 2 = 3
on the next iteration the numbers shift one step so they become:
1 + 2 + 3 = 6 
we do this n-2 amount of times
'''
n = int(input("Enter the length of the sequence: ")) # Do not change this line
#initialize first 3 integers for addition
count = 0
count_2 = 1
count_3 = 2
print(count_2)
print(count_3)
for i in range(2,n):
   # print(i)
    sum_number = count + count_2 + count_3
    count = count_2
    count_2 = count_3
    count_3 = sum_number
    print(sum_number)


'''
Algorithm that generates the first n numbers in
the following sequence 1,2,3,6,11,20,37......
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


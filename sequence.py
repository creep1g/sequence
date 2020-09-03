'''
Algorithm that generates the first n numbers in
the following sequence 1,2,3,6,11,20,37......
'''
n = int(input("Enter the length of the sequence: ")) # Do not change this line
count_j = 0
for i in range(1,n):
    for j in range(1, n):
        count_j +=1
    print(count_j)
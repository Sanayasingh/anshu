"""x=0
while x<=10:
    print(x)
    x=x+1"""
print("Number Pattern ")

# Decide the row count. (above pattern contains 5 rows)
#row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
"""for i in range(1, row + 1, 1):
    # Run inner loop i+1 times
    for j in range(1, i + 1):
        print(j, end=' ')
    # empty line after each row
    print("")"""
"""s=0
n=int(input("enter the number"))
for i in range(1,n+1,1):
        s=s+i
        print("\n")
        print("sum is:",s)"""
""""s = 0
n = int(input("Enter number "))
# run loop n times
# stop: n+1 (because range never include stop number in result)
for i in range(1, n + 1, 1):
    # add current number to sum variable
    s += i
print("\n")
print("Sum is: ", s)"""
'''n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)'''
'''n=int(input("enter the number"))
for i in range(1,11,1):
       mul=n*i
       print(mul)'''
'''numbers=[12,75,150, 180, 145, 525, 50]
for item in numbers:
    if item>500:
     break
    elif item>150:
        continue
    elif item%5==0:
          print(item)'''

"""numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)"""
'''num=75869
count=0
while num!=0:
    num=num//10
    count=count+1
    print("total digits are :",count)'''
"""num = 75869
count = 0
while num != 0:
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    count = count + 1
print("Total digits are:", count)"""
"""n=5
k=5
for i in range(0,n+1):
    for j in range(k-1,0,-1):
        print(j,end=' ')
    print()"""
'''n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()'''
"""list1 = [10, 20, 30, 40, 50]
newlist=reversed(list1)
for item in newlist:
    print(item)"""
"""list1=[10,20,30,40,50]
size=len(list1)
print(size)"""
"""list1 = [10, 20, 30, 40, 50]
# get list size
# len(list1) -1: because index start with 0
# iterate list in reverse order
# star from last item to first
size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])"""
"""for num in range(-10,0,1):
    print(num)"""
for i in range(5):
    print(i)
else:
    print('Done!')

lst = []
n = int (input ("Enter the limit: "))
print ("Enter the elements : \n")
for i in range (0,n):
    ele = int (input ())
    lst.append (ele)
print ("The elements are : ", lst)
print ("The positive numbers are: ")
for i in range (len (lst)):
    if lst[i] >= 0:
        print (lst[i], end=" ")

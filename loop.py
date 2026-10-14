# i = 5
# while (i >= 1):
#     print(i)
#     i -=1

# i = 1
# while (i <= 5):
#     print(i)
#     i +=1


# multiple of any number

# n = int(input("enter number: "))

# i = 1 
# while (i <= 10):
#     print(n*i)
#     i +=1


# break nd continue

# i = 1
# while (i <= 10):
#     if (i % 6 ==0):
#         break
#     print(i)
#     i +=1
# print("outsider of loop")




i = 1
while (i <= 10):
    if (i % 3 ==0):
        i +=1
        continue
    print(i)
    i +=1
print("outsider of loop")
# numbers = range(1,101)

# def primers(numbers):
#     for x in range(2, numbers):
#         if (numbers%x) == 0:
#             return False
#     return True

# primes = list(filter(primers, numbers))

# print(primes)

# while True:
#     userinput = input("Click Y or N please!")
#     if userinput == 'Y' or userinput == 'y':
#         print("clicked y!")
#         break
#     elif userinput == 'N' or userinput == 'n':
#         print("Nah fam")
#         break
#     else:
#         print("Click Y or N please!!!")


old = {1:2, 3:4}
new = {"a":"b"}

print(old)

list(old)
new.update(old)
old = new

print(old)




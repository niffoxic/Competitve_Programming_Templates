t = int(input())
 
for i in range(t):
 
 num = input()
 
 if("21" in num or int(num) % 21 == 0):
 
    print("The streak is broken!")
 
 else:
 
    print("The streak lives still in our heart!")

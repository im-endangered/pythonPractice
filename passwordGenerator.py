import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','%','^','&','*','(',')']
no_of_letters=int(input("Enter number of letters\n"))
no_of_numbers=int(input("Enter number of numbers\n"))
no_of_symbols=int(input("Enter Number of Symbols\n"))
password=[]
final_password=''
for i in range(0,no_of_letters):
    password.append(random.choice(letters))
for i in range(0,no_of_numbers):
    password.append(random.choice(numbers))
for i in range(0,no_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
for i in password:
    # print(type(i))
    final_password+=str(i)

print(f"Hello. Your password could be {final_password}")
# filewithpw=open('password.txt')
# filewithpw.write(f"Hello. Your password could be "+final_password)
# close(password.txt)

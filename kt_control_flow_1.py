# Question 1 write a program that prints all the odd numbers between variable A and variable B

num_a = int(input("Enter first number: "))
num_b = int(input("Enter first number: "))

if num_a < num_b:
    while num_a < num_b:
        num_a += 1
        if num_a % 2 != 0 and num_a != num_b:
            print(num_a)

elif num_a > num_b:
    num_c = num_a
    while num_a > num_b:
        if num_a % 2 != 0 and num_a != num_c:
            print(num_a)      
        num_a -= 1

 
# Question 2 write a program given a variable "S" print all the even characters (in terms of the length)

s = input("Enter a phrase: ")

print(s[1::2])

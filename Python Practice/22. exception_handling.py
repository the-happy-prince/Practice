num = input("Enter the number: ")
try:
    if(int(num)>20):
        raise ValueError(f"Value should be between 2 and 20")
except ValueError:
    print("ValueError")
finally:
    print("Finally")
print(f"Table of number {num} is below:")

# for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# This for loop can run, but what if the user gives a float as input. We are sure about the chance of getting errors so we will use try-except for exception handling

try:
    for i in range(1, 11):
        print(f"{int(num)} X {i} = {int(num)*i}")
except Exception as e: # Instead of Exception, we can use ValueError and IndexError. Read more about them.
    print(e)
finally:
    print("Finally")

print(f"Print it after exception handliing")
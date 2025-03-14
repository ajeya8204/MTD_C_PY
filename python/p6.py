def my_function(my_number):
    my_number[0] = 1000
    my_number[-1] = 10000

print('enter space separated nos of ur choice:')
number = [int(element) for element in input().split()]  # Input should be space-separated numbers
print(number)
my_function(number)
print(number)


values=input().split()
print(values)

my_str = raw_input("Enter a string in the format word:number: ")
values = my_str.split(':')
str_part = values[0]
total_sum = 0
for char in values[1]:
    total_sum = total_sum + int(char)**2
if total_sum % 2 == 0:
    new_str = str_part[-1] + str_part[:-1]
else:
    new_str = str_part[2:] + str_part[:2]
print(new_str)

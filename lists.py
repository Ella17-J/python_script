numbers = list(range(1,21))
print(numbers)

million_nums = list(range(1,1000001))
#print(million_nums)
print(min(million_nums))
print(max(million_nums))
print(sum(million_nums))

odd_numbers = list(range(1,21,2))
print(odd_numbers)
three_multiples = list(range(3,31,3))
print(three_multiples)

for value in range(1,11):
    cube_numbers = value**3
    print(cube_numbers)

cube = [value**3 for value in range(1,11)]
print(cube)
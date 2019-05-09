import itertools

numbers = []

while len(numbers) <= 4:
    number = input("enter a number: ")
    numbers.append(number)

good_combinations = []
all_combinations = set(itertools.permutations(numbers))
for combination in all_combinations:
    if combination[0] == 0:
        continue
    else:
        good_combinations.append(combination)

print(good_combinations)

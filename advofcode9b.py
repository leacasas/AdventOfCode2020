# Find a contiguous set of at least two numbers which sum to the invalid number from step 1
# To find the encryption weakness, add together the smallest and largest number in this contiguous range
# This is a variation of the "Knapsack problem"

lines = open("advofcode9_input.txt", "r").readlines()
#lines = open("advofcode9_example.txt", "r").readlines()
lines = list(map(int, lines))

def find_sets(numbers, number):
    subset = []
    total = 0

    for i in range(len(numbers)):
        total += numbers[i]
        subset.append(numbers[i])

        for j in range(i, len(numbers), 1):
            if i == j : continue

            if total + numbers[j] < number:
                total += numbers[j]
                subset.append(numbers[j])
                continue
            elif total + numbers[j] == number:
                total += numbers[j]
                subset.append(numbers[j])
                return subset
            else:
                total = 0
                subset.clear()
                break
    
    return subset

invalid_number = 1309761972
#invalid_number = 127

result = find_sets(lines, invalid_number)
result.sort()

print(result[0] + result[-1])
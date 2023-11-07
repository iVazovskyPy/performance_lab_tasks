file_path = input()

with open(file_path) as f:
    numbers = f.read().split()
    numbers = [int(x) for x in numbers]

    average_value = round(sum(numbers)/len(numbers))
    count = 0
    for i_num in numbers:
        count += abs(average_value - i_num)

print(count)

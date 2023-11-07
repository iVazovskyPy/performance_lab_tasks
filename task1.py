n, m = input().split()
numbers_line = str()

for i_num in range(int(m)):
    numbers_line += str(i_num + 1)

while True:
    current_num = int(numbers_line[-1]) + 1
    numbers_line += numbers_line[-1]

    for _ in range(int(n)-1):
        if current_num > int(n):
            current_num = 1
        else:
            numbers_line += str(current_num)
            current_num += 1

    if numbers_line[-1] == '1':
        break

result_line = numbers_line[::int(m)]
print(int(result_line))

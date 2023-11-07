path_to_round_file = input()
path_to_points_file = input()

with open(path_to_round_file) as f:
    round_center = f.read().split()

round_center = [int(x) for x in round_center]


with open(path_to_points_file) as f:
    points = f.read().split('\n')

range_x_axle = [round_center[2]+round_center[0], -round_center[2]+round_center[0]]
range_y_axle = [round_center[2]+round_center[1], -round_center[2]+round_center[1]]

x_code_status = str()
y_code_status = str()

for i_point in points:
    if range_x_axle[1] < int(i_point[0]) < range_x_axle[0]:
        x_code_status = 'in'
    elif int(i_point[0]) == range_x_axle[1] or int(i_point[0]) == range_x_axle[0]:
        x_code_status = 'on'
    else:
        x_code_status = 'out'

    if range_y_axle[1] < int(i_point[-1]) < range_y_axle[0]:
        y_code_status = 'in'
    elif int(i_point[-1]) == range_y_axle[1] or int(i_point[-1]) == range_y_axle[0]:
        y_code_status = 'on'
    else:
        y_code_status = 'out'

    if 'out' in [x_code_status, y_code_status]:
        print(2)
    elif 'on' in [x_code_status, y_code_status]:
        print(0)
    else:
        print(1)

    x_code_status = str()
    y_code_status = str()

def check_win_y():
    check_0 = field_list[0][0] + field_list[1][0] + field_list[2][0]
    check_1 = field_list[0][1] + field_list[1][1] + field_list[2][1]
    check_2 = field_list[0][2] + field_list[1][2] + field_list[2][2]
    if check_0 == win_x or check_1 == win_x or check_2 == win_x:
        print("X wins")
        return True
    elif check_0 == win_o or check_1 == win_o or check_2 == win_o:
        print("O wins")
        return True


def check_win_x():
    check_0 = "".join(field_list[0])
    check_1 = "".join(field_list[1])
    check_2 = "".join(field_list[2])

    if check_0 == win_x or check_1 == win_x or check_2 == win_x:
        print("X wins")
        return True
    elif check_0 == win_o or check_1 == win_o or check_2 == win_o:
        print("O wins")
        return True


def check_win_diagonals():
    check_0 = field_list[0][0] + field_list[1][1] + field_list[2][2]
    check_1 = field_list[0][2] + field_list[1][1] + field_list[2][0]
    if check_1 == win_x or check_0 == win_x:
        print("X wins")
        return True
    elif check_0 == win_o or check_1 == win_o:
        print("O wins")
        return True


win_o = "OOO"
win_x = "XXX"
turn = 1
cells_input = " " * 9

field_list = [[cells_input[0], cells_input[1], cells_input[2]],
              [cells_input[3], cells_input[4], cells_input[5]],
              [cells_input[6], cells_input[7], cells_input[8]]]

print(f"""---------
| {field_list[0][0]} {field_list[0][1]} {field_list[0][2]} |
| {field_list[1][0]} {field_list[1][1]} {field_list[1][2]} |
| {field_list[2][0]} {field_list[2][1]} {field_list[2][2]} |
---------""")

while True:
    x = input("Enter the coordinates: ")
    y = ""

    def check_input():
        global x, y

        if " " not in x:
            print("You should enter the numbers!")
            return False
        x, y = x.split()

        if not x.isdigit() or not y.isdigit():
            print("You should enter the numbers!")
            return False

        if not 1 <= int(x) <= 3 or not 1 <= int(y) <= 3:
            print("Coordinates should be from 1 to 3!")
            return False

        if "X" in field_list[int(x) - 1][int(y) - 1] or "O" in field_list[int(x) - 1][int(y) - 1]:
            print("This cell is occupied! Choose another one!")
            return False

    if check_input() is False:
        continue

    if turn % 2 == 1:
        field_list[int(x) - 1][int(y) - 1] = "X"
    else:
        field_list[int(x) - 1][int(y) - 1] = "O"
    turn += 1

    print(f"""---------
| {field_list[0][0]} {field_list[0][1]} {field_list[0][2]} |
| {field_list[1][0]} {field_list[1][1]} {field_list[1][2]} |
| {field_list[2][0]} {field_list[2][1]} {field_list[2][2]} |
---------""")
    if check_win_x() or check_win_y() or check_win_diagonals():
        break
    if turn == 10:
        print("Draw")
        break

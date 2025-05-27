def parse_cmd(command):

    command_name = command.split(" ")
    parameters = command_name[1:]
    return command_name[0], parameters


def draw_board(board):
    size = len(board)  # מספר השורות וגם מספר העמודות

    index_width = len(str(size - 1))  # רוחב ההזחה (למספרי שורות)
    result = " " * (index_width + 1)  # רווחים לשורת האותיות

    # שורת האותיות
    for i in range(size):
        result += chr(ord('A') + i) + " "
    result += "\n"

    # שורות הלוח
    for row_index, row in enumerate(board):
        row_str = str(row_index).rjust(index_width) + " |"
        for cell in row:
            row_str += cell + "|"
        result += row_str + "\n"

    return result


def convert_coords(location: str) -> tuple[int, int]:
    row_str = ""
    col_char = ""

    # נפריד את הספרות מהאות (תומך גם ב-10A, 12C וכו')
    for char in location:
        if char.isdigit():
            row_str += char
        else:
            col_char += char.upper()

    row = int(row_str)
    col = ord(col_char) - ord('A')

    return row, col

# This is a run example, use this to verify your code
# you should remove this code later
command, parameters = parse_cmd("test_command a b c d e")
print(f"This is the command: {command}")
print(f"This is the parameters: {parameters}")
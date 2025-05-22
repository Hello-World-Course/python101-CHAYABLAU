def parse_cmd(command):

    command_name = command.split(" ")
    parameters = command_name[1:]
    return command_name[0], parameters


# This is a run example, use this to verify your code
# you should remove this code later
command, parameters = parse_cmd("test_command a b c d e")
print(f"This is the command: {command}")
print(f"This is the parameters: {parameters}")
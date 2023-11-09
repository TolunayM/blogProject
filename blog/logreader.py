
def read_logs():
    log_file = 'access.log'

    with open(log_file, "r") as file:
        log_data = file.read()

    lines = log_data.split("\n")
    for line in lines:
        if line and line[-1].isdigit():
            print(line)
            return line



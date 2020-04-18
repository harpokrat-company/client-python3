

def exit_error(code = 0, message=None):
    if message is not None:
        print("ERROR: " + message)
    exit(code)

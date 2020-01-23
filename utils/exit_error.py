

def exit_error(code = 0, message=None):
    if message != None:
        print("ERROR: " + message)
    exit(code)

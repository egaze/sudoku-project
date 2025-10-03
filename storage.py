def load_from_storage(file_name):
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        file = open(file_name, 'w') # Creating the file
        file = open(file_name, 'r') # Setting the mode of the file we just created to read
    file_contents = file.read()
    if not file_contents: # Empty file
        return dict()
    else:
        data = eval(file_contents)
        return data


def save_to_storage(filename, save_state):
    file = open(filename, 'w')
    file.write(str(save_state))
    print('Saved to local storage!')



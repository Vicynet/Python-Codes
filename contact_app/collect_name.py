def collect_name():
    name = input("type your name: ").strip().lower()
    while not name.isalpha():
        print('Invalid name entry')
        name = input("type your name: ").strip().lower()
    return name

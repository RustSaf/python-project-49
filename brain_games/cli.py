import prompt


def main():
    print('Welcome to the Brain Games!')


def welcome_user():
    main()
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


if __name__ == '__main__':
    main()

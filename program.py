
def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (BR2)? ')

    # get html from web
    print(code)
    # parse the html
    # display for the forecast
    print('hello from main')


def print_the_header():
    print('----------------------------')
    print('       WEATHER APP')
    print('----------------------------')
    print()


if __name__ == '__main__':
    main()


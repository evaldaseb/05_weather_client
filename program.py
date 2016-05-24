
def main():
    print_the_header()

    code = input('What zipcode do you want the weather for (BR2+7PD)? ')

    # get html from web
    get_html_from_web(code)
    # parse the html
    # display for the forecast
    print('hello from main')


def print_the_header():
    print('----------------------------')
    print('       WEATHER APP')
    print('----------------------------')
    print()


def get_html_from_web(postcode):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(postcode)
    print(url)

if __name__ == '__main__':
    main()


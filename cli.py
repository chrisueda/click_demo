# cli.py
import click
import requests

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'


def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'http://samples.openweathermap.org/data/2.5/weather'

    query_params = {
        'q': location,
        'appid': api_key
    }

    print(query_params)

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']


@click.command()
@click.argument('location')
@click.option('--api-key', '-a')
def main(location, api_key):
    # TODO check if api_key is set
    weather = current_weather(location)
    print(f"The weather in {location} right now: {weather}.")


if __name__ == "__main__":
    main()

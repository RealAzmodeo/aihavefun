import requests

def get_random_joke():
    """
    Fetches a random joke from the official-joke-api.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    joke_data = response.json()
    return f"{joke_data['setup']} - {joke_data['punchline']}"

if __name__ == "__main__":
    print(get_random_joke())

import random

def get_random_joke():
    """
    Returns a random joke from a predefined list.
    """
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some couples go to the gym? Because some relationships don't work out!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "What do you call a fake noodle? An Impasta!",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    print(get_random_joke())

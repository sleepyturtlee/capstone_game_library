import requests

# API setup
# the base URL of the API we are using
base_url = "https://random-word-api.herokuapp.com/"

# get a random word from the API
def get_word():
    url = f"{base_url}/word?length=5"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        global word_of_day
        word_of_day = "".join(response.json()).upper()
        print(word_of_day)

# checks if a string of words is a real word (AKA if it's in the API)
def legit_word(word):
    # sorts for a word with a length of 5, and gets as many of those words as it can
    # I tried to get all of them by exceeding the # of all the words in the database, 
    # which will just get me all the 5 letter words in there
    url = f"{base_url}/word?length=5&number=1000000000"
    response = requests.get(url)
    print(response)

    # response status code 200 means the API is working
    if response.status_code == 200:
        if word.lower() in response.json():
            print("word is in the API")
            return True
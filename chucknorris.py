import requests
import json


#random chuch norris jokes
random_url = "https://api.chucknorris.io/jokes/random"


#list of categories
category_url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
random_cat_url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
search_url = "https://api.chucknorris.io/jokes/search?query={query}"



'''

Part I
The program should welcome the user by displaying a random chuch norris joke
'''

print('Here\'s a random Chuck Norris joke:')
url = 'https://api.chucknorris.io/jokes/random'
r = requests.get(url)

response = r.json()

print(response['value'])
print()


'''
Part II
list the categories to the user and ask to pick a category
'''

print('Here\'s a list of categories to choose from:')
url = 'https://api.chucknorris.io/jokes/categories'
r = requests.get(url)

response = r.json()

for category in response:
    print(category)

chosen_category = input('Please select a category fom the list: ')
print()


'''
Part III
Display a joke based on the category picked by the user
'''

print('Here is a joke from the category you selected!')
url = f"https://api.chucknorris.io/jokes/random?category={chosen_category}"
r = requests.get(url)
response = r.json()

print(response['value'])
print()

# to continue the program
input()

'''

Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''
response = input('Enter a few key words to find a Chuck Norris joke similar to your criteria: ')

url = f"https://api.chucknorris.io/jokes/search?query={response}"
r = requests.get(url)
response = r.json()


results = response.get('result', [])

if results:
    print("Here's the joke based on your selection:")
    print(results[0]['value'])
else:
    print("Sorry, no jokes were found for that search term.")
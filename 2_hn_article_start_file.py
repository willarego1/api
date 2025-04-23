import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')

submission_ids = r.json()

json.dump(submission_ids,outfile,indent=2)

url = 'https://hacker-news.firebaseio.com/v0/item/43646095.json'
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile, indent=4)

#exercise
#grab the top 10 stories and print out the title, discussion link and commenbts.
# sort it based on number of comments


sub_list = []

for sub_id in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{sub_id}.json'
    r = requests.get(url)
    response = r.json()

    a_dict = {
        'title': response['title'],
        'hn_link': f'https://news.ycombinator/com/item?id={sub_id}',
        'comments': response['descendants'],
    }
    sub_list.append(a_dict)

print(sub_list)
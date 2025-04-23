import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('output.json', 'w')

response = r.json()


list_of_repos = response['items']

#how many repos are in this file
print(len(list_of_repos))

#examine the first repo
first_repo = list_of_repos[0]

#how many attributes describe each repo?
#technically it is how many keys are in each repo

print(len(first_repo))

for key in first_repo:
    print(key)

#exercise
# print out the full name, the html url, the license name and topics
# for the first repo

print(f'Full Name: {first_repo['full_name']}')
print(f'HTML URL: {first_repo['owner']['html_url']}')
print(f'License Name: {first_repo['license']['name']}')

for topic in first_repo['topics']:
    print(topic)



# grab the top 10 repos and create a bar chart
# based on stars

from plotly.graph_objs import Bar
from plotly import offline

repo_names, stars = [], []

for repo_dict in list_of_repos[:10]:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])


data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker':{
        'color':'rgb(60,100,150)',
        'line': {'width':1.5, 'color': 'rgb(25,25,25)'},
    },
    'opacity':0.6,
}]

my_layout = {
    'title':'Most Starred Python Projects on Github',
    'xaxis':{'title':'Repository'},
    'yaxis':{'title':'Stars'},
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='python_repos.html')
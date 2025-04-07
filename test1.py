import requests
import json

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

outfile = open('hn.json','w')

# Process information about each submission.
submission_ids = r.json()
#print(submission_ids)

json.dump(submission_ids,outfile,indent=4)


#STOP HERE to evaluate response in JSON file

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/item/35455850.json"
r = requests.get(url)

outfile = open('hn2.json','w')

json.dump(r.json(),outfile,indent=4)


#STOP HERE to evaluate the response JSON file

submissions_list = []

for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #print(f'title: {response_dict["title"]}')
    #print(f"hn_link: http://news.ycombinator.com/item?id={submission_id}")
    #print(f"Comments: {response_dict['descendants']}")

    #input()

    # The Itemgetter can be used instead of the lambda function to achieve similar functionality. 
    # Outputs in the same way as sorted() and lambda, but has different internal implementation. 
    # It takes the keys of dictionaries and converts them into tuples. It reduces overhead and 
    # is faster and more efficient. 
    from operator import itemgetter
        
        
        # Build a dictionary for each article.
    a_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    submissions_list.append(a_dict)

    #print(submissions_list)
    #input()

submissions_list = sorted(submissions_list, key=itemgetter('comments'),
                                reverse=True)

submissions_list = sorted(submissions_list, key=lambda x:x['comments'],
                                reverse=True)


print(submissions_list)

for d in submissions_list:
    print(f"\nTitle: {d['title']}")
    print(f"Discussion link: {d['hn_link']}")
    print(f"Comments: {d['comments']}")
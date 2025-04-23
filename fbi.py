import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

criminals = r.json()

list_of_criminals = criminals['items']
most_wanted = []

subject_counts = {}

for item in list_of_criminals:
    if 'warning_message' in item.keys():
        if 'SHOULD BE CONSIDERED ARMED AND DANGEROUS' in str(item['warning_message']):
            entry = {
                'name': f'Name: {item['title']}',
                'link': f'FBI direct link: {item['url']}',
                'gender': f'Gender: {item['sex']}',
                'subject': f'Subject: {item['subjects'][0]}'
            }
            most_wanted.append(entry)

for criminal in criminals['items']:
        subjects = criminal.get('subjects', [])
        for subject in subjects:
            if subject in subject_counts:
                subject_counts[subject] += 1
            else:
                subject_counts[subject] = 1

with open("fbi.json", "w") as f:
    json.dump(most_wanted, f, indent=4)

for criminal in most_wanted:
    print(criminal['name'])
    print(criminal['link'])
    print(criminal['gender'])
    print(criminal['subject'])
    print()
    print()


sorted_subjects = sorted(subject_counts.items(), key=lambda x: x[1], reverse=True)


for subject, count in sorted_subjects:
    print(f"Crime: {subject} Count: {count}")
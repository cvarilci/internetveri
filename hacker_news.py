from operator import itemgetter

import requests

# API çağrısı yap ve yanıtı sakla
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Her bir gönderiyle ilgili olan bilgiyi işle
submission_ids = r.json()
submission_dicts = []
try :
    for submission_id in submission_ids[:30]:
        # Her bir gönderiyle ilgili ayrı bir API çağrısı yap.
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        #print(f"id : {submission_id}\tstatus : {r.status_code}")
        response_dict = r.json()

        # Her bir makale için bir sözlük oluştur.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
except KeyError:
    pass
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

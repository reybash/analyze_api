import requests

from plotly.graph_objs import Bar
from plotly import offline
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts, hn_links, titles, comments = [], [], [], []

for submission_id in submission_ids[:15]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    submission_dict = {
        'title': response_dict['title'],
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
    }

    if 'descendants' in response_dict:
        submission_dict['comments'] = response_dict['descendants']
    else:
        submission_dict['comments'] = 0

    submission_dicts.append(submission_dict)


submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    title = submission_dict['title']
    hn_url = submission_dict['hn_link']
    hn_link = f"<a href='{hn_url}'>{title}</a>"
    hn_links.append(hn_link)
    titles.append(submission_dict['title'])
    comments.append(submission_dict['comments'])

data = [{
    "type": "bar",
    "x": hn_links,
    "y": comments,
    "marker": {
        "color": 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    "opacity": 0.6
}]

my_layout = {
    "title": 'Most-Comments Article on HN',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Title of article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Amount of comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions.html')

from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response
url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status Code: {r.status_code}")

#Process information about each submission
submission_ids = r.json()
submission_dicts = []
repo_links, comments, labels = [], [], []
for submission_id in submission_ids[:30]:
	#Make a seperate API call for each submission
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\t Status Code: {r.status_code}")
	response_dict = r.json()

	#Build a dictionary for each article
	submission_dict = {
		"title": response_dict['title'],
		"hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
		"comments": response_dict.get('descendants', 0)
	}

	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


for submission_dict in submission_dicts:
	repo_links.append(f"<a href='{submission_dict['hn_link']}'> {submission_dict['title']}</a>")
	comments.append(submission_dict['comments'])
	labels.append(f"\nTitle: {submission_dict['title']}")
# 	print(f"\nTitle: {submission_dict['title']}")
# 	print(f"Discussion link:  {submission_dict['hn_link']}")
# 	print(f"Comments: {submission_dict['comments']}")

#Make visualization
data  = [{
	'type' : 'bar',
	'x' : repo_links,
	'y' : comments,
	'hovertext':labels,
	'marker':{
	'color':'rgb(60,100,150)',
	'line':{'width':1.5, 'color':'rgb(25,25,25)'}
	},
	'opacity': 0.6
}]

my_layout = {
	'title' : 'Most Active discussion on Hackernews',
	'titlefont':{"size": 28},
	'xaxis': {
	'title':'Discussion',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}
	},
	'yaxis': {'title':'Comments',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'hackernews_visual.html')


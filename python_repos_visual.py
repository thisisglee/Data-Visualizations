import requests

from plotly.graph_objs import Bar
from plotly import offline

#Make an API call and store the response
url='https://api.github.com/search/repositories?q=language:perl&sort=stars'
headers={'Accept':'applications/vnd.github.v3+json'}
r=requests.get(url, headers=headers)
print(f'Status Code: {r.status_code}')

#Process results
#Store API response in a variable
response_dict = r.json()
#Explore information about the respositories.
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
	repo_links.append(f"<a href='{repo_dict['html_url']}'> {repo_dict['name']}</a>")
	stars.append(repo_dict['stargazers_count'])
	owner = repo_dict['owner']['login']
	description = repo_dict['description']
	label = f"{owner}<br /> {description}"
	labels.append(label)


#Make visualization
data  = [{
	'type' : 'bar',
	'x' : repo_links,
	'y' : stars,
	'hovertext':labels,
	'marker':{
	'color':'rgb(60,100,150)',
	'line':{'width':1.5, 'color':'rgb(25,25,25)'}
	},
	'opacity': 0.6
}]

my_layout = {
	'title' : 'Most Stared Python projects on github',
	'titlefont':{"size": 28},
	'xaxis': {
	'title':'Repository',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}
	},
	'yaxis': {'title':'Stars',
	'titlefont': {'size': 24},
	'tickfont': {'size': 14}}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python_repos.html')
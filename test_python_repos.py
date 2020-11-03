import unittest

import requests


def tobetested():
	url='https://api.github.com/search/repositories?q=language:python&sort=stars'
	headers={'Accept':'applications/vnd.github.v3+json'}
	r=requests.get(url, headers=headers)
	response_dict = r.json()
	total_repos = response_dict["total_count"]
	repo_returned = len(response_dict['items'])
	return(r.status_code, total_repos, repo_returned)


class test_python_repos(unittest.TestCase):

	def setUp(self):
		self.status_code, self.total_repos, self.repo_returned = tobetested()

	def test_status_code(self):
		self.assertEqual(int(self.status_code), 200)

	def test_no_of_items(self):
		self.assertEqual(int(self.repo_returned), 30)

	def test_no_of_repo(self):
		self.assertGreater(int(self.total_repos), 5396436)

if __name__ == '__main__':
	unittest.main()
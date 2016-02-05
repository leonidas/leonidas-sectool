import requests
from requests.auth import HTTPBasicAuth
from itertools import chain

from .env import env


class GithubAuth(requests.auth.AuthBase):
    def __init__(self):
        self.auth_header = "token {token}".format(token=env('GITHUB_TOKEN'))

    def __call__(self, request):
        request.headers['Authorization'] = self.auth_header

        return request


GITHUB_AUTH = GithubAuth()


class Github(object):
    def __init__(self, user=None, org=None):
        if (user is None and org is None) or (user is not None and org is not None):
            raise AttributeError("exactly one of user and org must be specified")

        self.user = user
        self.org = org

    @property
    def owner(self):
        return self.org if self.org else self.user

    def make_url(self, *parts):
        return '/'.join(chain(['https://api.github.com'], parts))

    def make_owner_url(self, *parts):
        owner = 'orgs/{org}'.format(org=self.org) if self.org else 'users/{user}'.format(user=self.user)

        return self.make_url(owner, *parts)

    def get(self, *args, **kwargs):
        response = requests.get(auth=GITHUB_AUTH, *args, **kwargs)
        response.raise_for_status()
        return response.json()

    def get_repos(self):
        url = self.make_owner_url('repos')
        return self.get(url)

    def get_repo_contents(self, repo_name):
        url = self.make_url('repos', self.owner, repo_name, 'contents')
        return self.get(url)

    def get_repos_containing_file(self, filename='package.json'):
        for repo in self.get_repos():
            contents = self.get_repo_contents(repo['name'])
            if any(entry['name'] == filename for entry in contents):
                yield repo['name']


if __name__ == "__main__":
    from pprint import pprint
    for repo_name in Github(user='japsu').get_repos_containing_file():
        print(repo_name)
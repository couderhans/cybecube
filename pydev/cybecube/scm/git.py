import requests
import cybecube.converter.json2orm as json2orm

USER = 'AUSER'
GIT_API_URL = 'https://api.github.com'
headers = {'Authorization': 'token {}'.format('263d696fa716a967f4fd8ceddb0029ce91525f04'),
           'Content-Type': 'application/json'}


def get_repository_from_user(user, repository):
    try:
        git_url = '{}/repos/{}/{}'.format(GIT_API_URL, user, repository)
        response = requests.get(git_url, headers=headers)
        print(response.json())
        repository = json2orm.json2repository(response.json(), user)
        return repository
    except requests.RequestException as e:
        print('Failed to get api request from {}'.format(e))


def get_repos_from_user(user):
    try:
        git_url = '{}/users/{}/repos'.format(GIT_API_URL, user)
        response = requests.get(git_url, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print('Failed to get api request from {}'.format(e))


def get_contents_from_repo(user, repo, path):
    try:
        git_url = '{}/repos/{}/{}/contents/{}'.format(GIT_API_URL, user, repo, path)
        response = requests.get(git_url, headers=headers)
        return response.json()
    except requests.RequestException as e:
        print('Failed to get api request from {}'.format(e))


def get_source_from_content(download_url):
    try:
        git_url = '{}'.format(download_url)
        print('source found: {}'.format(git_url))
        response = requests.get(git_url, headers=headers, stream=True)
        return response
    except requests.RequestException as e:
        print('Failed to get api request from {}'.format(e))



import json
import cybecube.scm.git as git
import cybecube.database.repository as repos
import cybecube.database.content as contents

from cybecube.database.repository import Repository
from cybecube.database.content import Content


def scan_user_repositories(user):
    data = git.get_repos_from_user(user)
    print('data: {}'.format(data))
    for element in data:
        print('repository: {} /r'.format(element['name']))
        repository = Repository(user=user, name=element['name'], clone_url=element['clone_url'])
        repos.insert_into_repositories(repository)
        scan_repository_content(user, repository, '')


def scan_repository_content(user, repository, path):
    data = git.get_contents_from_repo(user, repository.name, path)
    repo = repos.get_repository(repository.name)
    for element in data:
        try:
            print('content for repository {}: {} - {}'.format(repo.name, element.get('name'), element.get('type')))
            content = Content(name=element.get('name'), type=element.get('type'), repository=repo)
            contents.insert_into_content(content)
            if element.get('type')=='dir':
                scan_repository_content(user, repository, element.get('name'))
        except AttributeError:
            # counters is not a dictionary, ignore and move on
            pass

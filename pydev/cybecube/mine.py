import cybecube.scm.git as git
import cybecube.database.repository as repos
import cybecube.database.content as contents
import cybecube.database.file as files

from cybecube.database.repository import Repository
from cybecube.database.content import Content
from cybecube.database.file import File, Url


def mine_user_repositories(user):
    data = git.get_repos_from_user(user)
    print('data: {}'.format(data))
    for element in data:
        print('repository: {} /r'.format(element['name']))
        repository = Repository(user=user, name=element['name'], clone_url=element['clone_url'])
        repos.insert_into_repositories(repository)
        mine_repository_content(user, repository, '')


def mine_repository_content(user, repository, path):
    data = git.get_contents_from_repo(user, repository.name, path)
    repo = repos.get_repository(repository.name)
    for element in data:
        try:
            print('content for repository {}: {} - {}'.format(repo.name, element.get('name'), element.get('type')))
            content = Content(name=element.get('name'), type=element.get('type'), repository=repo)
            contents.insert_into_content(content)
            if element.get('type') == 'dir':
                mine_repository_content(user, repository, element.get('path'))
            elif element.get('type') == 'file':
                url = Url(url=element.get('url'),
                          html_url=element.get('download-url'),
                          git_url=element.get('git_url'),
                          download_url=element.get('download_url'))
                file = File(name=element.get('name'),
                            type=element.get('type'),
                            size=element.get('size'),
                            sha=element.get('sha'),
                            url=url,
                            content=content)
                print('file from content {}: {} - url {}'.format(content.name, file, url))
                files.insert_into_file(file)
        except AttributeError:
            # counters is not a dictionary, ignore and move on
            pass

def mine_content_file():
    
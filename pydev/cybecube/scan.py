import cybecube.scm.git as git
import cybecube.database.repositories as repos


def scan_user_repositories(user):
    data = git.get_repos_from_user(user)
    print('data: {}'.format(data))
    for element in data:
        print('repository: {} /r'.format(element['name']))
        print('clone_url: {}'.format(element['clone_url']))
        repo = (user, element['name'], element['clone_url'])
        repos.insert_into_repositories(repo)


def scan_repository_content(user, repo, path):
    data = git.get_contents_from_repo(user, repo, path)
    print('path found: {}'.format(data))

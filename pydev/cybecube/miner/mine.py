from sqlalchemy import null

import cybecube.scm.git as git
import cybecube.database.repository as repositories
import cybecube.database.content as contents
import cybecube.database.file as files
import cybecube.database.package as packages
import  cybecube.database.clazz as clazzes
import cybecube.database.method as methods
import cybecube.analyser.method as methodbot
import fnmatch

from cybecube.database.repository import Repository
from cybecube.database.content import Content
from cybecube.database.package import Package
from cybecube.database.clazz import Clazz
from cybecube.database.method import  Method
from cybecube.database.file import File, Url


def mine_user_repositories(user):
    data = git.get_repos_from_user(user.name)
    print('data: {}'.format(data))
    for element in data:
        print('repository: {}'.format(element['name']))
        repository = Repository(name=element['name'], clone_url=element['clone_url'], user=user)
        if repositories.get_repository(repository.name) is None:
            repositories.insert_into_repository(repository)
        mine_repository_content(repository, '')


def mine_repository_content(repository, path):
    data = git.get_contents_from_repo(repository.user.name, repository.name, path)
    repo = repositories.get_repository(repository.name)
    for element in data:
        try:
            content = Content(name=element.get('name'), type=element.get('type'), repository=repo)
            contents.insert_into_content(content)
            if element.get('type') == 'dir':
                mine_repository_content(repository, element.get('path'))
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
                print('file {}: {} - url {}'.format(content.name, file, url))
                files.insert_into_file(file)
                if fnmatch.fnmatch(file.name, '*.java'):
                    print('java file found')
                    mine_source_code(file, url.download_url)
        except AttributeError:
            # counters is not a dictionary, ignore and move on
            pass


def mine_source_code(file, download_url):
    data = git.get_source_from_content(download_url)
    source = data.content.decode('utf-8')
    lines = str.split(source, '\n')
    for line in lines:
        if line.__contains__('package'):
            package_name = line.split(' ')[1].replace(';', '')
            package = Package(name=package_name,
                              type='java',
                              file=file)
            print('package name found {}'.format(package.name))
            if packages.get_package(package.name) is None:
                packages.insert_into_package(package)
                print('package added: {}'.format(package_name))
        if line.__contains__('public class'):
            clazz_name = line.split(' ')[2].replace(';', '')
            print('Clazz name found {}'.format(line))
            clazz = Clazz(name=clazz_name,
                          type='java',
                          package=package)
            if clazzes.get_clazz(clazz_name) is None:
                clazzes.insert_into_class(clazz)
                print('class added: {}'.format(clazz_name))
        if (methodbot.is_method(line)):
            print('line {}'.format(line))
            accessor = methodbot.get_accessor(line)
            print('accessor {}'.format(accessor))
            type = methodbot.get_type(line)
            print('type {}'.format(type))
            method_name = methodbot.get_method_name(line)
            print('method name {}'.format(method_name))
            signature = methodbot.get_signature(line)
            print('signature {}'.format(signature))
            method = Method(origin=line.strip().replace('{',''),name=method_name,access=accessor,type=type,signature=signature,clazz=clazz)
            if methods.get_Method(method_name) is None:
                methods.insert_into_Method(method)
                print('Method added: {}'.format(method.name))
    return lines

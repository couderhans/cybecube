import cybecube.miner.mine as mining
import cybecube.scm.git as github
import cybecube.database.user as users
import cybecube.database.repository as repos
import cybecube.database.content as contents
import cybecube.database.file as files
import cybecube.database.package as packages
import cybecube.database.clazz as clazzes
import cybecube.database.method as methods

import sys
import getopt

from cybecube.database.user import User
from cybecube.database.repository import Repository
from sqlalchemy import null


def main(argv):
    global user
    global repo
    try:
        opts, args = getopt.getopt(argv, "c:d:m", ["create=", "delete=", "mine=", "repo=", "user="])
        print('opts {} and args {}'.format(opts, args))
    except getopt.GetoptError as optE:
        print('getopt error {}'.format(optE.args[0]))
    for opt, arg in opts:
        if opt == '--user':
            user = User(name=arg)
        if opt == '--repo':
            repository = github.get_repository_from_user(user.name,repository=arg)
            repo = repository
        if opt in ('-d', '--delete'):
            repos.delete_repository()
            contents.delete_content()
            files.delete_table_file()
            packages.delete_table_package()
            clazzes.delete_table_class()
            methods.delete_table_method()
        elif opt in ('-c', '--create'):
            repos.create_table_repository()
            contents.create_table_content()
            files.create_table_file()
            packages.create_table_package()
            clazzes.create_table_class()
            methods.create_table_method()
        elif opt in ('-m', '--mine'):
            if users.get_user(user.name) == null:
                users.insert_into_user(user)
            mining.mine_user_repositories(user)


if __name__ == '__main__':
    main(sys.argv[1:])

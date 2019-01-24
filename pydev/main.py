import cybecube.miner.mine as mining
import cybecube.database.user as users
import cybecube.database.repository as repos
import cybecube.database.content as contents
import cybecube.database.file as files
import cybecube.database.package as packages

import sys
import getopt

from cybecube.database.user import User
from sqlalchemy import null

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "c:d:s", ["create=", "delete=", "scan="])
        print('opts {} and args {}'.format(opts, args))
    except getopt.GetoptError as optE:
        print('getopt error {}'.format(optE.args[0]))
    for opt, arg in opts:
        if opt in ('-d', '--delete'):
            repos.delete_repository()
            contents.delete_content()
            files.delete_table_file()
            packages.delete_table_package()
        elif opt in ('-c', '--create'):
            repos.create_table_repository()
            contents.create_table_content()
            files.create_table_file()
            packages.create_table_package()
        elif opt in ('-s', '--scan'):
            user = User(name=arg)
            if users.get_user(user.name) == null:
                users.insert_into_user(user)
            mining.mine_user_repositories(user)


if __name__ == '__main__':
    main(sys.argv[1:])

import cybecube.mine as mining
import cybecube.database.repository as repos
import cybecube.database.content as content
import cybecube.database.file as file

import sys
import getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "c:d:s", ["create=", "delete=", "scan="])
        print('opts {} and args {}'.format(opts, args))
    except getopt.GetoptError as optE:
        print('getopt error {}'.format(optE.args[0]))
    for opt, arg in opts:
        if opt in ('-d', '--delete'):
            repos.delete_repositories()
            content.delete_content()
        elif opt in ('-c', '--create'):
            repos.create_table_repositories()
            content.create_table_content()
            file.create_table_file()
        elif opt in ('-s', '--scan'):
            mining.mine_user_repositories(arg)


if __name__ == '__main__':
    main(sys.argv[1:])

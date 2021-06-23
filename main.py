#!/usr/bin/env python2
import argparse
import json
import os
import sys

import server.FileService as FileService

def commandline_parser():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d', '--dir', default=os.path.join(os.getcwd()),
        help="working directory (default: dir)")

    parser.add_argument('-f', '--filename', help='File Name (default: filename)')

    return parser


def command_change_dir():

    dir_name = raw_input('Where we are going to: ')
    return FileService.change_dir(dir_name)

def command_get_files():

    quest1 = raw_input('We stay here (print : 1) or change location (print : 2): ')

    if quest1 == '1':
        dir_name = os.getcwd()

    elif quest1 == '2':
        dir_name = raw_input('Where we are going to: ')

    else:
        print('Ok, I decide to stay here : ' + os.getcwd())
        dir_name = os.getcwd()

    return FileService.get_files(dir_name)


def command_get_file_data():

    quest1 = raw_input('We stay here (print : 1) or change location (print : 2): ')

    if quest1 == '1':
        dir_name = os.getcwd()

    elif quest1 == '2':
        dir_name = raw_input('Where we are going to: ')

    else:
        print('Ok, I decide to stay here : ' + os.getcwd())
        dir_name = os.getcwd()

    file_name = raw_input('What file we are looking for: ')

    return FileService.get_file_data(dir_name, file_name)


def command_create_file():


    quest1 = raw_input('We stay here (print : 1) or change location (print : 2): ')

    if quest1 == '1':
        dir_name = os.getcwd()

    elif quest1 == '2':
        dir_name = raw_input('Where we are going to: ')

    else:
        print('Ok, I decide to stay here : ' + os.getcwd())
        dir_name = os.getcwd()

    file_name = raw_input('Enter new file name: ')
    file_format = raw_input('Enter new file extension: ')

    return FileService.create_file(dir_name, file_name, file_format)


def command_delete_file():

    quest3 = raw_input('We stay here (print : 1) or change location (print : 2): ')

    if quest3 == '1':
        dir_mame = os.getcwd()

    elif quest3 == '2':
        dir_mame = raw_input('Where we are going to: ')

    else:
        print('Ok, I decide to stay here : ' + os.getcwd())
        dir_mame = os.getcwd()

    file_mame = raw_input('What file we are looking for: ')

    return FileService.delete_file(dir_mame, file_mame)

def command_help():
    print("""The simple File manager 1.0
Available commands:
help  : show help
chdir : change working directory
list  : get list of files
create: create a file with content
get   : get a file data
delete: delete a file
exit  : exit from app
""")

def command_exit():
    sys.exit(0)


def main():

    parser  = commandline_parser()
    target_params = parser.parse_args(sys.argv[1:])
    path = target_params.dir
    FileService.change_dir(path)

    functions = {
        'help': command_help,
        'chdir': command_change_dir,
        'list': command_get_files,
        'create': command_create_file,
        'get': command_get_file_data,
        'delete': command_delete_file,
        'exit': command_exit,
    }

    command_help()

    while True:
        try:

            command = raw_input('Input command: ')

            def cmd_unknown():
                print("Unknown command: {}".format(command))

            result = functions.get(command, cmd_unknown)()


        except Exception as err:

            print(err)


if __name__ == '__main__':
    main()




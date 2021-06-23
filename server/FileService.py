#Task-02
import os, time, sys, stat
from pathlib import Path

def check_path(path):

    if path.__contains__('.') or path.__contains__(' '):
        return True

def change_dir(path, autocreate=True):

   if not check_path(path):

       if os.path.exists(path):

           if path <> os.getcwd():
               print('Current directory : ' + os.getcwd())
               print("""Target directory : """ + path)

           else:
               print("""We are still here : """ + path)

           os.chdir(path)

       else:

           if autocreate:

               os.makedirs(path)
               print("""Here are nour new location : """ + path)

           else:

               raise RuntimeError('Directory {} is not found'.format(path))
   else:

       raise ValueError('Check path format')


def get_files(path):

    os.chdir(path)
    print("""We are here : """ + path)

    files = os.listdir(path)

    i = 1

    file_info_table_header = "#    File Name    File type    File size (Kb)"
    print(file_info_table_header)

    for file in files:

        if os.path.isdir(file):
            wi = "dir"

        else:
            wi = "file"

        file_info = str(i) + "    " + file + "    " + wi + "    " +  str(Path(file).stat().st_size) + " Kb"

        print(file_info)

        i = i + 1


def get_file_data(path, filename):

    os.chdir(path)
    content = ''

    with open(filename, 'r') as f:
        content = content + f.read()

    print('File name : ' + os.path.basename(filename))
    print('Content: '+ content)
    print('Created: '+ time.ctime(os.path.getctime(filename)))
    print('Last modified: '+ time.ctime(os.path.getmtime(filename)))
    print('File size: '+  str(Path(filename).stat().st_size) + " Kb")


def create_file(path, filename, format):

    os.chdir(path)

    full_filename = filename + "." + format

    mode = 0o777 | stat.S_IRUSR

    if os.path.exists(full_filename):
        print('File ' + full_filename + ' already exists')
    else:
        os.mknod(full_filename, mode)
        print('File ' + path + '/' + full_filename + ' successfully created')

def delete_file(path, filename):

    os.chdir(path)

    os.remove(filename)

    print('File' + path + '/' + filename + ' successfully deleted.')

# coding=utf-8
import os
import pytest
import random
import string

from server import FileService

class Test_change_dir:

    def test_incorrect_type1(self):

        with pytest.raises(TypeError):

            FileService.change_dir(None)

    def test_incorrect_type2(self):

        with pytest.raises(TypeError):

            FileService.change_dir(int)

    def test_dot_dir(self):

        with pytest.raises(ValueError):

            FileService.change_dir(".")

    def test_incorrect_value2(self):

        with pytest.raises(ValueError):

            FileService.change_dir("..")

    def test_incorrect_value3(self):

        with pytest.raises(ValueError):

            FileService.change_dir('../something')

    def test_existing_dir_no_create(self):

        current_dir = os.getcwd()

        os.mkdir('ExistingDirectory')
        new_dir = os.getcwd()

        FileService.change_dir('ExistingDirectory', auto_create=False)

        assert os.path.basename(new_dir) == 'ExistingDirectory'

    def test_existing_dir_create(self):

        current_dir = os.getcwd()

        os.mkdir('ExistingDirectory')
        new_dir = os.getcwd()

        FileService.change_dir('ExistingDirectory', auto_create=True)

        assert os.path.basename(new_dir) == 'ExistingDirectory'


    def test_non_existing_dir_no_create(self):

        current_dir = os.getcwd()

        current_dir_name = os.path.basename(current_dir)

        list_of_dirs = os.listdir(current_dir)

        new_dir_name = current_dir_name.join((random.choice(string.ascii_letters)) for x in range(len(current_dir_name)))

        with pytest.raises(RuntimeError):

            i = 0

            for dirs in list_of_dirs:

                dir_name = os.path.basename(dirs)

                if new_dir_name != dir_name:

                    i = i + 1

            if i == 0:

                new_dir = os.path.join(current_dir, new_dir_name)
                FileService.change_dir(new_dir, autocreate=False)

                current_dir2 = os.getcwd()

                assert os.path.basename(current_dir2) != new_dir

    def test_non_existing_dir_create(self):

        current_dir = os.getcwd()

        current_dir_name = os.path.basename(current_dir)

        list_of_dirs = os.listdir(current_dir)

        new_dir_name = ''.join((random.choice(current_dir_name)) for x in range(len(current_dir_name)))

        i = 0

        for dirs in list_of_dirs:

            dir_name = os.path.basename(dirs)

            if new_dir_name != dir_name:

                i = i + 1

        if i == 0:

            new_dir = os.path.join(current_dir, new_dir_name)

            FileService.change_dir(new_dir, autocreate=True)

            current_dir2 = os.getcwd()

            assert os.path.basename(current_dir2) == new_dir

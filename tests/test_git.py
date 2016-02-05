import os
from shutil import unpack_archive
from tempfile import TemporaryDirectory
from pkg_resources import resource_filename

from sectool.services.git import push_working_directory, shallow_clone


def test_push_working_directory():
    original_directory = os.getcwd()

    with TemporaryDirectory() as new_cwd:
        with push_working_directory(new_cwd):
            assert os.path.realpath(os.getcwd()) == os.path.realpath(new_cwd)

        assert os.path.realpath(os.getcwd()) == os.path.realpath(original_directory)


def test_shallow_clone():
    with TemporaryDirectory() as tmpdir:
        archive_filename = resource_filename(__name__, 'data/test_repository.tar')
        unpack_archive(archive_filename, tmpdir)

        with shallow_clone(os.path.join(tmpdir, 'test_repository')) as working_copy_path:
            assert 'known_file' in os.listdir(working_copy_path)
            with open(os.path.join(working_copy_path, 'known_file')) as known_file:
                assert known_file.read() == 'Hello, World!\n'
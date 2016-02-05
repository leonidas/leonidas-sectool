from os import getcwd

from sectool.services.git import push_working_directory


def test_push_working_directory():
    original_directory = getcwd()

    with TemporaryDirectory() as new_cwd:
        with push_working_directory(new_cwd):
            assert getcwd() == new_cwd

        assert getcwd() == original_directory
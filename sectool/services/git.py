from contextlib import contextmanager
from os import getcwd, chdir
from tempfile import TemporaryDirectory
from subprocess import check_call


@contextmanager
def push_working_directory(new_workdir):
    old_workdir = getcwd()
    chdir(new_workdir)
    yield
    chdir(old_workdir)


@contextmanager
def shallow_clone(git_url):
    with TemporaryDirectory() as tmpdir:
        check_call(['git', 'clone', '--depth', '1', git_url, tmpdir])
        yield tmpdir
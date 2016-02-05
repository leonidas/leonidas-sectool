from contextlib import contextmanager
from os import getcwd, chdir
from tempfile import TemporaryDirectory
from subprocess import check_call
import logging


logger = logging.getLogger(__name__)


@contextmanager
def push_working_directory(new_workdir):
    old_workdir = getcwd()
    chdir(new_workdir)
    yield
    chdir(old_workdir)


@contextmanager
def shallow_clone(git_url):
    with TemporaryDirectory() as tmpdir:
        logger.debug('Shallow cloning %s into %s', git_url, tmpdir)
        check_call(['git', 'clone', '--depth', '1', git_url, tmpdir])
        logger.debug('Shallow clone complete')
        yield tmpdir
        logger.debug('Done with shallow working copy of %s', git_url)
import logging
from subprocess import check_call, CalledProcessError

from sectool.services.env import env
from sectool.services.github import GitHub
from sectool.services.git import shallow_clone, push_working_directory


logger = logging.getLogger(__name__)


def check_repo(github, repo_name):
    logger.info('Checking %s/%s', github.owner, repo_name)

    checkout_url = github.get_checkout_url(repo_name)

    with shallow_clone(checkout_url) as working_copy:
        with push_working_directory(working_copy):
            try:
                return check_call(['nsp', 'check'])
            except CalledProcessError as e:
                logger.error("nsp check returned non-zero exit status, see log for details")


def check_account(org=None, user=None):
    github = GitHub(org=org, user=user)

    logger.info('Checking %s %s', 'org' if org else 'user', org if org else user)

    for repo_name in github.get_repos_containing_file('package.json'):
        check_repo(github, repo_name)


def check_all():
    users = env('GITHUB_USERS').split(',')
    orgs = env('GITHUB_ORGS').split(',')

    logger.info('Running `nsp check` for users=%s, orgs=%s', ','.join(users), ','.join(orgs))

    for user in users:
        check_account(user=user)

    for org in orgs:
        check_account(org=org)


if __name__ == '__main__':
    import coloredlogs
    coloredlogs.install(level=logging.DEBUG if env('DEBUG') else logging.INFO)
    check_all()
from sectool.services.github import Github


def test_make_url():
    assert Github(user='japsu').make_owner_url('repos') == 'https://api.github.com/users/japsu/repos'
from sectool.services.github import GitHub


def test_make_url():
    assert GitHub(user='japsu').make_owner_url('repos') == 'https://api.github.com/users/japsu/repos'
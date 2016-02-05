from envparse import Env


env = Env(
    GITHUB_TOKEN=str,
    GITHUB_USERS=str,
    GITHUB_ORGS=str,
    DEBUG=dict(type=bool, default=False),
)

env.read_envfile()
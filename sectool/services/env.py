from envparse import Env


env = Env(
    GITHUB_TOKEN=str
)

env.read_envfile()
# Leonidas security tool

## What it does

* `sectool.npm_check_all` – runs `nsp check` on all `package.json` projects

## Getting started

### Installation

    python3 -m venv venv3-sectool
    source venv3-sectool/bin/activate

    git clone git@github.com:leonidas/leonidas-sectool
    cd leonidas-sectool
    pip install -U pip wheel setuptools
    pip install -r requirements.txt

### Configuration

Create a file called `.env` with the following parameters (also environment vars work):

    # Your GitHub API token
    GITHUB_TOKEN=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

    # Users and organizations whose repositories to work on, comma separated
    GITHUB_USERS=japsu
    GITHUB_ORGS=leonidas

### Running `npm_check_all`

    python -m sectool.npm_check_all
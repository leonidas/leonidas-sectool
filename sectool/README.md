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

## Development

### Running tests

    py.test

## License

    The MIT License (MIT)

    Copyright © 2016 Leonidas Oy Ltd

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
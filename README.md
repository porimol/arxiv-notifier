# Arxiv Notifier

Arxiv Notifier is a web application, where you can subscribe to get daily preprint scientific journal over an automated mailing system.

> You must have MongoDB installation in your local environment or you can use manage MongoDB service like [Cloud Database](https://www.mongodb.com/free-cloud-database).

## Table of Contents

* [Background](#background)
* [Project Run](#how-to-run-this-project)
* [Project Structure](#project-structure)
* [Features Released](#features-released)
* [Upcoming Features](#upcoming-features)
* [Maintainers](#maintainers)
* [How to become a contributor](#how-to-become-a-contributor)
* [License](#license)

## Background

> Will be added

### Python Version

> Minimum python version should have 3.7.x or upper

### How do I get set up?

If you would like to used `Virtualenv`
Install the virtualenv using this command(If you have not installed virtualenv yet.)

```python
$ [sudo] pip install virtualenv
```

Learn more to visit [Virtualenv](https://virtualenv.pypa.io), [User Guide](https://virtualenv.pypa.io/en/stable/userguide/)

Create a directory using the following command from your terminal
```ssh
$ [sudo] mkdir [project_name]
```

Switch to **[project_name]** directory
```ssh
$ cd [project_name]
```

#### git clone
```python
$ git clone git@github.com:porimol/arxiv-notifier.git .
```

Afterthen, create virtual env file by the following command from your terminal
```ssh
$ virtualenv -p python3 .venv
```

If you create virtual env file successfully on your development machine then run this command
```ssh
$ source .venv/bin/activate
```

Installing the requirements using the following commands
```python
$ pip install -r requirements.txt
```

## How to Run this project

```python
// Development
$ cd [project_name]

$ python main.py
or 
$ gunicorn --bind 0.0.0.0:5000 main:server --reload
```

Hit this url in your browser
http://0.0.0.0:5000

And, here you are ready to go.....

## Project Structure

```python
├── LICENSE
├── Procfile
├── README.md
├── Readme.txt
├── config.py
├── main.py
├── notifier
│   ├── __init__.py
│   ├── app
│   │   ├── __init__.py
│   │   ├── contact.py
│   │   ├── form.py
│   │   ├── landing.py
│   │   └── subscribe.py
│   ├── static
│   │   ├── .....
│   └── templates
│       ├── 404.html
│       ├── about.html
│       ├── contact.html
│       ├── contact_followup.html
│       ├── faq.html
│       ├── footer.html
│       ├── header.html
│       ├── landing.html
│       ├── layout.html
│       ├── notifier.html
│       ├── sidebar.html
│       ├── subscribe_success.html
│       └── why-us.html
└── requirements.txt
```

### Features Released

* [x] Subscribe to Arxiv Notifier
* [x] Contact Us

### Upcoming Features

* [ ] Arxive Scraper
* [ ] Citation Scraper
* [ ] Send email to every subscribers every night at at 00:00hrs
* [ ] Create developer document
* [ ] Dockerize
* [ ] and Based on users feedback

## Maintainers

* **[Porimol Chandro](https://github.com/porimol)**


### How to become a contributor

If you want to contribute to `Arxiv Notifier` and make it better, your help is very welcome.
You can make constructive, helpful bug reports, feature requests and the noblest of all contributions.
If like to contribute in a good way, then follow the following guidelines.

#### How to make a clean pull request

* Create a personal fork on Github.
* Clone the fork on your local machine.(Your remote repo on Github is called `origin`.)
* Add the original repository as a remote called `upstream`.
* If you created your fork a while ago be sure to pull upstream changes into your local repository.
* Create a new branch to work on! Branch from `dev`.
* Implement/fix your feature, comment your code.
* Follow `Arxiv Notifier`'s code style, including indentation(4 spaces).
* Write or adapt tests as needed.
* Add or change the documentation as needed.
* Push your branch to your fork on Github, the remote `origin`.
* From your fork open a pull request to the `dev` branch.
* Once the pull request is approved and merged, please pull the changes from `upstream` to your local repo and delete your extra branch(es).

## License

### [The MIT License](LICENSE.txt)

Copyright (c) 2020, Porimol Chandro porimolchandroroy@gmail.com

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
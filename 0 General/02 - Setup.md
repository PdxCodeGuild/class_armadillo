


# Setup

This document contains an overview for the software setup for the course. Please try to get as much done as possible before the course starts, but we'll also go over the setup on the first day of class to ensure everyone's up to speed.

- [Setup](#setup)
  - [1 Pick a CLI](#1-pick-a-cli)
      - [Opening the CLI](#opening-the-cli)
      - [Common CLI Commands](#common-cli-commands)
  - [2 Install the latest version of Python (3.8.2)](#2-install-the-latest-version-of-python-382)
  - [2 Install Git and make a [GitHub](https://github.com/) account](#2-install-git-and-make-a-github-account)
  - [3 Install an Editor](#3-install-an-editor)
    - [Visual Studio Code](#visual-studio-code)
      - [Shortcuts](#shortcuts)
      - [Recommended Extensions](#recommended-extensions)
    - [Atom](#atom)
  - [4 Install Slack](#4-install-slack)
  - [5 Pick a Browser](#5-pick-a-browser)
  - [6 Zoom](#6-zoom)
  - [7 A Full Test](#7-a-full-test)



## 1 Pick a CLI

CLI stands for 'command-line interface', and it was the only way to use a computer before the development of GUIs 'graphical user interface'. It's still used to perform many computer operations that go 'under the hood'.

#### Opening the CLI

In OS X, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In Windows, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python, but there's no color differentiation, and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/). Another option for Windows is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In Linux, you can open a terminal with `Ctrl + Alt + T`.

Visual Studio Code also has a terminal built in, which you can access with `ctrl+j` or using the main menu `Terminal -> New Terminal`.

#### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directoryname>` change directory
    - `cd ..` will bring you into the parent directory
    - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder 
- `rmdir <foldername>` removes a folder
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file
- `cp filename1 filename2` copies a file
- `up-arrow` will bring up the last command entered
- `tab` will attempt to autocomplete whatever you're typing
    - try `cd D` + `tab` + `tab`
- `ctrl+c` kill currently running process
- `touch file.txt` creates a file
- `echo "Hello World!" >> hello_world.txt` will create a file with the given contents


## 2 Install the latest version of [Python (3.8.2)](https://www.python.org/downloads/)

Python is a programming language, and we'll be using the python interpreter in order to run our code. We'll write our source code in text files with the extension `.py` and run the code by running `python file.py` in our terminals. You can find more info in the [official docs](https://docs.python.org/3/using/cmdline.html).


- `python` start the interactive interpreter
- `python <file>` execute the python source code in the given file
- `python --help` print out all command-line options
- `python --version` show which version of python you're using

If you're on windows be sure to select "add python to path" when installing. You can check whether the installation was successful by running `python --version` or `python3 --version` or `py --version`.

## 2 Install [Git](https://git-scm.com/downloads) and make a [GitHub](https://github.com/) account

Git is a version control system, it keeps tracks of changes to files to allow developers to undo changes and collaborate on projects. You can check whether the installation was successful by running `git` in a terminal which should show a list of commands.

GitHub is a hosting service for Git repositories. Our class will have a repository hosted there we'll collaborate on. It also serves as a programmer's portfolio, potential employers can see your activity and code you commit, so make sure you commit changes regularly and only commit clean, working code.

## 3 Install an Editor

[Visual Studio Code](https://code.visualstudio.com/) is the recommended editor, but there's also [Atom](https://atom.io/) and [PyCharm](https://www.jetbrains.com/pycharm/).

### [Visual Studio Code](https://code.visualstudio.com/)

- [editing guide](https://code.visualstudio.com/docs/editor/codebasics)
- [shortcut cheat sheet](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf), and [this list](https://medium.com/better-programming/20-vs-code-shortcuts-for-fast-coding-cheatsheet-10b0e72fd5d)
- [Guide to Python](https://code.visualstudio.com/docs/python/python-tutorial)
- [Guide to Flask](https://code.visualstudio.com/docs/python/tutorial-flask)
- [Guide to Django](https://code.visualstudio.com/docs/python/tutorial-django).

#### Shortcuts

- `ctrl + /` toggle comment
- `tab` indent a block of text, `shift + tab` to unindent
- `alt + up/down` move line up or down
- `ctrl + d` select matching text, useful for renaming variables, `ctrl + u` to unselect

- You can change the color scheme easily `File -> Preferences -> Color Theme`
- If you don't like the suggestions popping up when you type, you can turn them off `File -> Preferences -> Settings -> Text Editor -> Suggestions -> Suggest on Trigger Characters`. You can still open suggestions manually with `ctrl + space`.

#### Recommended Extensions

- [Markdown All-in-One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)


### [Atom](https://atom.io/)

You can find a list of shortcuts [here](https://github.com/nwinkler/atom-keyboard-shortcuts)

- `ctrl + /` toggle comment
- `tab` indent a block of text, `shift + tab` to unindent
- `ctrl + d` select matching text, useful for renaming variables, `ctrl + u` to unselect
- `ctrl + up/down` move a line of text up and down
- `ctrl + shift/cmd + d` duplicate a line of text
- `tab` for autocomplete, e.g. type "html" and hit `tab` to get a stock html page

You install and remove packages by going to `File -> Settings -> Packages/Install`.

- [Beautify](https://atom.io/packages/atom-beautify) will make your code pretty.
- [Emmet](https://atom.io/packages/emmet) gives more advanced autocomplete features.
- [Teletype](https://teletype.atom.io/) for collaborating with others.


## 4 Install [Slack](https://slack.com/)

Slack is an instant messaging service we'll use to communicate. If you send me an email `matthew@pdxcodeguild.com` I can send you an invite to PDX Code Guild's Slack. You can use Slack in a browser, but it can also be installed as a desktop and mobile app.

- Desktop: [Windows](https://slack.com/downloads/windows), [Mac](https://slack.com/downloads/mac), [Linux](https://slack.com/downloads/linux)
- Mobile: [Android](https://slack.com/downloads/android), [iOS](https://slack.com/downloads/ios)


## 5 Pick a Browser

[Chrome](https://www.google.com/chrome/), [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [Safari](https://www.apple.com/safari/) are all excellent choices. When developing on the front-end (HTML, CSS, & JavaScript) it's best to test on the most popular browsers, you can find statistics on popularity [here](https://en.wikipedia.org/wiki/Usage_share_of_web_browsers#Summary_tables).


## 6 Zoom

[Zoom](https://zoom.us/) is a video chatting service we'll be using to hold class online. I'll post a link to each day's meeting in our Slack channel. Students are required to have their video on the majority of the time to ensure they're engaged, but if you're concerned about privacy you can set a "virtual background" by clicking the arrow next to the video icon and selecting "choose virtual background". You can find some free backgrounds [here](https://www.shutterstock.com/discover/free-virtual-backgrounds). You're also welcome to mute yourself if you're not talking to cut down on background noise. Zoom also allows people to share their screens. If the top panel is getting in your way while sharing your screen, click the ellipses (...) and select "hide floating media controls".


## 7 A Full Test

1. Go to our class repository on github and copy the url.
2. Open a terminal and run `git clone <repo url>` and `cd <repo folder>`. This will create a local copy of the class repository.
3. Open the folder in your editor
4. Edit create a folder with your name in the `Code` folder.
5. Inside that folder create `hello_world.py`, write `print('hello world!')` inside the file and save it
6. In your terminal `cd` into your personal folder
7. Run `python hello_world.py` you should see "hello world!"
8. Use the GUI or terminal to commit the change and push it to the repository on GitHub
  1. `git pull`
  2. `git add hello_world.py`
  3. `git commit -m "added hello world"`
  4. `git push`
9. Go to the class repository on GitHub and you should see your file


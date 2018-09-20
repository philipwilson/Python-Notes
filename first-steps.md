## Install the Anaconda Python 3.6 environment on your Macbook

Macbooks ship with a version of python already installed.  Unfortunately it's version 2 python.  We're following the MIT 6.0001 course which uses python version 3, packaged with some other useful tools and libraries in the Anaconda distribution.  Install as follows:  


1. Download the Python 3.6 64-bit Graphical Installer package from [anaconda.com](https://www.anaconda.com/download/#macos)
2. Run the installer package from your downloads directory.  You will be given the option to install vscode, Microsoft's IDE.  This is entirely optional, I'll discuss IDEs below.
3. After the installer package finishes, you should find an app called Anaconda-Navigator which you can launch from "Launchpad" or your Applications folder.  From Navigator you can launch Spyder, the IDE that ships with Anaconda.
4. You should also be able to run the upgraded python from the command line.  If you open a terminal and type 'python3' you should get an interactive session `>>>` prompt, preceeded by text saying it's the Anaconda, Inc. version.

### A note on editors and IDEs

As a programmer you will spend a significant part of your day creating, reading, editing, building, testing, and debugging programs.  Many software tools exist to help with these activities, including single-purpose utilities and large integrated environments called IDEs.
* If you already know how to use a text editor like `vim` or `emacs`, that's great, otherwise I recommend biting the bullet and learning basic `vim` usage; `vim` is pre-installed on normal MacOS and Linux systems, so it's always available.
* We won't rely on the features of any particular IDE in our work, but you are welcome to experiment.  There are dozens available, I'll mention 3:
    * PyCharm [download community edition here](https://www.jetbrains.com/pycharm/download/#section=mac) - This is a popular IDE at The Hut Group.
    * Visual Studio Code [download here](https://code.visualstudio.com/download) or from within Anaconda-Navigator - This is Microsoft's IDE, recently made available for MacOS and Linux.
    * Spyder - This is installed with the Anaconda Python distribution, and may be run from Anaconda-Navigator.  The lecturers in the MIT 6.0001 Open Courseware videos use Spyder in their lectures.
    * Intelligent developers disagree with religious fervor about which of these is best.
    * Personally I use `emacs`, to near universal derision at THG.  See: [Editor Wars.](https://en.wikipedia.org/wiki/Editor_war)





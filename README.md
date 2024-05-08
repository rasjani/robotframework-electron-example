Using Robot Framework and SeleniumLibrary to automate Electron apps
===================================================================

Electron apps are essentially just web applications running inside bundled chrome/chromium browsers.

I made this example based on discussion on this discussion in (rf forums)[https://forum.robotframework.org/t/not-recommended-to-use-robot-framework-with-electron-app/7211]

Everything in this repository is not automated and point of the repo is to highlight what should be done.


## Setup

1. Find out the exact version of your Electron.
2. Download appropriate chromedriver from Electron [releases](https://github.com/electron/electron/releases) page. eg, locate the release, expand assets and pick the correct os/arch version.
3. Extract the downloaded chromedriver zip and extract it somewhere in your PATH. For example, if you are using venv, you can place all the files into your venv's bin (Scripts on windows) directory.
4. If you are running on Mac, you need to notarize the binaries but thats not covered here.
5. Edit vars.py so that both, your Electron application and chromedriver is referenced correctly.

And then run with  `robot electron_test.robot`


## Notes

If ChromeService is not passed to `Create Webdriver`keyword, somewhat recently added `selenium-manager` hangs your robotframework execution. Using older selenium like 4.0.9 does not have this issue and passing `service` is optional.

At the time of writing repository, following components where used:

* python 3.12
* robotframework 7.0
* robotframework-seleniumlibrary 6.3.0
* selenium 4.2.0


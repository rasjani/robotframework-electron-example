*** Settings ***
Library     SeleniumLibrary
Variables   vars.py
Suite Teardown   Close All Browsers
Suite Setup      Open Electron Application


*** Keywords ***
Open Electron Application
  [Documentation]  Open's your electron application by providing browser binary via
  ...  ${signal_electron} and chromedriver binary via ${signal_service}
  ...  see vars.py for more details.
  Create Webdriver    Chrome    options=${signal_electron}    service=${signal_service}

*** Test Cases ***
Initial Setup
  [Documentation]  Does nothing except takes a screenshot of application opened by Suite Setup
  Capture Page Screenshot

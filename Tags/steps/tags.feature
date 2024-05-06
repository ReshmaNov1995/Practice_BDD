@Regression
Feature:The login page test case
@unit
Scenario:Positive test cases
  Given lims link
  When enter the user name
  When enter the password
  Then click on the login button

@smoke
Scenario:Test cases for passing parameter
  Given lims1 http://62.171.183.83:9092/QuaLISWeb/#/login test
  When enter1 the cdolman name
  When enter1 the 123
  Then click1 on the login button
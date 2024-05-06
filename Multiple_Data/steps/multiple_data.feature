Feature:The login page test case

  Scenario Outline: Negative test cases for <user> and <password>
    Given lims11 http://62.171.183.83:9092/QuaLISWeb/#/login test
    When enter11 the <user> name
    When enter11 the <password> name1
    Then click11 on the login butt-on

    Examples:
      | user    | password |
      | cdolman | 123      |
      | cdolman | 123      |
      | cdolman | 123      |

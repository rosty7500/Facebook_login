Project name ==> Facebook login

Framework : PYTEST



Folders:

Pages ==> Locators.py , functions.py
test ==> report.html , login-data-import.csv , test_executable_file.py

Other files:
.gitignore
README.md
requirements.txt

Executable file ==> test_executable_file.py

report.html ==> consists of testrun passes/fails

Execution command ==>
pytest --html=report.html : Which will generate a report about the test pass/fail
OR
py.test test_executable.py -s

NOTE:
Import the requirements.txt using pip install -r requirements.txt
All tests are independent of each other.
Uploading on GITHUB, Please clone it on your local and execute the test_executable_file.py in test folder
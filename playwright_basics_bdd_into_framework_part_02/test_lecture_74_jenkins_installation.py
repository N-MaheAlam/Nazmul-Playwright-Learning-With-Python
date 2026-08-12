"""

 ========================= LECTURE 74 - Jenkins Installation ===========================


Jenkins:

May in your system you might have jenkins already installed. If not you can go to the below website
"https://www.jenkins.io/download/lts/macos/" and follow the steps

If you already have it then, go to the main terminal from your Mac
and do
=====>  " cd .jenkins"

it will take you to the jenkins folder and delete everything ( you can keep your old jobs and place it once
the installation is done.
Now, download the jenkins java jar file from the below website:
"https://www.jenkins.io/download/"
Now, from terminal go to the folder (normally all the downloads are in download file and open
terminal from there)
Write in download folder terminal
 ====>  " java jar jenkins_file_name.jar --httpPort=8080 "
 it will run and will give you a password like below
 ======> "  [LF]> Please use the following password to proceed to installation:
            [LF]>
            [LF]> 9424d1cb506944a98e4a7d44f3f64fcd "

Now from your browser go to
=======> "http://localhost:8080/"
give the password that you get and provide "necessary plugin install "
Then, give your credentials to signup, and you are good to go

======================== LECTURE 75 - Jenkins Project creation ===========================

From jenkin log in page
=>  Click " New Item"

Then give the project name and choose

=>  "Freestyle Project"

as we might change somthing inside the
project

Then, you need to provide path
If the project is on GitHub we can simply pass the url

But the project is on our local system
so select
=> " Advanced"
Then
=>  "Custom project"
go the project and give the absolute path of the project

Scroll down adn you will see "Add build step"
Then select 'Execute Shell'
It will pop up a text box and write your CLI command like for to run all tests or only smoke test
In command box, what I will do, I will provide the following command for now

"pytest --browser_name chrome -n 3 --tracing on --html=report_from_jenkins.html"

Now,,,,,,,,,,,,,,,,,,,,,,
If we want to run with parameter for example, the above command If I want to set my browser from
jenkins, I can create parameter by clicking
=====>  "This project is parameterised" and
provide
=======>    "Choice parameter
For example in Choice parameter I will give "Name"  as "browser" and in
"Choices" section, I will provide each line with name such as
"chrome
firefox
Microsoft Edge"

Then , in " Add build step" I will use like below

======> pytest --browser_name "$browser" -n 3 --tracing on --html=report_from_jenkins.html"

Now, When I will build the project I will see "Build with Parameters"
Click on that and select the option whatever I like, If I choose "chrome" all my tests will run in
Chrome browser
"""
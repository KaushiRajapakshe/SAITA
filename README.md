# 2020-110

**SMART ARTIFICIAL INTELLIGENT TROUBLESHOOTING AGENT (SAITA)**

**2020_110**

Supervisor Name: Mr. Udara Samarathunga
Co-supervisor Name: Ms. Thilmi Anuththara

**Team Details**

D.I.K. Rajapakshe - IT16178700 <br />
M.P.P. Shamil - IT17018760 <br />
P.M.C.P. Paththinisekara - IT17056212 <br />
S.K. Liyanage - IT17152938 <br />

**Main Objectives**

There are few objectives that was achieved through the completion of this study. Primarily what this research study is trying to achieve is implementing a troubleshooting system which will solve windows operating system related issues using artificial intelligence and machine learning which will successfully provide solution to regular user and industry level troubleshooting issues.

Simply, main objective here is to create an artificial intelligent troubleshooting assistant program for windows operating system. In this research we proposed a system named Smart Artificial Intelligent Troubleshooting Agent (SAITA), which is mainly designed to troubleshoot Windows Operating System (OS) specific issues. Furthermore, this study identifies the limitations of prevailing troubleshooting software and introduces Artificial Intelligence (AI) based solution. This solution can be decomposed into four primary areas of troubleshooting namely, primary service-specific issues, fundamental (basic) user issues, pre-selected application-specific issues, and software installation environment setup troubleshooting.

**Main Research questions**

How to solve Windows operating system related issues using AI troubleshooter?

**Individual research question**

-	IT16178700 <br />
How to solve pre-selected application errors using OS troubleshooter using ontology.?
-	IT17018760 <br />
How to solve abundant service-specific issues using machine learning.?
-	IT17056212 <br />
How to solving fundamental Operating System issues using shell scripts and NLG?
-	IT17152938 <br />
How to perform environment setup using the dependency resolving?

**Individual Objectives**

This study will be divided in to 4 specific sub objectives which will be carry out the separate by the research team members. Each of those sub objectives is an essential aspect of the project which are specifically designed to achieve a specific part of the troubleshooting field of Windows OS. Those sub objectives are the main components in the software architecture. Determine the optimum solution to sort out application (pre-selected) related issues.
1. Troubleshoot application related issues.
2. Troubleshoot abundant services specific issues.
3. Troubleshoot fundamental OS specific issues.
4. Perform environment setup by analyzing software.

**Troubleshoot application related issues**

This sub objective handle how to solve pre-selected applications errors using OS troubleshooter. So, it essentially handles the part of getting the issue from the user and identifying the issue then use the knowledge base to create a solution for the issue. Following are the objectives that have to be completed in order to have the full functionality of this component.

-	Identify typical symposium and problem related to the pre-selected application.
-	User can easily fixed issue when running the applications.
-	At a minimum, SAITA able to help them narrow down the problem by executing the solution.
-	This technique can resolve the situation so one can continue working without any issues.

**Troubleshoot abundant services specific issues**

Developing a machine learning based algorithm to determine the most appropriate route of repairing the service by using models which were trained before. All the routes are not pre train paths. It trains by user’s feedback and it is real time learning algorithm. That gets the most appropriate path by the previous trainings. If there are no any training paths at the first time it takes the shortest path to execute. If there is a path with pre trained, it takes the highest reward path to execute. Customized Markov decision making technique is used to this system to find the most appropriate paths by start and end points. Start and end points means there are lots of nodes which means the PowerShell codes that used to execute and solve the issues. The final objective of the solving abundant issues in SAITA system is to troubleshoot the issue which the user had.

**Troubleshoot fundamental OS specific issues**

Specifically, the objective of this research component to create an implement a troubleshooting module that will solve fundamental Windows operating system specific issues. In order to develop a system which, enable the user to effectively interact and perform computer troubleshooting effectively following sub objectives was achieved,
-	Implementing a Decision-making process for identifying the windows issue using suitable machine learning algorithms. In this case the decision tree classification algorithm was used to identify the user issues from the user inputs such as error details.
-	Implementing a Decision-making process categorizing the solution as a technical solution or a non-technical NLG solution based on the user replies. This was also achieved through a decision tree algorithm.
-	Implement a mechanism to create sentences for non-technical or user side issues by utilizing the data from the solution database. This objective was achieved through a Markov chain text generation model.
-	Create a solution machine learning based solution ranking mechanism. This step was implemented using the Logistic regression algorithm.

**Software installation environment setup**

Specifically, SAITA this part tries to create algorithms base dependencies management system and rule base environment variables.
-	Get the Software list or software with the version from the user.
-	Create dependencies hierarchy.
-	Analyze risk and get user conformations.
-	Create a Windows Restore point.
-	Install software.
-	Add environment variables.

**Modules and the system architecture**

The main 4 components that are separated in to 4 members are the main modules of the projects these 4 modules handle different troubleshooting areas. Therefore, the individual modules connect to main chat platform to work as an entire system. Troubleshoot application related issues data are stored in a remote Knowledge base, Software installation environment setup data stored in a remote database and storage. However, fundamental OS specific issues component data and services specific issues data are stored locally in order to troubleshoot network issues.

**Steps to Execute the individual code**

IT16178700- <br />
Software- PyCharm, Fuseki Server, Anaconda <br />
Steps-
-	Download the Project.
-	Run the Fuseki Server
-	Upload saita.owl file to server.
-	Open the IT16178700 Project in PyCharm.
-	Create a ‘Conda’ environment for the IT16178700 project.
-	Install all the imported dependencies.
-	Run the Project.
    
IT17018760 - <br />
Software- PyCharm, Xampp(MySQL), Anaconda <br />
Steps- 
-	Download the Project.
-	Import IT17018760.sql to MySQL server
-	Open the IT17018760 Project in PyCharm.
-	Create a ‘Conda’ environment for the IT17018760 project.
-	Install all the imported dependencies.
-	Run the Project.

IT17056212- <br />
Software- PyCharm, Xampp(MySQL), Anaconda <br />
Steps- 
-	Download the Project.
-	Import it17056212.sql to MySQL server
-	Open the IT17056212 Project in PyCharm.
-	Create a ‘Conda’ environment for the IT17056212 project.
-	Install all the imported dependencies.
-	Run the Project.
    
IT17152938- <br />
Software- PyCharm, MySQL, Apache, Anaconda <br />
Steps- 
-	Download the Project.
-	Import it17152938.sql to MySQL server
-	Open the IT17152938 Project in PyCharm.
-	Create a ‘Conda’ environment for the IT17152938 project.
-	Install all the imported dependencies.
-	Run the Project.
However, the software installation part will not be executed until necessary software added to the storage.

**Dependencies**

IT16178700 Project branch – <br />
-	Libraries-
-	    • win32api
        • winapps
        • subprocess
        • sys
        • os
        • fnmatch
        • tk
        • tkinter
        • wordnet
        • Synset
        • copy
        • re
        • requests
        • ImageTk
        • Image
        • datetime
        • time
        • calendar
        
IT17018760 Project branch –
-	Libraries- 
-       • difflib
        • win32api
        • mysql
        • tkinter
        • time
        • subprocess
        • re
        • operator
        • csv
        • collections
        • pandas
        
IT17056212 Project branch –
-	Libraries- 
-       • tkinter
        • subprocess
        • win32api
        • csv
        • difflib
        • random
        • datetime
        • time
        • PIL
        • pymysql
        • pandas
        • sklearn.linear_model 
        • pickle
        • json
        • win32com
        • sys
        • collections
        • language_check

IT17152938 Project branch –
-	Libraries- 
-       • winapps
        • win32com
        • threading
        • tkinter
        • platform
        • subprocess
        • ctypes
        • zipfile
        • requests
        • pathlib
        • os
        • mysql
        • PIL
        • win32api

Above libraries has to be installed in each project in order for them to run correctly.

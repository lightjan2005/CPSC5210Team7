# CPSC5210Team7
This is a project to write unit test to a basketball program
The game is simply a text-based basketball simulation. There are numbers associated with different shot types and defense formations. The user enters one of these numbers when prompted for a shot type or defense formation. This allows the game to progress such that the set probabilities are used to determine the outcome of the user having chosen a certain shot type. This project is in Python.

There are four types of shots:

Long Jump Shot (30ft)

Short Jump Shot (15ft)

Lay Up

Set Shot


Both teams use the same defense, but you may call it:

Enter (6): Press

Enter (6.5): Man-to-man

Enter (7): Zone

Enter (7.5): None


To change defense, type "0" as your next shot.


How to run the tests in PyCharm-

First, in order to see the code coverage in pycharm, you have to download pycharm professional. Then you import our project through our github or our zipfile. Open our file. The interpreter we are using is Python 3.8. You also must install “unittest” and “coverage” package in order to compile the unit tests. Finally, you click on compile at the top right corner. The results of the testing will be shown in the console.  

Steps to run the tests in VSCode-

1. After cloning the repository, to build and run the tests in python, we had to install the pytest module in VSCode. 

2. For parameterized tests, install parameterized module 

   > pip install parameterized 

3. To run the tests, we can run them from the command line which gives a summary of tests that passed/failed 

   > pytest test_basketball.py 

4. To get code coverage run ‘Analyze Code Coverage For All Tests’ from Test dropdown in VSCode. 



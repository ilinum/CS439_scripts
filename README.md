# CS439_scripts
Scripts written for CS 439 (Operating Systems) class

##Race Condition
Currently the only script done.
It runs a particular tests a lot of times in order to find a race condition

###How to use
* Copy the file into src/vm/build directory
* Run python race_condition.py [name_of_test] [num_runs]
* If num_runs is not specified, it runs the test 50 times
* Output is printed to the console and also stored in race_condition_[name_of_test].txt file

####Examples:
* python race_condition.py args-none 10
* python race_condition pt-grow-stack

###TODO:
* If passed a particular argument exit on first failed test
* Implement error checking for shell commands
* Allow user to select the name of output file
* Allow quiet execution (with no output to console)

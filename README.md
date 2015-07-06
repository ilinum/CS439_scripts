# CS439_scripts
Scripts written for CS 439 (Operating Systems) class for testing Pintos Operating System for Project 3 (VM)

##Race Condition
Runs a particular tests a lot of times in order to find a race condition

###How to use:
* Copy the file into src/vm/build directory
* Run python race_condition.py [name_of_test] [num_runs]
* If num_runs is not specified, it runs the test 50 times
* Output is printed to the console and also stored in race_condition_[name_of_test].txt file

####Examples:
* python race_condition.py args-none 10
* python race_condition pt-grow-stack

###TODO:
* OUTPUT FILES ARE A COMPLETE MESS
* If passed a particular argument exit on first failed test
* Implement error checking for shell commands
* Allow user to select the name of output file
* Allow quiet execution (with no output to console)


##All Race Condition
Runs race_condition.py on all tests in test_names.txt
test_names.txt contains all tests for Project 3 (Virtual Memory) except for the extra credit tests

###How to use:
* Copy all files from this repo into src/vm/build directory
* Run python run_all_race_condition.py
* Script takes a while to run, so best to use tmux:
  * ssh onto a lab machine
  * Run tmux
  * Run python run_all_race_condition.py > output_file.txt &
  * Close the window
  * In a few hours ssh onto a lab machine and run tmux attach

###TODO:
* Allow specifying number of runs for each tests (current default is 50)
* Run in tmux by default

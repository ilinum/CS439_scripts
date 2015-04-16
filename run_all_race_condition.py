import sys
import os.path
from subprocess import Popen, PIPE

DEFAULT_RUNS = 50
working_tests = 0
not_working = 0
OUTPUT_FILE = "all_race_condition_out.txt"
tests_ran = DEFAULT_RUNS # TODO (Stas): allow specifying num runs

def run_command (command):
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	# TODO(Stas): implement error checking. Hard to differentiate between 
	# compile warnings and compile errors
	return out

# TODO(Stas): do something about buffering
output = open(OUTPUT_FILE, 'w', 0) 
# output.write("Test: " + test_name + "\nRuns: " + str(tests_to_run) + "\n")
tests = open("test_names.txt").readlines()

run_command (["make", "clean"])
run_command (["make"])
start_message = "Running all of the tests " + str(tests_ran) + " times."
output.write(start_message + "\n")
print start_message
print "Full output can be found in " + OUTPUT_FILE

for t in tests:
	t = t[:-1].lower()
	command = ['python', 'race_condition.py', t, str(tests_ran)]
	# print command
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	print "Test: " + t
	output.write("\n" + str(t) + "\n")
	if len (err) != 0:
		print "something went wrong. Error message: "
		print err
	if "Tests passed: " + str(tests_ran) in out:
		working_tests += 1
		test_write = "All " + str(tests_ran) +" tests passed for " + str(t) + "\n"
		test_write += "It is *probably* working\n"
		output.write(test_write)
	else:
		not_working += 1
		test_write = "Some tests failed for " + str(t) + "\n"
		test_write += "Output: " + "\n"
		test_write += out + "\n"
		output.write(test_write)
	print test_write

results = "\nTests working: " + str(working_tests) + "\n"
results += "Tests failing: " + str(not_working) + "\n"
print results
output.write(results)
output.close()

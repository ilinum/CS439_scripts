import sys
import os.path
from subprocess import Popen, PIPE

DEFAULT_RUNS = 50
arg_length = len (sys.argv)
tests_passed = 0
tests_failed = 0
if (arg_length < 2 or arg_length > 3):
	print "Wrong number of arguments!"
	print 'Argument List provided:', str(sys.argv)
	exit(0)
test_name = sys.argv[1]
#now try to guess if it's userprog or vm
if (os.path.isfile('../../tests/vm/' + test_name + '.ck')):
	path_to_test = "tests/vm/" + test_name
else:
	if not os.path.isfile('../../tests/userprog/' + test_name + '.ck'):
		print "test not found"
		exit(0)
	path_to_test = "tests/userprog/" + test_name

if (arg_length == 3):
	tests_to_run = sys.argv[2]
else:
	print "Number of tests not provided. Set to default."
	tests_to_run = DEFAULT_RUNS
print "Test " + path_to_test + " will be ran " + str(tests_to_run) + " times"

def run_command (command):
	p = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	out, err = p.communicate()
	# TODO(Stas): implement error checking. Hard to differentiate between 
	# compile warnings and compile errors
	return out

# TODO(Stas): do something about buffering
output = open("race_condition_" + test_name + ".txt", 'w', 0) 
output.write("Test: " + test_name + "\nRuns: " + str(tests_to_run) + "\n")

for i in range(int(tests_to_run)):
	try:
		os.remove(path_to_test + ".result")
		os.remove(path_to_test + ".output")
	except:
		pass
	print "Test number " + str(i + 1)
	test_out = run_command (["make", path_to_test + ".result"])
	# done testing
	passed = run_command (["grep", "-c", "PASS", path_to_test + ".result"])
	res_file = open (path_to_test + ".result")
	# did i pass?
	if (int(passed)) > 0:
		tests_passed += 1
		res = res_file.read()
		output.write(res)
		print ('\033[92m' + "passed" + '\033[0m')
	else:
		tests_failed += 1
		res = res_file.readlines()
		print ('\033[91m' + "FAILED" + '\033[0m')
		print '\n' + "".join(res[1:]) + "\n"
		output.write("".join(res) + "\n")

results = "Tests passed: " + str(tests_passed) + "\n"
results += "Tests failed: " + str(tests_failed) + "\n"
results += "Failed: " + str(float(tests_failed)/tests_to_run) + "%\n"
print results
output.write(results)
output.close()

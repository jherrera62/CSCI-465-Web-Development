#!/usr/bin/python
import sys
import os
import filecmp
from os import listdir
from os.path import isfile, join

def create_dir(dir):
    result = True
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)
    except OSError:
        print("Could not create directory {}!".format(dir))
        result = false
    return result

def get_file_list(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]

def run_test(test_name):
    input_file = "tests/{}.in".format(test_name)
    output_file = "results/{}.out".format(test_name)
    expected_output_file = "tests/{}.out".format(test_name)
    command = "python filter.py < {} | python sort.py | python uniq.py | python pig_latin.py > {}".format(input_file, output_file)
    print(command)
    os.system(command)
    print("Comparing {} {}...".format(output_file, expected_output_file))
    if not filecmp.cmp(output_file, expected_output_file, shallow=False):
        print("Test {} FAILED!".format(test_name))
    else:
        print("Test {} PASSED".format(test_name))

if create_dir("results"):
    file_list = get_file_list("tests")
    for filename in file_list:
        if ".in" in filename:
            test_name = filename.strip(".in").strip("_")
            run_test(test_name)

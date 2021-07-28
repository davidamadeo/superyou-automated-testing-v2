#!/bin/bash

for py_file in $(find testcase_homepage -name *.py)
do
    python $py_file
done
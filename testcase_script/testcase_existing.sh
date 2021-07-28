#!/bin/bash

for py_file in $(find testcase_existing -name *.py)
do
    python $py_file
done
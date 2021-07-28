#!/bin/bash

for py_file in $(find testcase_form -name *.py)
do
    python $py_file
done
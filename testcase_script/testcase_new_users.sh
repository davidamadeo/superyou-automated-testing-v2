#!/bin/bash

for py_file in $(find testcase_new_users -name *.py)
do
    python $py_file
done
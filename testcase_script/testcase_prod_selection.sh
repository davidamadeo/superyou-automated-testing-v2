#!/bin/bash

for py_file in $(find testcase_prod_selection -name *.py)
do
    python $py_file
done
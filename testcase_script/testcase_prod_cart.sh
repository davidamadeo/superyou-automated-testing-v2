#!/bin/bash

for py_file in $(find testcase_prod_cart -name *.py)
do
    python $py_file
done
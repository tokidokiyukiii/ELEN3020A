#!/usr/bin/env python3
''' Test suite for getbest.py '''

from io import StringIO
import sys
import os

# Importing the functions from getbest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from getbest import getCols, findTop

def test_getCols_basic():
    ''' Testing if getCols finds the right columns '''
    print("Testing getCols")
    csv_header = "Course, Student Number, Mark, Comment\n"
    f = StringIO(csv_header)
    num_col, mark_col = getCols(f)

    assert num_col == 1, f"Expected Student Number at index 1: {num_col}"
    assert mark_col == 2, f"Expected Mark at index 2: {mark_col}"
    print("getCols testcase passed")

def test_findTop_basic():
    ''' Testing if findTop finds best student '''
    print("Testing findTop")
    csv_data = ''' 16001, 72
    167381, 90
    143211, 83 '''
    f = StringIO(csv_data)
    best_idx, best_mark = findTop(f, 0, 1)

    assert best_idx == "167381", f"Expected student {best_idx}"
    assert best_mark == 90, f"Expected mark {best_mark}"
    print("findTop testcase passed")


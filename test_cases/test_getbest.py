#!/usr/bin/env python3
''' Testcase for getbest.py '''

from io import StringIO
import sys
import os

# Importing the functions from getbest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from getbest import getCols, findTop

def test_getCols__basic():
    ''' Testing if getCols finds the right columns '''
    print("Testing getCols")
    csv_header = "Course,Student Number,Mark,Comment\n"
    f = StringIO(csv_header)
    num_col, mark_col = getCols(f)

    assert num_col == 1, f"Expected Student Number at index 1: {num_col}"
    assert mark_col == 2, f"Expected Mark at index 2: {mark_col}"
    print("getCols testcase passed")

def test_findTop_basic()::
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

def test__reversed__columns():
    '''Testing if the columns are read correctly even if the column order is reversed'''
    print("Testing with reversed columns")
    csv_header = "Mark,Course,Student Number,Comment\n"
    f = StringIO(csv_header)
    num_col, mark_col = getCols(f)

    assert num_col == 2, f"Expected Student Number at index 2: {num_col}"
    assert mark_col == 0, f"Expected Mark at index 0: {mark_col}"
    print("Reversed Columns testcase passed")

def test_new_files():
    '''Testing with own made example CSV file'''
    print("Testing new files")

    #Getting the root
    base_dir = os.path.dirname(os.path.abspath(__file___))

    #Test 1
    file1_path = os.path.join(base_dir, "test1.csv")
    with open(file1_path, 'r') as f:
        num_col, mark_col = getCols(f)

        #checking if corrrect coloumns are found
        assert num_col == 0, f"test1.csv: Student Number at index 1 {num_col}"
        assert mark_col == 1, f"test1.csv: Mark at index 2 {mark_col}"

        #checking the correct top student is found
        best_id, best_mark = findTop(f, num_col, mark_col)
        assert best_id == "2658083", f"test1.csv: Student Number {best_id}"
        assert best_mark == 90, f"test1.csv: Mark {best_mark}"

    print("test1.csv passed")

    #Test 2 (reversed)
    file2_path = os.path.join(base_dir, "test2.csv")
    with open(file2_path, "r") as f:
        num_col, mark_col = getCols(f)

        #checking if correct columns are found
        assert num_col == 2, f"test2.csv: Student Number at index 2 {num_col}"
        assert mark_col ==0, f"test2.csv: Mark at index 0 {mark_col}"

        #checking if correct top student is found
        best_id, best_mark = findTop(f, num_col, mark_col)
        best_id == "2658085", f"test2.csv: Student Number {best_id}"
        best_mark == "92", f"test2.csv: Mark {best_mark}"

    print("test2.csv passed")


if __name__ == "__main__":
    print("Testing Testcases")
    try:
        test_getCols_basic()
        test_findTop_basic()
        test_reversed_columns()
        test_new_files()
        print("All Testcases Passed!")
    except AssertionError as e:
        print(f"Test Failed: {e}"}

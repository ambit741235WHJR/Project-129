@echo off
python "PYs/Data Pre-Processing.py"
ECHO Data Pre-Processed
python "PYs/Data Merging.py"
ECHO Data Merged
python "PYs/Data Cleaning.py"
ECHO Data Cleaned and Fully Merged
pause
@echo off
echo starting ...
call pytest tests/test_store.py --alluredir=tests/reports
rem exit

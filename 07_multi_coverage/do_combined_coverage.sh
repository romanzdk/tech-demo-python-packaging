#!/usr/bin/env sh

# Run and report coverage on both distribution packages separate
cd fruit
coverage run
coverage report
cd ../vegetable
coverage run
coverage report
cd ..

# Combine the coverage data into one file
coverage combine --keep fruit/.coverage vegetable/.coverage

# Report
coverage report


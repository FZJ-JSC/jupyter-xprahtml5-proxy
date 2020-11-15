#!/bin/bash

# you might need to modify your environment
# before you can start 'xpra'
# Do it here.

# example
# module purge > /dev/null
# module use $OTHERSTAGES > /dev/null
# module load Stages/2020 > /dev/null
# module load GCCcore/.9.3.0 > /dev/null
# module load xpra/4.0.4-Python-3.8.5 > /dev/null

xpra $@

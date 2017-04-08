#!/bin/bash

if [ "$1" = "clean" ]; then
    unset PYTHONPATH
else
    export PYTHONPATH=`pwd`:${PYTHONPATH}
fi

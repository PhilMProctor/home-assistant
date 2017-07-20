#!/bin/bash
. /home/pi/notebook/bin/activate
cd /home/pi/notebook/notebooks
exec /home/pi/notebook/bin/jupyter notebook > /dev/null 2>&1
echo $$
echo $BASHPID

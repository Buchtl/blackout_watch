#!/bin/bash
pushd ~ || exit
rm -f heartbeat.txt times.txt systime.txt downtimes.json startup.log
popd || exit
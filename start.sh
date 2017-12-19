#!/bin/sh
export PYTHONPATH=~/pybrain:$PYTHONPATH
echo -n "Starting KippoRLPot in background..."
twistd -y kippo.tac -l log/kippo.log --pidfile kippo.pid

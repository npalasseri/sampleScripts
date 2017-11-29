#!/bin/bash
source $GRINDER_WORKSPACE/setGrinderEnv.sh
java -classpath $CLASSPATH net.grinder.TCPProxy -console -http > grinder.py

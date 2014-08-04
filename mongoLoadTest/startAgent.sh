#!/bin/bash
source $GRINDER_WORKSPACE/setGrinderEnv.sh
echo "More from : "$CLASSPATH
java -classpath $CLASSPATH net.grinder.Grinder "$PWD/grinder.properties"

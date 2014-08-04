from net.grinder.script import Test
from net.grinder.script.Grinder import grinder
from java.util import Date
from java.lang import Thread
 
test1 = Test(1, "Log method")
 
# Instrument the info() method with our Test.
test1.record(grinder.logger.info)
 
class TestRunner:
    def __call__(self):
        grinder.logger.info("Hello World : Sleeping for 500 ms")
	Thread.sleep(10000)
        grinder.logger.info("waking up" )

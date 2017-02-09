from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2olog_and_echo():
    """
    Python API test: h2o.log_and_echo(message=u'')
    """
    h2o.log_and_echo("Testing h2o.log_and_echo")

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2olog_and_echo)
else:
    h2olog_and_echo()

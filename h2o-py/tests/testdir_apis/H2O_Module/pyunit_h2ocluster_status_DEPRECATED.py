from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o

def h2ocluster_status():
    """
    Python API test: h2o.cluster_status()
    Deprecated, use h2o.cluster().show_status(True)
    """
    h2o.cluster_status()    # no return type

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2ocluster_status)
else:
    h2ocluster_status()

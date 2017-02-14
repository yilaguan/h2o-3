from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrameAnyNaRm():
    """
    Python API test: h2o.frame.H2OFrame.any_na_rm()
    """
    h2o.connect()
    python_lists = [[0,1,0,0], [0,0,0,0]]
    h2oframe = h2o.H2OFrame(python_obj=python_lists, na_strings=['NA'])
    assert h2oframe.any(), "h2o.H2OFrame.any_rm_na() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrameAnyNaRm())
else:
    h2o_H2OFrameAnyNaRm()

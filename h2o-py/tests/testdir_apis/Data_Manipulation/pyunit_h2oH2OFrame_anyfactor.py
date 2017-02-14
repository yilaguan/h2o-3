from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_anyfactor():
    """
    Python API test: h2o.frame.H2OFrame.anyfactor()
    """
    try:
        h2o.connect()
        python_lists = [[1,1,1,1], [1,1,1,1]]
        h2oframe = h2o.H2OFrame(python_obj=python_lists, na_strings=['NA'])
        # should return false since all are numbers
        assert not(h2oframe.anyfactor()), "h2o.H2OFrame.anyfactor() command is not working."
        h2oframe[0]=h2oframe[0]>0.0     # change one column to categorical
        assert h2oframe.anyfactor(), "h2o.H2OFrame.anyfactor() command is not working."
    except Exception as e:
        assert False, "h2o.H2OFrame.anyfactor() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_anyfactor())
else:
    h2o_H2OFrame_anyfactor()

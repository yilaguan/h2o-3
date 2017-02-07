from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np

def h2o_H2OFrameAcos():
    """
    Python API test: h2o.frame.H2OFrame.acos()
    """
    try:
        h2o.connect()
        python_lists = np.random.uniform(-1,1, (3,4))
        h2oframe = h2o.H2OFrame(python_obj=python_lists)
        newframe = h2oframe.acos()       # new H2O frame contains only positive elements
        assert pyunit_utils.assert_corret_frame_operation(h2oframe, newframe, "acos"), \
            "h2o.H2OFrame.acos() command is not working."
    except Exception as e:
        assert False, "h2o.H2OFrame.acos() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrameAcos())
else:
    h2o_H2OFrameAcos()

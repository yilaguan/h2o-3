from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrameAsin():
    """
    Python API test: h2o.frame.H2OFrame.asin()
    """
    try:
        h2o.connect()
        python_lists = np.random.uniform(-1,1, (3,4))
        h2oframe = h2o.H2OFrame(python_obj=python_lists)
        newframe = h2oframe.asin()
        assert_is_type(newframe, H2OFrame)
        pyunit_utils.assert_corret_frame_operation(h2oframe, newframe, "asin")
    except Exception as e:
        assert False, "h2o.H2OFrame.asin() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrameAsin())
else:
    h2o_H2OFrameAsin()

from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame
import random

def h2o_H2OFrame_digamma():
    """
    Python API test: h2o.frame.H2OFrame.digamma()

    Copied frm pyunit_vec_math_ops.py
    """
    h2o.connect()
    num_data = [[random.uniform(1,10) for r in range(5)] for c in range(5)]
    h2o_data = h2o.H2OFrame(num_data)
    newframe = h2o_data.digamma()
    assert_is_type(newframe, H2OFrame)
    pyunit_utils.assert_corret_frame_operation(h2o_data, newframe, "digamma")

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_digamma())
else:
    h2o_H2OFrame_digamma()

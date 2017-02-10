from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np

def h2o_H2OFrame_get_frame_data():
    """
    Python API test: h2o.frame.H2OFrame.get_frame_data
    """
    h2o.connect()
    python_lists = np.random.uniform(-1,1, (3,4))
    frameName = "randomlyGeneratedFrame."
    h2oframe = h2o.H2OFrame(python_obj=python_lists, destination_frame=frameName)
    assert frameName==h2oframe.frame_id, "h2o.H2OFrame.frame_id command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_get_frame_data())
else:
    h2o_H2OFrame_get_frame_data()

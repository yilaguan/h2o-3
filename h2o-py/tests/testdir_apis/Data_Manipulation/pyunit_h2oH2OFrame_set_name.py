from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame
import numpy as np

def h2o_H2OFrame_set_name():
    """
    Python API test: h2o.frame.H2OFrame.set_name(col=None, name=None)
    """
    h2o.connect()
    python_lists = np.random.randint(-5,5, (100, 3))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)
    newName = "Dolphine"
    newName2 = "Sharks"
    h2oframe.set_name(col=0, name=newName)
    assert h2oframe.names[0]==newName, "h2o.H2OFrame.set_name() command is not working."

    h2oframe.set_name(col=1, name=newName2)
    assert h2oframe.names[1]==newName2, "h2o.H2OFrame.set_name() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_set_name())
else:
    h2o_H2OFrame_set_name()

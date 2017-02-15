from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_structure():
    """
    Python API test: h2o.frame.H2OFrame.structure()
    """
    h2o.connect()
    frame = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris.csv"))
    frame.structure()

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_structure())
else:
    h2o_H2OFrame_structure()

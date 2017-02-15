from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame

def h2o_H2OFrame_substring():
    """
    Python API test: h2o.frame.H2OFrame.sub(pattern, replacement, ignore_case=False)

    Copied from pyunit_substring.py
    """
    h2o.connect()
    frame = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris.csv"))
    frame["C5"] = frame["C5"].sub('s','z', ignore_case=False)
    assert frame[1,4] == "Iriz-setosa", "Expected 'Iriz-setosa', but got {0}".format(frame[1,4])

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_substring())
else:
    h2o_H2OFrame_substring()

from __future__ import print_function
import sys, os
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_columns():
    """
    Python API test: h2o.frame.H2OFrame.columns()

    Copied from pyunit_colnames.py
    """
    h2o.connect()
    iris_wheader = h2o.import_file(pyunit_utils.locate("smalldata/iris/iris_wheader.csv"))
    expected_names = ["sepal_len", "sepal_wid", "petal_len", "petal_wid", "class"]
    assert iris_wheader.columns == expected_names, \
        "Expected {0} for column names but got {1}".format(expected_names, iris_wheader.columns)

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_columns())
else:
    h2o_H2OFrame_columns()

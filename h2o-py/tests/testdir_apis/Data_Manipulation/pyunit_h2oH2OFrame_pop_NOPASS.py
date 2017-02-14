from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame
from random import randrange
import numpy as np


def h2o_H2OFrame_pop():
    """
    Python API test: h2o.frame.H2OFrame.isfactor()
    """
    h2o.connect()
    row_num = randrange(2,10)
    col_num = randrange(3,20)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)

    oneColumn = h2oframe.pop[3]     # pop using integer index
    assert_is_type(oneColumn, H2OFrame)
    assert h2oframe.ncol==(col_num-1), "h2o.H2OFrame.pop() command is not working."  # check return result

    oneColumn = h2oframe.pop[h2oframe.names[1]]     # pop using column name
    assert_is_type(oneColumn, H2OFrame)
    assert h2oframe.ncol==(col_num-2), "h2o.H2OFrame.pop() command is not working."  # check return result

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_pop())
else:
    h2o_H2OFrame_pop()

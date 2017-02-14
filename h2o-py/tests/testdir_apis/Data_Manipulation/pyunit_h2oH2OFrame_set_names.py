from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame
import numpy as np
from random import shuffle
import random

def h2o_H2OFrame_set_names():
    """
    Python API test: h2o.frame.H2OFrame.set_names(names)
    """
    h2o.connect()

    row_num = randrange(1,10)
    col_num = randrange(1,10)
    python_lists = np.random.randint(-5,5, (row_num, col_num))
    h2oframe = h2o.H2OFrame(python_obj=python_lists)

    newNames = random.sample(h2oframe.names, col_num)
    h2oframe.set_names(names=newNames)

    assert h2oframe.names==newNames, "h2o.H2OFrame.set_names() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_set_names())
else:
    h2o_H2OFrame_set_names()

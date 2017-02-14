from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
import numpy as np
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_cummax():
    """
    Python API test: h2o.frame.H2OFrame.prod(na_rm=False)
    """
    h2o.connect()
    python_object=[list(range(1,10)), list(range(1,10))]
    python_object_transpose = np.transpose(python_object)
    foo = h2o.H2OFrame(python_obj=python_object)
    foo_transpose =  h2o.H2OFrame(python_obj=python_object_transpose)

    prod1 = foo_transpose.prod(na_rm=False)   # default
    prod2 = foo.prod(na_rm=True)   # row

    # check correct return type
    assert_is_type(prod1, float)
    assert_is_type(prod2, float)
    assert abs(prod1-prod2)<1e-6, "h2o.H2OFrame.prod() command is not working."
if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_cummax())
else:
    h2o_H2OFrame_cummax()

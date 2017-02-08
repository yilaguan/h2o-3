from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
from tests import pyunit_utils
import h2o
from h2o.utils.typechecks import assert_is_type
from h2o.frame import H2OFrame


def h2o_H2OFrame_countmatches():
    """
    Python API test: h2o.frame.H2OFrame.countmatches()

    Copied from pyunit_countmatches.py
    """
    try:
        h2o.connect()

        iris_frame = h2o.import_file(path=pyunit_utils.locate("smalldata/iris/iris.csv"),
                                     col_types=["numeric","numeric","numeric","numeric","string"])
        result_frame = iris_frame.countmatches(["ic","ri","ca"])
        assert_is_type(result_frame, H2OFrame)

    except Exception as e:
        assert False, "h2o.H2OFrame.countmatches() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_countmatches())
else:
    h2o_H2OFrame_countmatches()

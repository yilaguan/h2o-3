from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_as_data_frame():
    """
    Python API test: h2o.frame.H2OFrame.as_data_frame()

    Copied from pyunit_as_data_frame.py
    """
    try:
        h2o.connect()
        smallbike = h2o.import_file(pyunit_utils.locate("smalldata/jira/citibike_head.csv"))
        smallbike_noheader = smallbike.as_data_frame(use_pandas=False, header=False)
        assert len(smallbike_noheader) == smallbike.nrow

        head_small_bike = smallbike.head(rows=5, cols=2)
        tail_small_bike = smallbike.tail(rows=5, cols=2)
        assert len(head_small_bike[0])==len(tail_small_bike[0])==5, "h2o.H2OFrame.as_data_frame() command is " \
                                                                    "not working."
        assert len(head_small_bike)==len(tail_small_bike)==5, "h2o.H2OFrame.as_data_frame() command is not working."

        ##use_pandas = True
        small_bike_pandas = smallbike.as_data_frame(use_pandas=True, header=True)
        assert small_bike_pandas.__class__.__name__ == "DataFrame"
        assert small_bike_pandas.shape == (smallbike.nrow, smallbike.ncol)
    except Exception as e:
        assert False, "h2o.H2OFrame.as_data_frame() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_as_data_frame())
else:
    h2o_H2OFrame_as_data_frame()

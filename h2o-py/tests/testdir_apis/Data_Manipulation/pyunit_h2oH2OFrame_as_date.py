from __future__ import print_function
import sys
sys.path.insert(1,"../../../")
import h2o
from tests import pyunit_utils

def h2o_H2OFrame_as_date():
    """
    Python API test: h2o.frame.H2OFrame.as_date()

    Copied from pyunit_as_date.py
    """
    try:
        h2o.connect()
        hdf = h2o.import_file(path=pyunit_utils.locate("smalldata/jira/v-11-eurodate.csv"))
        temp = hdf['sd1'].as_date("YYYY-mm-dd")
        print("wow")
    except Exception as e:
        assert False, "h2o.H2OFrame.as_date() command is not working."

if __name__ == "__main__":
    pyunit_utils.standalone_test(h2o_H2OFrame_as_date())
else:
    h2o_H2OFrame_as_date()

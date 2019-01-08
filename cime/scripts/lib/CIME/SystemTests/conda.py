"""
Implemetation of CIME MCC test: Compares ensemble methods

This does two runs: In the first we run a three member ensemble using the
 MULTI_DRIVER capability, then we run a second single instance case and compare
"""

import sys
import logging
import datetime

from CIME.utils import expect
from CIME.SystemTests.system_tests_common import SystemTestsCommon

logger = logging.getLogger(__name__)


class CONDA(SystemTestsCommon):

    def __init__(self, case):
        """
        initialize an object interface to the SMS system test
        """
        super(CONDA, self).__init__(case)

        isconda = 'conda' in sys.version.lower() or 'continuum' in sys.version.lower()

        expect(isconda, 'This is not running inside a Anaconda/miniconda environment.\n'
                        '    The system version is: "{}"\n'
                        '    The system executable is: "{}"'.format(sys.version, sys.executable))

        datestamp = datetime.datetime.today().strftime('%Y%m%d-%H%M%S')
        with open('/autofs/nccs-svm1_home1/kennedy/E3SM/E3SM/cime/scripts/CONDA_{}.log'.format(datestamp), 'w') as condalog:
            condalog.write('CONDA:INIT: system version:\n     {}\n\n'.format(sys.version))
            condalog.write('CONDA:INIT: system executable:\n     {}\n\n'.format(sys.executable))


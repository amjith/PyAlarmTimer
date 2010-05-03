from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')
setup(
    options = {'py2exe':{'bundle_files':1, 'includes':["sip"]}},
    windows = [{'script': "AlarmSetup.py"}],
    license="GNU General Public License (GPL)",  
    package_data={"AlarmClock": ["Resources/bell.png"]},  

    zipfile = None,
    )


from distutils.core import setup
import py2exe, sys, os

#setup(windows=[{"script":"AlarmSetup.py"}], options={"py2exe":{"includes":["sip"]}})

sys.argv.append('py2exe')
setup(
    options = {'py2exe':{'bundle_files':1, 'includes':["sip"]}},
    windows = [{'script': "AlarmSetup.py"}],
    zipfile = None,
    )


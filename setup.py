import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

APP = ['Danvasion.py']
DATA_FILES = ['bacon.png', 'blaine.png','brendan.png', 'bullet.png','cody.png',
              'daniel.png', 'lizzy.png' 'millie.png', 'paige.png', 'rachel.png',
              'sophie.png', 'stars.png', 'pew.wav'  ]
OPTIONS = {
 'iconfile':'daniel.icns',
 'argv_emulation': True,
 'packages': ['sys', 'pygame', 'random', 'time', 'certifi'],
 'includes': ['alien.py', 'bacon.py','bullet.py',
                   'button.py', 'game_functions.py','game_stats.py',
                   'scoreboard.py', 'settings.py', 'ship.py' ],
 'plist': {
     'PyRuntimeLocations': [
         '@executable_path/../Frameworks/libpython3.7m.dylib',
         '/Users/blainequackenbush/opt/anaconda3/pkgs/python-3.7.6-h359304d_2/lib/libpython3.7m.dylib']
}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

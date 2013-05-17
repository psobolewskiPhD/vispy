# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import

"""
Vispy - http://vispy.org

The vispy consists of multiple subpackages that need to be imported
separately before use. These are:

  * ... todo

"""

__version__ = '0.0.dev'

import vispy.util
from vispy.util import keys

from vispy.event import EmitterGroup, Event




## used for application-global settings.

class Config(object):
    def __init__(self):
        self.events = EmitterGroup(source=self,
                                   changed=Event,)
        self._config = {}
    
    def __getitem__(self, item):
        return self._config[item]
    
    def __setitem__(self, item, val):
        self._config[item] = val
        ## inform any listeners that a configuration option has changed
        self.events.changed(type='config_change', item=item, value=val)
        
    def update(self, **kwds):
        for k,v in kwds.items():
            self[k] = v


config = Config()
config['default_backend'] = 'qt'
config['qt_lib'] = 'any'  # options are 'pyqt', 'pyside', or 'any'


# -*- coding: utf-8 -*-
"""
Add FDSN URL's to those listed by default in obspy.clients.fdsn.header.URL_MAPPINGS 

:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
from obspy.clients.fdsn.header import URL_MAPPINGS

MORE_FDSN = {'AUSPASS':'http://auspass.edu.au',
             'BATS':'http://batsws.earth.sinica.edu.tw',
             'LOCALHOST':'http://localhost:8080'}

URL_MAPPINGS.update(MORE_FDSN)

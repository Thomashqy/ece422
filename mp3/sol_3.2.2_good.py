#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """            Ӌ�		;��M�^Jp��h2FOC�!�����h39����������#_�7��c_BKY)�2*<m�wŀ�fcɨď��[h!�ȩ�*`������rV������Z�FZ�$h��@�R
"""
from hashlib import sha256

if sha256(blob).hexdigest() == "46f1fbcb1d6f045ff2989d01200cbc23a8d68a5f00414ce2d9137bb05f247f7f":
    print "I come in peace."
else:
    print "Prepare to be destroyed!"

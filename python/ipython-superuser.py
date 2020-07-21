import os
import time
import sys

time.sleep(1)

import ncs
ncs_trans_id=int(os.environ['NCS_MAAPI_THANDLE'])
ncs_sess_id=int(os.environ['NCS_MAAPI_USID'])
maapi=ncs.maapi.Maapi()
trans=maapi.attach(ncs_trans_id)
root=ncs.maagic.get_root(trans)
if len(sys.argv) > 1:
    path = ncs.maagic.get_node(trans, sys.argv[1])

print("+-----------------------------------------------------------------------------+")
print("| You may reference the current transaction maagic YANG root object as 'root' |")
print("| E.g.   In [1]: for dev in root.devices.device:                              |")
print("|          ...:     print dev.name                                            |")
print("| If a keypath was given to the ipython cli command, you may reference        |")
print("| the maagic YANG path object as 'path', E.g:                                 |")
print("| JLINDBLA-M-J8L9# ipython devices device                                     |")
print("|        In [1]: for dev in path:                                             |")
print("|          ...:     print dev.name                                            |")
print("+-----------------------------------------------------------------------------+")

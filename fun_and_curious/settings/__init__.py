from fun_and_curious.settings.base import *

if IN_PYTHONANYWHERE is True:
    from fun_and_curious.settings.prod import *
else:
    from fun_and_curious.settings.local import *

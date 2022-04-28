from .base import *
import socket

hostname = socket.gethostname()
if hostname =='alpini':
   from .prod import *
else:
   from .dev import *
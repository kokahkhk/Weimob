import os,sys
import re
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(path)
from lib.common import Common

class lib(Common):
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	pass


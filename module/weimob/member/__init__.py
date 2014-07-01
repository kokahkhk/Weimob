import os,sys
import re
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "//Weimob"))
sys.path.append(path)
from businessset import BusinesssetPage
from public.public import PublicModule
from membercardset import MembercardsetPage
from weimembermgmt import MemberMgmtgPage
from membertrade import MemberTradePage
from membermkt import MemberMktPage

class member(BusinesssetPage,
	PublicModule,
	MembercardsetPage,
	MemberMgmtgPage,
	MemberTradePage,
	MemberMktPage):
	ROBOT_LIBRARY_SCOPE = 'GLOBAL'
	pass
'''
@author:wuxusheng
'''
import os,sys
import re
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "//Weimob"))
sys.path.append(path)
import settings
from lib.common import Common

class LoginPage(Common):
	
	def user_login(self):
		url = settings.Weimob.Live.URL
		username = settings.Weimob.Live.USERNAME
		password = settings.Weimob.Live.PASSWORD
		self.start_page(url,'gc')
		self.input_text('username',username)
		self.input_password('password',password)
		self.click_button('btn-login')
		self.wait_until_page_contains_element("mainFrame", settings.TIMEOUT)
		self.maximize_browser_window()


'''
@author:wuxusheng
'''
import settings
from lib.common import Common

class MainPage(Common):

	def choose_public_name(self, index):
		self.select_frame("mainFrame")
		self.click_element("//table[@id='listTable']/tbody/tr[%s]/td" %index)
		self.wait_until_page_contains_element("left", settings.TIMEOUT)
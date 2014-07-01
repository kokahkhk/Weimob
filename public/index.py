#coding=utf-8
'''
@author:wuxusheng
'''
import settings
from lib.common import Common
import time

class IndexPage(Common):
	
	def navigate_to_wei_member(self):
		self.click_element("//div[@class='subnav'][10]/div/a")
		self.wait_until_page_contains_element("//a[(text()='数据统计')]", settings.TIMEOUT)
		time.sleep(1)

#coding=utf-8
'''
@author:wuxusheng
'''
import settings
from lib.common import Common

class BusinesssetPage(Common):

	def input_id_shopname(self, text):
		self.input_text("shop_name",text)

	def input_id_keyword(self, text):
		self.input_text("keyword",text)

	def input_id_address(self, text):
		self.input_text("address",text)

	def input_id_phone(self, text):
		self.input_text("phone",text)

	def click_id_insertimage(self):
		self.click_element("insertimage")
		self.wait_until_page_contains_element("//input[@class='ke-button-common ke-button' and @value='确定']",settings.TIMEOUT)
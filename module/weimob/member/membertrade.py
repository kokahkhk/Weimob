#coding=utf-8
'''
@author:wuxusheng
'''
import settings
from lib.common import Common

class MemberTradePage(Common):

	def click_class_icongift(self):
		self.click_element("//i[@class='icon-gift']")

	def input_name_key(self, text):
		self.input_text('key', text)

	def input_name_sn(self, text):
		self.input_text('sn', text)

	def click_class_conumesearch(self):
		self.click_element("//div[@class='tile-info' and (strong/text()='消费查询')]")
		self.wait_until_page_contains_element("//button[@class='btn' and i/@class='icon-search']", settings.TIMEOUT)

	def click_class_chargesearch(self):
		self.click_element("//div[@class='tile-info' and (strong/text()='充值查询')]")
		self.wait_until_page_contains_element("//button[@class='btn' and i/@class='icon-search']", settings.TIMEOUT)

	def click_class_scoresearch(self):
		self.click_element("//div[@class='tile-info' and (strong/text()='积分查询')]")
		self.wait_until_page_contains_element("//button[@class='btn' and i/@class='icon-search']", settings.TIMEOUT)

	''' 
	消费查询
	'''
	def input_name_moneys_from(self, cash_from, cash_to):
		self.input_text("//input[@name='moneys']", cash_from)
		self.enter_tab(1)
		self.enter_send(cash_to)

	def click_class_iconsearch(self):
		self.click_element("//button[@class='btn' and i/@class='icon-search']")
		self.wait_until_page_contains_element("//button[@class='btn' and i/@class='icon-search']", settings.TIMEOUT)


	


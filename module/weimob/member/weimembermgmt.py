#coding=utf-8
'''
@author:wuxusheng
'''
import settings
from lib.common import Common

class MemberMgmtgPage(Common):

	def click_class_iconclouddownload(self):
		self.click_element("//i[@class='icon-cloud-download']")

	def click_class_iconrefresh(self):
		self.click_element("//i[@class='icon-refresh']")

	def input_id_keywordinput(self, text):
		self.input_text("keyword-input", text)

	def click_inquery(self):
		self.click_element("//button[@class='btn' and (text()='查询')]")

	def click_class_iconyen(self, index):
		element_iconye = "//table[@id='listTable']/tbody/tr[%s]/td[10]/a[1]/i" %index
		element_membertrade_iconye = "//i[@class='icon-yen']"

		if self.capture_exception(element_iconye) == False:
			self.click_element(element_iconye)
			self.wait_until_page_contains_element("//form[@id='Form1']/div[3]/button[2]",settings.TIMEOUT)
		elif self.capture_exception(element_membertrade_iconye) == False:
			self.click_element(element_membertrade_iconye)
			self.wait_until_page_contains_element("//form[@id='Form1']/div[3]/button[2]",settings.TIMEOUT)
		else:
			print 'Not Match Element'			

	def click_class_iconusd(self, index):
		element_iconusd = "//table[@id='listTable']/tbody/tr[%s]/td[10]/a[2]/i" %index
		element_membertrade_iconusd = "//i[@class='icon-usd']"

		if self.capture_exception(element_iconusd) == False:
			self.click_element(element_iconusd)
			self.wait_until_page_contains_element("//form[@id='Form1']/div[3]/button[1]",settings.TIMEOUT)
		elif self.capture_exception(element_membertrade_iconusd) == False:
			self.click_element(element_membertrade_iconusd)
			self.wait_until_page_contains_element("//form[@id='Form1']/div[3]/button[1]",settings.TIMEOUT)
		else:
			print 'Not Match Element'


	def click_class_iconmoney(self, index):
		element_iconmoney = "//table[@id='listTable']/tbody/tr[%s]/td[10]/a[3]/i" %index
		element_membertrade_iconmoney = "//i[@class='icon-money']"

		if self.capture_exception(element_iconmoney) == False:
			self.click_element(element_iconmoney)
			self.wait_until_page_contains_element("//form[@id='Form3]/div/div/div/input[@name='nick']",settings.TIMEOUT)
		elif self.capture_exception(element_membertrade_iconmoney) == False:
			self.click_element(element_membertrade_iconmoney)
			self.wait_until_page_contains_element("//form[@id='Form3]/div/div/div/input[@name='nick']",settings.TIMEOUT)
		else:
			print 'Not Match Element'

	def click_class_iconbarchart(self, index):
		self.click_element("//table[@id='listTable']/tbody/tr[%s]/td[10]/a[4]/i" %index)	

	def click_class_iconlock(self, index):
		self.click_element("//table[@id='listTable']/tbody/tr[%s]/td[10]/a[6]/i" %index)

	def input_id_price(self, text):
		self.input_text('price', text)

	def input_name_nick(self, text):
		element_iconye = "//form[@id='Form1']/div/div/div/input[@name='nick']"
		element_iconusd = "//form[@id='Form2']/div/div/div/input[@name='nick']"
		element_iconmoney = "//form[@id='Form3']/div/div/div/input[@name='nick']"

		if self.capture_exception(element_iconye) == False:
			self.input_text(element_iconye, text)
		elif self.capture_exception(element_iconusd) == False:
			self.input_text(element_iconusd, text)
		elif self.capture_exception(element_iconmoney) == False:
			self.input_text(element_iconmoney, text)
		else:
			print 'Not Match Element'

	def click_class_btnbtnprimary(self):
		element_iconye = "//form[@id='Form1']/div[3]/button[1]"
		element_iconusd = "//form[@id='Form2']/div[3]/button[1]"
		element_iconmoney = "//form[@id='Form3']/div[3]/button[1]"
		element_icongift = "//form[@id='Form3']/div[4]/button[2]"

		if self.capture_exception(element_iconye) == False:
			self.click_element(element_iconye)
		elif self.capture_exception(element_iconusd) == False:
			self.click_element(element_iconusd)
		elif self.capture_exception(element_iconmoney) == False:
			self.click_element(element_iconmoney)
		elif self.capture_exception(icongift) == False:
			self.click_element(icongift)
		else:
			print 'Not Match Element'

	def click_class_btnbtndefault(self):
		element_iconye = "//form[@id='Form1']/div[3]/button[2]"
		element_iconusd = "//form[@id='Form2']/div[3]/button[2]"
		element_iconmoney = "//form[@id='Form3']/div[3]/button[2]"
		element_icongift = "//form[@id='Form3']/div[4]/button[2]"

		if self.capture_exception(element_iconye) == False:
			self.click_element(element_iconye)
		elif self.capture_exception(element_iconusd) == False:
			self.click_element(element_iconusd)
		elif self.capture_exception(element_iconmoney) == False:
			self.click_element(element_iconmoney)
		elif self.capture_exception(icongift) == False:
			self.click_element(icongift)
		else:
			print 'Not Match Element'

	def input_id_money(self, text):
		self.input_text('money', text)

	def input_id_score(self, text):
		self.input_text('score', text)

	def input_id_truename(self, text):
		self.input_text('truename', text)

	def click_class_freeze(self):
		self.click_element("//a[@class='btn' and i/@class='icon-lock']")
#coding=utf-8
'''
@author:wuxusheng
'''
import os,sys
import re
import time
path = os.path.abspath(os.path.join(os.path.dirname(__file__), "//Weimob"))
sys.path.append(path)
import settings
from login import LoginPage
from index import IndexPage
from main import MainPage

class PublicModule(LoginPage,
	IndexPage,
	MainPage):

	def click_image_ok_button(self):
		self.click_element("//input[@class='ke-button-common ke-button' and @value='确定']")

	def click_image_cancel_button(self):
		self.click_element("//input[@class='ke-button-common ke-button' and @value='取消']")

	def click_name_viewserver(self):
		self.click_element("//input[@class='ke-button-common ke-button' and @value='图片空间']")
		self.wait_until_page_contains_element("//div[@class='ke-inline-block ke-item'][1]/div[@class='ke-inline-block ke-photo']/img", settings.TIMEOUT)

	def choose_image_from_imagespace(self,index):
		# self.execute_javascript("$(window.frames['mainFrame'].document).find('.ke-plugin-filemanager-body>div>div>img')[%s].click()" %index)
		self.click_element("//div[@class='ke-inline-block ke-item'][%s]/div[@class='ke-inline-block ke-photo']/img" %index)
		self.wait_until_page_contains_element("//div[@class='ke-inline-block ke-photo'][1]/img", settings.TIMEOUT)
		time.sleep(3)
		self.click_element("//div[@class='ke-inline-block ke-photo'][1]/img")
		self.wait_until_element_is_visible("//input[@class='ke-button-common ke-button' and @value='取消']", settings.TIMEOUT)

	def navigate_to_menu(self,text):
		self.click_element("//a[(text()='%s')]" %text)
		self.wait_until_page_contains_element("mainFrame", settings.TIMEOUT)
		self.select_frame("mainFrame")

	def navigate_to_sub_tab(self,text):
		self.click_element("//a[(text()='%s')]" %text)

	def click_button_save(self):
		self.scroll_down()		
		self.click_button("bsubmit")

	def click_button_cancel(self):
		self.scroll_down()
		self.click_element("//button[@class='btn' and (text()='取消')]")

	def checkpoint_cancel_button(self):
		self.scroll_down()
		self.wait_until_page_contains_element("//button[@class='btn' and (text()='取消')]", settings.TIMEOUT)

	def click_class_iconcalendar(self):
		self.click_element("//i[@class='icon-calendar']")
		self.wait_until_page_contains_element("//button[@class='btn-success applyBtn btn btn-small']", settings.TIMEOUT)
		self.click_element("//button[@class='btn-success applyBtn btn btn-small']")

	def click_page_next(self):
		self.scroll_down()
		self.click_element("//a[(text()='下一页')]")
		self.wait_until_page_contains_element("//a[(text()='上一页')]", settings.TIMEOUT)	

	def click_page_previous(self):
		self.scroll_down()
		self.click_element("//a[(text()='上一页')]")
		self.wait_until_page_contains_element("//a[(text()='下一页')]", settings.TIMEOUT)

	def click_page_number(self, number):
		self.scroll_down()
		self.click_element("//a[(text()='%s')]" %number)

	def click_class_iconedit(self, index):
		element_memberprivilege = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[1]/i[@class='icon-edit']" %index
		element_businessrelate = "//table[@id='listTable']/tbody/tr[%s]/td[5]/a[1]/i[@class='icon-edit']" %index
		element_weimembermng = "//table[@id='listTable']/tbody/tr[%s]/td[10]/a[5]/i[@class='icon-edit']" %index
		element_membermkt = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[3]/i[@class='icon-edit']" %index
		
		if self.capture_exception(element_memberprivilege) == False:
			self.click_element(element_memberprivilege)
			self.checkpoint_cancel_button()
		elif self.capture_exception(element_businessrelate) == False:
			self.click_element(element_businessrelate)
			self.checkpoint_cancel_button()
		elif self.capture_exception(element_weimembermng) == False:
			self.click_element(element_weimembermng)
			self.checkpoint_cancel_button()
		elif self.capture_exception(element_membermkt) == False:
			self.click_element(element_membermkt)
			self.ccheckpoint_cancel_button()
		else:
			print 'Not Match Element'

	def click_class_iconremove(self, index):
		element_memberprivilege = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[2]/i[@class='icon-remove']" %index
		element_businessrelate = "//table[@id='listTable']/tbody/tr[%s]/td[5]/a[2]/i[@class='icon-remove']" %index
		element_membermkt = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[4]/i[@class='icon-remove']" %index
		element_membermkt_car = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[3]/i[@class='icon-remove']" %index

		if self.capture_exception(element_memberprivilege) == False:
			self.click_element(element_memberprivilege)
		elif self.capture_exception(element_businessrelate) == False:
			self.click_element(element_businessrelate)
		elif self.capture_exception(element_membermkt) == False:
			self.click_element(element_membermkt)
		elif self.capture_exception(element_membermkt_car) == False:
			self.click_element(element_membermkt_car)
		else:
			print 'Not Match Element'

	def checkbox_class_checkall(self):
		self.click_element("//input[@class='check_all']")

	def checkbox_name_check(self, index):
		self.click_element("//table[@id='listTable']/tbody/tr[%s]/td[1]/input" %index)

	def input_class_kecontent(self,text):
		self.select_frame("//iframe[@class='ke-edit-iframe']")
		self.input_text("//body[@class='ke-content']", text)
		self.unselect_frame()
		self.select_frame("mainFrame")


#coding=utf-8
'''
@author:wuxusheng
'''
import settings
from lib.common import Common

class MemberMktPage(Common):

	class_iconticket = "//i[@class='icon-ticket']"
	class_iconplus = "//a[@class='btn' and i/@class='icon-plus']"
	class_iconcreditcard = "//i[@class='icon-credit-card']"
	class_iconshare = "//i[@class='icon-share']"
	class_iconstarempty = "//i[@class='icon-star-empty']"
	class_iconshoppingcart = "//i[@class='icon-shopping-cart']"
	class_iconheartempty = "//i[@class='icon-heart-empty']"
	class_btnselectimg = "//button[@class='btn select_img']"
	class_iconcog = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[2]/i[@class='icon-cog']"
	class_iconminus = "//table/tbody/tr[%s]/td[1]/a/i[@class='icon-minus']"
	name_title = 'title'
	name_crowdtype_1 = "//input[@name='crowd_type' and @value='0']"
	name_type = "//input[@name='type' and @value=%s]"
	name_sendnums = 'sendnums'
	name_nums ='nums'
	name_givevalue ='give_value'
	name_dmoney = 'dmoney'
	name_dayjf = 'dayjf'
	name_dayjf6 = 'dayjf6'
	name_share = 'share'
	name_zhuanfa = 'zhuanfa'
	name_check = 'check'
	name_integral = 'integral'
	name_numbertime = 'numbertime'
	name_voteselectvalue = "//table/tbody/tr[%s]/td[2]/input"
	name_ckmsg = 'ck_msg'
	name_rechargevalue = 'recharge_value'
	name_integralvalue = 'integral_value'
	name_giveintegral = 'give_integral'
	name_couponvalue = 'coupon_value'
	name_activitiesvalue = 'activities_value'
	id_sendnumber = 'send_number'
	id_sendmsg = 'send_msg'
	datahref_normal = "//input[@data-href='normal']"
	datahref_marketing = "//input[@data-href='marketing']"
	datahref_caring= "//input[@data-href='caring']"


	def click_class_iconticket(self):
		self.click_element(MemberMktPage.class_iconticket)
		self.wait_until_page_contains_element(MemberMktPage.class_iconplus,settings.TIMEOUT)

	def click_class_iconcreditcard(self):
		self.click_element(MemberMktPage.class_iconcreditcard)

	def click_class_iconshare(self):
		self.click_element(MemberMktPage.class_iconshare)

	def click_class_iconstarempty(self):
		self.click_element(MemberMktPage.class_iconstarempty)

	def click_class_iconshoppingcart(self):
		self.click_element(MemberMktPage.class_iconshoppingcart)

	def click_class_iconheartempty(self):
		self.click_element(MemberMktPage.class_iconheartempty)

	''' 
	优惠劵
	'''

	def click_class_iconplus(self, index):
		n = int(index)+4
		element_car = "//table/tbody/tr[%s]/td[1]/a/i[@class='icon-plus']" %n

		if self.capture_exception(MemberMktPage.class_iconplus) == False:
			self.click_element(MemberMktPage.class_iconplus)
			self.checkpoint_cancel_button()
		elif self.capture_exception(element_car) == False:
			self.click_element(element_car)
		else:
			print 'Not Match Element'		


	def input_name_title(self, text):
		self.input_text(MemberMktPage.name_title, text)

	def radio_datahref_normal(self):
		self.click_element(MemberMktPage.datahref_normal)

	def radio_datahref_marketing(self):
		self.click_element(MemberMktPage.datahref_marketing)

	def radio_datahref_caring(self):
		self.click_element(MemberMktPage.datahref_caring)

	def radio_name_crowdtype_1(self):
		self.click_element(MemberMktPage.name_crowdtype_1)

	def radio_name_type(self, index):
		self.click_element(MemberMktPage.name_type %index)

	def input_name_sendnums(self, text):
		self.input_text(MemberMktPage.name_sendnums, text)

	def input_name_nums(self,text):
		self.input_text(MemberMktPage.name_nums, text)

	def click_class_btnselectimg(self):
		self.click_element(MemberMktPage.class_btnselectimg)
		self.wait_until_page_contains_element("//input[@class='ke-button-common ke-button' and @value='确定']", settings.TIMEOUT)

	def input_name_givevalue(self, text):
		self.input_text(MemberMktPage.name_givevalue, text)

	def input_name_dmoney(self, text):
		self.input_text(MemberMktPage.name_dmoney, text)

	def click_class_iconbarchart(self, index):
		element_membermkt = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[1]/i[@class='icon-bar-chart']" %index
		element_car = "//table[@id='listTable']/tbody/tr[%s]/td[7]/a[2]/i[@class='icon-bar-chart']" %index

		if self.capture_exception(element_membermkt) == False:
			self.click_element(element_membermkt)
			self.wait_until_page_contains_element("is_use", settings.TIMEOUT)
		elif self.capture_exception(element_car) == False:
			self.click_element(element_car)
		else:
			print 'Not Match Element'

	def click_class_iconcog(self, index):
		self.click_element(MemberMktPage.class_iconcog %index)		

	''' 
	积分攻略
	'''

	def input_name_dayjf(self, text):
		self.input_text(MemberMktPage.name_dayjf, text)

	def input_name_dayjf6(self, text):
		self.input_text(MemberMktPage.name_dayjf6, text)

	def input_name_share(self, text):
		self.input_text(MemberMktPage.name_share, text)

	def input_name_zhuanfa(self, text):
		self.input_text(MemberMktPage.name_zhuanfa, text)

	def input_name_check(self, text):
		self.input_text(MemberMktPage.name_check, text)

	def input_name_voteselectvalue(self, text, index):
		"""Arg1 input content,Arg2 input index"""
		n = int(index)+4
		self.input_text(MemberMktPage.name_voteselectvalue %n, text)

	def click_class_iconminus(self, index):
		n = int(index)+4
		self.click_element(MemberMktPage.class_iconminus %n)

	''' 
	积分兑换
	'''
	def input_name_integral(self, text):
		self.input_text(MemberMktPage.name_integral, text)

	def input_name_numbertime(self, text):
		self.input_text(MemberMktPage.name_numbertime, text)

	def checkbox_name_ckmsg(self):
		self.click_element('ck_msg')

	''' 
	充值赠送
	'''
	def input_id_sendnumber(self, text):
		self.input_text(MemberMktPage.id_sendnumber, text)

	def click_id_sendmsg(self):
		self.click_element(MemberMktPage.id_sendmsg)

	def input_name_rechargevalue(self, text):
		self.input_text(MemberMktPage.name_rechargevalue)

	def input_name_integralvalue(self, text):
		self.input_text(MemberMktPage.name_integralvalue)

	def input_name_giveintegral(self, text):
		self.input_text(MemberMktPage.name_giveintegral, text)

	def input_name_couponvalue(self, text):
		self.input_text(MemberMktPage.name_couponvalue, text)

	def input_name_activitiesvalue(self, text):
		self.input_text(MemberMktPage.name_activitiesvalue, text)
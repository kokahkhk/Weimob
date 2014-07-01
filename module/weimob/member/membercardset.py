#coding=utf-8
'''
@author:wuxusheng
'''
import settings
import time
import sys
from lib.common import Common
reload(sys)
sys.setdefaultencoding('utf8')

class MembercardsetPage(Common):

	''' 
	卡片设置
	'''

	def input_id_cname(self, text):
		self.input_text("cname", text)

	def click_rel_iimg(self):
		self.click_element("//button[@rel='i-img']")
		self.wait_until_page_contains_element("//input[@class='ke-button-common ke-button' and @value='图片空间']", settings.TIMEOUT)

	def click_rel_mc(self):
		self.click_element("//button[@rel='mc']")
		self.wait_until_page_contains_element("//input[@class='ke-button-common ke-button' and @value='图片空间']", settings.TIMEOUT)

	def click_rel_iimgbg(self):
		self.click_element("//button[@rel='mc']")
		self.wait_until_page_contains_element("//input[@class='ke-button-common ke-button' and @value='图片空间']", settings.TIMEOUT)

	def radio_name_isshow_1(self):
		self.click_element("//div[@class='control-group'][6]/div/label[1]/input")

	def radio_name_isshow_0(self):
		self.click_element("//div[@class='control-group'][6]/div/label[2]/input")

	def radioe_name_khtype_1(self):
		self.click_element("//input[@type='radio' and @name='kh_type' and @value='1']")		

	def radioe_name_khtype_0(self):
		self.click_element("//input[@type='radio' and @name='kh_type' and @value='0']")

	def radio_name_khtype_2(self):
		self.click_element("//input[@type='radio' and @name='kh_type' and @value='2']")

	def radio_name_proving_1(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz1' and @name='proving']")

	def radio_name_proving_0(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz0' and @name='proving']")

	def radio_name_isrecharge_1(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz1' and @name='is_recharge']")

	def radio_name_isrecharge_0(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz0' and @name='is_recharge']")

	def radio_name_ispayment_1(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz1' and @name='is_payment']")

	def radio_name_ispayment_0(self):
		self.clear_input()
		self.click_element("//input[@id='proving_yz0' and @name='is_payment']")

	def clear_input(self):
		self.input_text('password','')

	def input_id_password(self,text):
		self.input_text('password',text)

	def input_id_description(self, text):
		self.input_text('description', text)

	''' 
	会员卡资料设置
	'''

	def checkbox_name_nameisedit(self):
		self.click_element("name_is_edit")

	def checkbox_name_phoneisedit(self):
		self.click_element("phone_is_edit")

	def checkbox_name_birthdayismust(self):
		self.click_element("birthday_is_must")

	def checkbox_name_birthdayisedit(self):
		self.click_element("birthday_is_edit")

	def checkbox_name_genderismust(self):
		self.click_element("gender_is_must")

	def checkbox_name_addressismust(self):
		self.click_element("address_is_must")

	def checkbox_name_txtismust(self, index):
		self.click_element("txt_is_must%s" %index)

	def checkbox_name_txtisupdate(self, index):
		self.click_element("txt_is_update%s" %index)

	def click_id_add(self, index):
		self.click_element("add%s" %index)

	def click_id_sadd(self, index):
		self.click_element("sadd%s" %index)

	def click_id_dodelit(self, index):
		self.click_element("//tr[@id='trtxt%s']/td/p/a[(text()='删除')]" %index)

	def click_id_sdodelit(self, index):
		self.click_element("//tr[@id='trtxt%s']/td/p/a[(text()='删除')]" %index)

	''' 
	会员卡特权
	'''

	def click_addmemberprivilege(self):
		self.click_element("//a[@class='btn' and i/@class='icon-plus']")

	def input_id_shorttitle(self, text):
		self.input_text("short_title", text)

	def checkbox_class_selectmemberall(self):
		self.click_element("//input[@class='select-member-all']")

	def checkbox_class_withcheckbox(self, index):
		self.click_element("//td[@class='with-checkbox'][%s]/input" %index)

	def click_class_icontrash(self, index):
		self.click_element("//i[@class='icon-trash']")

	def checkbox_name_show(self, index):
		element = "//table[@id='listTable']/tbody/tr[%s]/td/label/input[1]" %index
		self.click_element(element)
		self.get_element_attribute("%s@is_show" %element)
		time.sleep(5)


	''' 
	业务关联
	'''

	def click_id_addmenu(self):
		self.click_element("add_menu")

	def input_name_name(self, text):
		self.input_text('name', text)

	def input_name_order(self, number):
		self.input_text('order', number)

	''' 
	等级设置
	'''

	def radio_name_basic_totalscore(self):
		self.click_element("//label[@class='radio inline'][1]/input[@name='basis']")

	def radio_name_basic_totalconsume(self):
		self.click_element("//label[@class='radio inline'][2]/input[@name='basis']")

	def input_id_sxname(self, text):
		self.input_text('sxname', text)

	def input_id_sxstarjf(self, text):
		self.input_text('sxstarjf', text)

	def click_id_changegrade(self):
		self.click_element('changegrade')

	def click_id_addrank(self):
		self.click_element('addrank')

	def input_id_addname(self, index, text):
		self.input_text("add[name][%s]" %index, text)

	def input_id_addstartjf(self, index, text):
		self.input_text("add[startjf][%s]" %index, text)

	def input_id_addendjf(self, index, text):
		self.input_text("add[endjf][%s]" %index, text)

	def input_id_zk(self, index, text):
		self.input_text("add[zk][%s]" %index, text)

	def click_class_del(self, index):
		self.click_element("//table[@id='rank_table']/tbody/tr[%s]/td[4]/a" %index)





from Selenium2Library import Selenium2Library
import re
import win32com.client
from selenium import webdriver

class Common(Selenium2Library):
	_browser = None
	autoit = win32com.client.Dispatch("AutoItX3.Control")
	
	@property
	def start_browser(self):
		return self._browser

	@start_browser.setter
	def start_browser(self, value):
		self._browser = value[1]
	
	def start_page(self, url, browser='firefox', alias=None, remote_url=False,
                desired_capabilities=None, ff_profile_dir=None):
		self.start_browser = self.open_browser(url, browser, alias=None, remote_url=False,
                desired_capabilities=None, ff_profile_dir=None)

	def get_new_window(self, title):		
		for handle in self._browser.window_handles:
			self._browser.switch_to_window(handle)
			_title = self._browser.title
			if re.match(r".*%s.*" %title ,_title) != None:
				new_handle = handle
				break
			else:
				new_handle = None

		if new_handle == None:
			raise ValueError("Title didn't match")
		else:
			pass

	def close_new_window(self, title):
		self.get_new_window(title)
		return self._browser.close()
	
	def return_main_window(self):
		return self._browser.switch_to_window(self._browser.window_handles[0])

	def scroll_down(self):
		self.autoit.Send("{PGDN}")

	def capture_exception(self, element):
		try:
			self.element_should_be_visible(element)
			value = False
		except:
			value = True
		return value

	def enter_tab(self, index):
		self.autoit.Send("{TAB} %s" %index)

	def enter_send(self, text):
		self.autoit.Send(text)
				


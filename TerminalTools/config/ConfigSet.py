#-*-coding:UTF-8-*-
__author__ = 'fxf'

from ConfigParser import ConfigParser

class ConfigSet(object):
	
	config_file = None
	config = None
	config_path = ''
	
	def __init__(self, config_file):
		self.config_file = config_file
		self.config = ConfigParser()
		self.config.read(config_file)
	
	def get(self,section = '',key = ''):
		if self.config is None:
			raise IOError("Can't find config files")
		return self.config.get(section, key)
	
	def get_file_list(self,section = '', key = ''):
		if self.config_file is None:
			raise IOError("Can't find config files")
		list_str = self.config.get(section, key)
		if list_str is None or list_str == '':
			return []
		return [item.strip() for item in list_str.split(',')]

	def get_keyword_list(self,section = '', key = ''):
		if self.config_file is None:
			raise IOError("Can't find KEYWORD files")
		list_str = self.config.get(section, key)
		if list_str is None or list_str == '':
			return []
		return [item for item in list_str.split(',')]
	
	def get_version_list(self, section = '', key = ''):
		if self.config_file is None:
			raise IOError("Can't find config files")
		list_str = self.config.get(section, key)
		if list_str is None or list_str == '':
			return []
		return [item.lstrip().rstrip('.zip') for item in list_str.split(',')]
		
if __name__ == '__main__':
	config = ConfigSet('result-analyzer/check-keyword.ini')
	print config.get_keyword_list('analyzer','keyword')
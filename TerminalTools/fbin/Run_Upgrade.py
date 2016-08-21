#-*-coding:UTF-8-*-
__author__ = 'fxf'

import sys

from analyzer.ResultAnalyzer import ResultAnalyzer
from config.ConfigSet import ConfigSet
from modules.FileControl import FileControl
from modules.ServerControl import ServerControl
from modules.BoxControl import BoxControl

class Run_Upgrade(object):
	
	def __init__(self):
    	config = ConfigSet('config/resource/upgrade.ini')
		self.paths_config = dict()
		self.files_config = dict()
		self.paths_config['version_download'] = config.get('path','version_download')
		self.paths_config['version_url'] = config.get('path','version_url')
		self.paths_config['result_url'] = config.get('path','result_url')
		self.paths_config['server_url'] = config.get('path','server_url')
		self.paths_config['update_url'] = config.get('path','update_url')
		self.files_config['update_file'] = config.get('file','update_file')
		self.files_config['filelist_xml'] = config.get('file','filelist_xml')
		self.files_config['changelog_xml'] = config.get('file','changelog_xml')
		self.files_config['server_start_file'] = config.get('file','server_start_file')
		self.files_config['server_stop_file'] = config.get('file','server_stop_file')
		self.files_config['target_version'] = config.get('upgrade','target_version')
		self.files_config['target_finger'] = config.get('upgrade','target_finger')
		self.files_config['now_version'] = config.get('upgrade','now_version')
		self.files_config['now_finger'] = config.get('upgrade','now_finger')
		self.version = config.get_version_list('version','full_version_list')
		self.full_version = config.get_file_list('version','full_version_list')
		self.path_version = config.get_file_list('version','path_version_list')
		self.finger = config.get_file_list('version','finger_version_list')
		
	def upgrade(self,item,version,nums):
		if item == 'tota':
			if version == 'now':
				md5_sum = FileControl().calMd5forfile(self.paths_config['version_download'] + self.files_config['now_version'])
				FileControl().filelist_xml(self.files_config['filelist_xml'],md5_sum) 
				FileControl().changelog_xml(self.files_config['changelog_xml'],self.files_config['now_version'].rstrip('.zip'))
				FileControl().inputupgradefile(self.paths_config['version_download']+self.files_config['now_version'],self.files_config['update_file'])
			elif version == 'target':
				md5_sum = FileControl().calMd5forfile(self.paths_config['version_download'] + self.files_config['target_version'])
				FileControl().filelist_xml(self.files_config['filelist_xml'],md5_sum) 
				FileControl().changelog_xml(self.files_config['changelog_xml'],self.files_config['target_version'].rstrip('.zip'))
				FileControl().inputupgradefile(self.paths_config['version_download']+self.files_config['target_version'],self.files_config['update_file'])
			elif version == 'path':
				md5_sum = FileControl().calMd5forfile(self.paths_config['version_download'] + self.path_version[nums])
				FileControl().filelist_xml(self.files_config['filelist_xml'],md5_sum) 
				FileControl().changelog_xml(self.files_config['changelog_xml'],self.files_config['now_version'].rstrip('.zip'))
				FileControl().inputupgradefile(self.paths_config['version_download']+self.path_version[nums],self.files_config['update_file'])
		a
			BoxControl().waittimes(10)
		elif item == 'pota':
			pass
		elif item == 'usb':
			BoxControl().upgrade_usb(self.paths_config['version_download'] + self.files_config['now_version'])
		else:	
			continue
	
		if item == 'tota':
			BoxControl().upgrade()
		else:
			continue
		if version == 'now' or item == 'target':
			BoxControl().waittimes(160)
		else:
			BoxControl().waittimes(60)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		if version == 'now':
			ResultAnalyzer().resultout(self.paths_config['result_url'],self.files_config['now_finger'])
		elif version == 'target':
			ResultAnalyzer().resultout(self.paths_config['result_url'],self.files_config['target_finger'])
		elif version == 'path':
			ResultAnalyzer().resultout(self.paths_config['result_url'],self.finger[nums])
			
	def tota(self,item,states):
		if item == 'auto':
			Run_Upgrade().upgrade('tota','now')
			if states == 'manual':
				raw_input("")
			Run_Upgrade().upgrade('tota','target')
			if states == 'manual':
				raw_input("")
			for version in self.full_version:
				Run_Upgrade().upgrade('tota','now')
				if states == 'manual':
				raw_input("")
				Run_Upgrade().upgrade('tota','path')
				if states == 'manual':
				raw_input("")
		elif item == 'full':
			Run_Upgrade().upgrade('tota','now')
			if states == 'manual':
				raw_input("")
			Run_Upgrade().upgrade('tota','target')
			if states == 'manual':
				raw_input("")
		elif item == 'path':
			for version in self.full_version:
				Run_Upgrade().upgrade('tota','now')
				if states == 'manual':
					raw_input("")
				Run_Upgrade().upgrade('tota','path')
				if states == 'manual':
					raw_input("")
		
		
	
		
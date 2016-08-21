#-*coding:UTF-8-*-
__author__='fxf'
import os
import sys
from analyzer.ResultAnalyzer import ResultAnalyzer
from config.ConfigSet import ConfigSet
from modules.FileControl import FileControl
from modules.ServerControl import ServerControl
from modules.BoxControl import BoxControl

class Upgrade_USB(object):
	config = ConfigSet('config/resource/upgrade.ini')
	paths_config = dict()
	files_config = dict()
	paths_config['version_download'] = config.get('path','version_download')
	paths_config['version_url'] = config.get('path','version_url')
	paths_config['result_url'] = config.get('path','result_url')
	paths_config['server_url'] = config.get('path','server_url')
	paths_config['update_url'] = config.get('path','update_url')
	files_config['update_file'] = config.get('file','update_file')
	files_config['filelist_xml'] = config.get('file','filelist_xml')
	files_config['changelog_xml'] = config.get('file','changelog_xml')
	files_config['server_start_file'] = config.get('file','server_start_file')
	files_config['server_stop_file'] = config.get('file','server_stop_file')
	files_config['target_version'] = config.get('upgrade','target_version')
	files_config['target_finger'] = config.get('upgrade','target_finger')
	files_config['now_version'] = config.get('upgrade','now_version')
	files_config['now_finger'] = config.get('upgrade','now_finger')
	version = config.get_version_list('version','full_version_list')
	full_version = config.get_file_list('version','full_version_list')
	path_version = config.get_file_list('version','path_version_list')
	finger = config.get_file_list('version','finger_version_list')
		
	def __init__(self):
		pass
	
	def upgrade_auto_full(self):
		BoxControl().upgrade_usb(Upgrade_USB.paths_config['version_download'] + Upgrade_USB.files_config['now_version'])
		BoxControl().waittimes(160)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		ResultAnalyzer().resultout(Upgrade_USB.paths_config['result_url'],Upgrade_USB.files_config['now_finger'])
		#
		BoxControl().upgrade_usb(Upgrade_USB.paths_config['version_download'] + Upgrade_USB.files_config['target_version'])
		BoxControl().waittimes(160)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		ResultAnalyzer().resultout(Upgrade_USB.paths_config['result_url'],Upgrade_USB.files_config['target_finger'])
	
	def upgrade_auto_path(self):
		nums = 0
		for version in Upgrade_USB.full_version:
			#
			BoxControl().upgrade_usb(Upgrade_USB.paths_config['version_download'] + version)
			BoxControl().waittimes(160)
			ServerControl().adb_usb_if()
			BoxControl().waittimes(90)
			ResultAnalyzer().resultout(Upgrade_USB.paths_config['result_url'],Upgrade_USB.finger[nums])
			#
			BoxControl().upgrade_usb(Upgrade_USB.paths_config['version_download'] + Upgrade_USB.path_version[nums])
			BoxControl().waittimes(60)
			ServerControl().adb_usb_if()
			BoxControl().waittimes(90)
			ResultAnalyzer().resultout(Upgrade_USB.paths_config['result_url'],Upgrade_USB.files_config['target_finger'])
			nums += 1

if __name__ == '__main__':
	upgrade = Upgrade_USB()
	upgrade.upgrade_auto_full()
	upgrade.upgrade_auto_path()

	
	
		
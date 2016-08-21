#-*coding:UTF-8-*-
__author__='fxf'
import sys
#sys.path.append("./")
from analyzer.ResultAnalyzer import ResultAnalyzer
from config.ConfigSet import ConfigSet
from modules.FileControl import FileControl
from modules.ServerControl import ServerControl
from modules.BoxControl import BoxControl

class Upgrade_OTA(object):
	
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
		ServerControl().apache_control(Upgrade_OTA.files_config['server_start_file'])

		md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.files_config['now_version'])
		FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
		FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.files_config['now_version'].rstrip('.zip'))
		FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.files_config['now_version'],Upgrade_OTA.files_config['update_file'])
		BoxControl().waittimes(10)
		BoxControl().upgrade()
		BoxControl().waittimes(160)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		ResultAnalyzer().resultout(Upgrade_OTA.paths_config['result_url'],Upgrade_OTA.files_config['now_finger'])
	
		md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.files_config['target_version'])
		FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
		FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.files_config['target_version'].rstrip('.zip'))
		FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.files_config['target_version'],Upgrade_OTA.files_config['update_file'])
		BoxControl().waittimes(10)
		BoxControl().upgrade()
		BoxControl().waittimes(160)
		ServerControl().adb_usb_if()
		BoxControl().waittimes(90)
		ResultAnalyzer().resultout(Upgrade_OTA.paths_config['result_url'],Upgrade_OTA.files_config['target_finger'])
		#
		
	def upgrade_auto_path(self):
		nums = 0
		for version in Upgrade_OTA.full_version:
			#
			md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + version)
			FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
			FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],version.rstrip('.zip'))
			FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+version,Upgrade_OTA.files_config['update_file'])
			BoxControl().waittimes(10)
			BoxControl().upgrade()
			BoxControl().waittimes(160)
			ServerControl().adb_usb_if()
			BoxControl().waittimes(90)
			ResultAnalyzer().resultout(Upgrade_OTA.paths_config['result_url'],Upgrade_OTA.finger[nums])
			#
			md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.path_version[nums])
			FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
			FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.path_version[nums].rstrip('.zip'))
			FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.path_version[nums],Upgrade_OTA.files_config['update_file'])
			BoxControl().waittimes(10)
			BoxControl().upgrade()
			BoxControl().waittimes(60)
			ServerControl().adb_usb_if()
			BoxControl().waittimes(90)
			ResultAnalyzer().resultout(Upgrade_OTA.paths_config['result_url'],Upgrade_OTA.files_config['target_finger'])
			nums += 1
	
		ServerControl().apache_control(Upgrade_OTA.files_config['server_stop_file'])
	
	def upgrade_manual_full(self):
		ServerControl().apache_control(Upgrade_OTA.files_config['server_start_file'])
	
		md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.files_config['now_version'])
		FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
		FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.files_config['now_version'].rstrip('.zip'))
		FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.files_config['now_version'],Upgrade_OTA.files_config['update_file'])
		print ("Now version£º"+Upgrade_OTA.files_config['now_version']+"It will be update by yourself, just do it")
		raw_input("Please touch Enter after updated,it will be continue")

		md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.files_config['target_version'])
		FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
		FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.files_config['target_version'].rstrip('.zip'))
		FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.files_config['target_version'],Upgrade_OTA.files_config['update_file'])
		print ("Lasted Version£º"+Upgrade_OTA.files_config['target_version']+"It will be update by yourself, just do it")
		raw_input("Please touch Enter after updated,it will be continue")
		
		ServerControl().apache_control(Upgrade_OTA.files_config['server_stop_file'])
	
	def upgrade_manual_path(self):
		ServerControl().apache_control(Upgrade_OTA.files_config['server_start_file'])
		nums = 0
		for version in Upgrade_OTA.full_version:
			md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + version)
			FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
			FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.version.rstrip('.zip'))
			FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+version,Upgrade_OTA.files_config['update_file'])
			print ("Ready Version£º"+version+"It will be update by yourself, just do it")
			raw_input("Please touch Enter after updated,it will be continue")

			md5_sum = FileControl().calMd5forfile(Upgrade_OTA.paths_config['version_download'] + Upgrade_OTA.path_version[nums])
			FileControl().filelist_xml(Upgrade_OTA.files_config['filelist_xml'],md5_sum) 
			FileControl().changelog_xml(Upgrade_OTA.files_config['changelog_xml'],Upgrade_OTA.path_version[nums].rstrip('.zip'))
			FileControl().inputupgradefile(Upgrade_OTA.paths_config['version_download']+Upgrade_OTA.path_version[nums],Upgrade_OTA.files_config['update_file'])
			print ("Path Version£º"+Upgrade_OTA.path_version[nums]+"It will be update by yourself, just do it")
			raw_input("Please touch Enter after updated,it will be continue")
			nums += 1
	
		ServerControl().apache_control(Upgrade_OTA.files_config['server_stop_file'])
	

if __name__ == '__main__':
	upgrade = Upgrade_OTA()
	upgrade.upgrade_auto_full()
	upgrade.upgrade_auto_path()
	upgrade.upgrade_manual_full()
	upgrade.upgrade_manual_path()
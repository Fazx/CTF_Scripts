#!/usr/bin/env python
#coding=utf-8
#by p0

import sys
import os
import pwd
import hashlib
import datetime
import time
import getpass
import commands
import re

CURRENT_UID = pwd.getpwnam(getpass.getuser()).pw_uid
CURRENT_GID = pwd.getpwnam(getpass.getuser()).pw_gid

def scan_files(directory, prefix=None, postfix=None):
	file_list = []
	dir_list  = []
	directory = os.path.normpath(directory)
	for parent, dirnames, filenames in os.walk(directory):
		for dirname in dirnames:
			dir_list.append(os.path.join(parent, dirname))
		
		for filename in filenames:
			if postfix:
				if filename.endswith(postfix):
					file_list.append(os.path.join(parent, filename))
			elif prefix:
				if filename.startswith(prefix):
					file_list.append(os.path.join(parent, filename))
			else:
				file_list.append(os.path.join(parent, filename))
				
	return {'file': file_list, 'dir': dir_list}

def md5sum(filename):
	md5 = ''
	if os.access(filename, os.F_OK) and os.access(filename, os.R_OK):
		fd = open(filename, 'rb')
		fcont = fd.read()
		fd.close()
		md5 = hashlib.md5(fcont).hexdigest()
	return md5

def diff(src_dir, dst_dir):
	modified_file  = []
	deleted_file   = []
	added_file     = []
	modified_dir   = []
	deleted_dir    = []
	added_dir      = []
	
	src_dir = os.path.normpath(src_dir)
	dst_dir = os.path.normpath(dst_dir)
	
	src_scan_files = scan_files(src_dir)
	src_file_list  = src_scan_files['file']
	src_dir_list   = src_scan_files['dir']

	dst_scan_files = scan_files(dst_dir)
	dst_file_list = dst_scan_files['file']
	dst_dir_list  = dst_scan_files['dir']
	
	short_dst_file_list = []
	short_dst_dir_list  = []
	
	for dfile in dst_file_list:
		short_dst_file_list.append(dfile[len(dst_dir):])
		found = False
		for sfile in src_file_list:
			if dfile[len(dst_dir):] == sfile[len(src_dir):]:
				found = True
				if md5sum(dfile) != '' and md5sum(dfile) != md5sum(sfile):
					diff_content = commands.getoutput('diff {} {}'.format(sfile,dfile))
					diff_line = re.search('\d+(,\d+)?[acd]\d+(,\d+)?', diff_content).group()
					modified_file.append({
						'filename':dfile[len(dst_dir):],
						'line':diff_line,
						'content':diff_content
						})
				break
		if found == False:
			added_file.append(dfile[len(dst_dir):])

	for sfile in src_file_list:
		if sfile[len(src_dir):] not in short_dst_file_list:
			deleted_file.append(sfile[len(src_dir):])
	
	for ddir in dst_dir_list:
		short_dst_dir_list.append(ddir[len(dst_dir):])
		found = False
		for sdir in src_dir_list:
			if ddir[len(dst_dir):] == sdir[len(src_dir):]:
				found = True
				if os.stat(ddir).st_mode != os.stat(sdir).st_mode:
					modified_dir.append(ddir[len(dst_dir):])
				break
		if found == False:
			added_dir.append(ddir[len(dst_dir):])

	for sdir in src_dir_list:
		if sdir[len(src_dir):] not in short_dst_dir_list:
			deleted_dir.append(sdir[len(src_dir):])
			
	return {'modified_file': modified_file, 'deleted_file': deleted_file, 'added_file': added_file, 'modified_dir': modified_dir, 'deleted_dir': deleted_dir, 'added_dir': added_dir}


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print 'Usage: ' + sys.argv[0] + ' dir1 dir2'
		exit()
	
	diff_files = diff(sys.argv[1], sys.argv[2])
	print '--------------------修改文件及修改所在行--------------------'
	for diff_file in diff_files['modified_file']:
		print '~{}   {}'.format(diff_file['filename'],diff_file['line'])
	print '\n'

	print '--------------------删除文件--------------------'
	for deleted_file in diff_files['deleted_file']:
		print deleted_file
	print '\n'

	print '--------------------添加文件--------------------'
	for added_file in diff_files['added_file']:
		print added_file
	print '\n'

	print '--------------------修改目录--------------------'
	for modified_dir in diff_files['modified_dir']:
		print modified_dir
	print '\n'

	print '--------------------删除目录--------------------'
	for deleted_dir in diff_files['deleted_dir']:
		print deleted_dir
	print '\n'

	print '--------------------添加目录--------------------'
	for added_dir in diff_files['added_dir']:
		print added_dir
	print '\n'

	print '--------------------修改文件内容--------------------'
	for diff_file in diff_files['modified_file']:
		print '***{}***'.format(diff_file['filename'])
		print diff_file['content']
		print '\n'

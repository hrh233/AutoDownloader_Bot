#! usr/bin/python3
#coding:UTF-8

'''
		=============
		 Change Logs
		=============

****************************************
2023/04/09 :
添加了 "get_request" 函数
****************************************
'''

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

from urllib import request
import urllib.parse
import urllib.request

def get_request(url,flag,*file_root):
	'''
	用于http/https协议下的get请求
	url代表要请求的url,flag为返回方式:
		若flag为0,则返回明文或2进制数据
		若flag为1,则将得到的数据写入文件
	file_root为选填参数,代表请求的数据储存是时的目录,默认为'./'
	'''
	try:
		response = request.urlopen(url)
	except:
		print('[!]请求URL下的数据异常')
		return -1		#将函数以异常形式返回错误代
	
	content = response.read().decode("UTF-8",errors='ignore')	#读取数据并转码
	
	if flag == 0:		#以明文或数据输出并且返回
		print(content)	#打印数据
		return content	#返回数据
	elif flag == 1:		#将数据写入文件
		root = ''
		
		if file_root == None:	#如果未传递参数
			root = './'			#设置为默认目录
		
		else:					#如果传入参数
			root = file_root	#设置目录
		
		#获得文件名
		'''
		pass
		'''
		
		#写入文件
		file = open(root+filename,'w')	#以写的方式打开文件
		file.write(data)	#写入数据
		file.close()		#关闭文件
		return 0

def main():
	#获得视频BV号
	keyword = '1Na4y1T75k' #input("请输入视频BV号:")
	
	#合成为目标URL
	url = f'https://www.bilibili.com/video/BV{keyword}/'
	get_request(url,0)

if __name__ == '__main__':
	main()

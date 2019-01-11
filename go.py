from ftplib import FTP
import requests
import random
import time
import vk
import uuid
import os
import ftplib


def parser_file():
	readfile = 'source.txt'
	filename_result = 'no_short_links.txt'
	reader = open(readfile)
	for line in reader:
		unique_filename = str(uuid.uuid4())
		filename = 'parser_file/' + unique_filename + ".html"
		writer = open(filename, "w")
		file_to_text = "<!DOCTYPE html><html><head><title>" + unique_filename + "</title></head><body>" + line + "</body></html>"
		writer.write(file_to_text)
		writer.close()
		print('1_stage_parse_success')
	filename1 =	os.listdir(path='parser_file')
	new_wrt = open('no_short_links.txt', "a")
	for line in filename1:
		stroka = 'http://gruz4ik.tk/free/' + line +'\n'
		new_wrt.writelines(stroka)
	print('2_stage_parse_success')

def short():
	readfile = 'no_short_links.txt'
	url='http://vds2019.tk/api.php?key=V3xkVXYNwE7HgB1Yb0FiTEEKrcuXHBHrLHB536xKImNKu&url&url='
	reader = open(readfile)
	writer = open('short_link.txt', 'a')
	for line in reader:
		url2 = line
		host = url+url2
		post = requests.get(host)
		print(post.text)
		new_str = post.text + "\n"
		writer.write(new_str)
		time.sleep(1)
	print('short_success')

def vk_post():
	access_token='d91368b35e26bc61e27673db7ad6e74966f1d6f3cca99b2dcee00176a192076f33fb69992590f1a31d364'
	session = vk.Session(access_token=access_token)
	api = vk.API(session)
	reader = open("short_link.txt", "r")
	for line in reader:
         api.wall.post(owner_id='-23840424', message = line, v='5.92')
         time.sleep(3)
	print('vk_post_success')

def ftp_sync():
    ftp = ftplib.FTP('files.000webhost.com')
    ftp.login('vdsshop','modest12@')
    ftp.cwd('public_html/free')
    path = 'parser_file/'
    print (ftp.getwelcome())
    print (ftp.pwd())
    names = os.listdir(path='parser_file/')
    for file in names:
     wrie = path + file
     sendfile = open(wrie,'rb')
     ftp.storbinary('STOR ' +  file, sendfile)
     sendfile.close()
     time.sleep(0.1)
     print ("Uploaded " + file)
    ftp.quit()
    #print('ftp_update_success')

if __name__ == '__main__':
	parser_file()
	short()
	ftp_sync()
	vk_post()

#test-23840424 vds--162032252

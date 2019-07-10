from ftplib import FTP
import datetime
from os import path, mkdir


def grab_rwsa_data(url, username, password, working_dir, output_dir):
	ftp = FTP(url)
	ftp.login(user=username, passwd=password)
	ftp.cwd(working_dir)
	#ftp.dir()
	most_recent_date = datetime.date(2000,1,1)
	most_recent_file = str()
	for x in ftp.nlst():
		split_list = x.split('_')
		try:
			year = int(split_list[1])
			month = int(split_list[2])
			day = int(split_list[3].split('.')[0])
			d = datetime.date(year,month,day)
			if d > most_recent_date:
				most_recent_date = d
				most_recent_file = x
		except:
			pass

	filename = most_recent_file
	out_file = path.join(output_dir, filename)
	localfile = open(out_file, 'wb')

	ftp.retrbinary("RETR " + filename, localfile.write, 1024)
	ftp.quit()

	return out_file

def grab_acsa_data(url, username, password, working_dir, output_dir):
	ftp = FTP(url)
	ftp.login(user=username, passwd=password)
	for utility in ['Sanitary', 'Water']:
		ftp.cwd('/' + working_dir)
		most_recent_date = datetime.date(2000,1,1)
		most_recent_file = str()
		for x in ftp.nlst():
			split_list = x.split('_')
			try:
				if split_list[1] == utility and split_list[2].endswith('.gdb'):
					year = int(split_list[2][0:4])
					month = int(split_list[2][4:6])
					day = int(split_list[2][6:8])
					d = datetime.date(year,month,day)
					if d > most_recent_date:
						most_recent_date = d
						most_recent_file = x
			except:
				pass
		gdb = path.join(output_dir,most_recent_file)
		print(gdb)
		mkdir(gdb)
		print(ftp.pwd())
		ftp.cwd(most_recent_file)
		print(ftp.pwd())
		for x in ftp.nlst():
			filename = x
			out_file = path.join(gdb, x)
			localfile = open(out_file, 'wb')
			ftp.retrbinary("RETR " + filename, localfile.write, 1024)
	ftp.quit()

	#return out_file
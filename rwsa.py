from ftplib import FTP
import datetime

def login_ftp(url, username, password, working_dir):
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
	print(most_recent_date, most_recent_file)
	filename = most_recent_file
	localfile = open(filename, 'wb')

	ftp.retrbinary("RETR " + filename, localfile.write, 1024)
	ftp.quit()

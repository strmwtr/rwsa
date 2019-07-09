from ftplib import FTP

def login_ftp(url, username, password, working_dir):
	ftp = FTP(url)
	ftp.login(user=username, passwd=password)
	ftp.cwd(working_dir)
	ftp.dir()
	#filename = "RWSA_2019_06_10.gdb.zip"
	#localfile = open(filename, 'wb')

	#ftp.retrbinary("RETR " + filename, localfile.write, 1024)
	ftp.quit()

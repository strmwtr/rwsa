from ftplib import FTP


def login_ftp(url, username, password, working_dir):
	ftp = FTP(url)
	ftp.login(user=username, passwd=password)
	#ftp.dir()
	ftp.cwd(working_dir)
	ftp.dir()
	ftp.quit()

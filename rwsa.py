from ftplib import FTP


def login_ftp(url, username, password):
	ftp = FTP(url)
	ftp.login(user=username, passwd=password)
	#ftp.dir()
	ftp.cwd('GIS Files/RWSA')
	ftp.dir()
	ftp.quit()

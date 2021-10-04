def horario (s):
	h=(s//3600)
	m=(s//60-(h*60))
	seg=(s-(h*3600+m*60))
	print("{:02}:{:02}:{:02}".format(h,m,seg))
horario(3890)

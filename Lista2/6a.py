def propint (n):
	if 1000<=n<=9999:
		a=n//100
		b=n-a*100
		if (a+b)**2==n:
			return True
		else:
			return False
	else:
		return False
print(propint(315))

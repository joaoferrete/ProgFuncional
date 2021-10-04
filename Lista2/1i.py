def paroimpa (a,s,d,f,g):
	contapar=0
	contaimpar=0
	somapar=0
	somaimpar=0
	mediapar=0
	mediaimpar=0
	if a%2==0:
		contapar+=1
		somapar+=a
	else:
		contaimpar+=1
		somaimpar+=a
	if s%2==0:
		contapar+=1
		somapar+=s
	else:
		contaimpar+=1
		somaimpar+=s
	if d%2==0:
		contapar+=1
		somapar+=d
	else:
		contaimpar+=1
		somaimpar+=d
	if f%2==0:
		contapar+=1
		somapar+=f
	else:
		contaimpar+=1
		somaimpar+=f
	if g%2==0:
		contapar+=1
		somapar+=g
	else:
		contaimpar+=1
		somaimpar+=g
	if contapar!=0:
		mediapar=somapar/contapar
	if contaimpar!=0:
		mediaimpar=somaimpar/contaimpar
	return somapar, mediapar, somaimpar, mediaimpar
print(paroimpa(1,2,3,4,5))

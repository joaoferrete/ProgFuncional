tc1h = int(input("Digite o tempo do 1 corredor\nHora:    "))
tc1m = int(input("Minuto:  "))
tc1s = int(input("Segundo: "))

tc2h = int(input("Digite o tempo do 2 corredor\nHora:    "))
tc2m = int(input("Minuto:  "))
tc2s = int(input("Segundo: "))

if tc1h > tc2h:
	print("VENCEDOR: CORREDOR 2")
	difh = tc1h - tc2h
	if tc1m<tc2m:
		difh=difh-1
		tc1m+=60
		difm=tc1m - tc2m
		difs=tc1s - tc2s
		if tc1s < tc2s:
			difm = tc1m - tc2m 
			difm -= 1
			tc1s += 60
			difs = tc1s - tc2s

	elif tc1s < tc2s:
		difm = tc1m - tc2m 
		difm -= 1
		tc1s += 60
		difs = tc1s - tc2s
        
	else:
		difm = tc1m - tc2m
		difs = tc1s - tc2s
    
elif tc1h == tc2h and tc1m > tc2m:
	print("VENCEDOR: CORREDOR 2")
	difh = tc1h - tc2h
	difm = tc1m - tc2m
	if tc1s < tc2s:
		difm -= 1
		tc1s += 60
		difs = tc1s - tc2s
	else:    
		difs = tc1s - tc2s
elif tc1h == tc2h and tc1m == tc2m and tc1s > tc2s:
	print("VENCEDOR: CORREDOR 2")
	difm = tc1m - tc2m    
	difs = tc1s - tc2s
    
else:
	difh = tc2h - tc1h
	print("VENCEDOR: CORREDOR 1")
	if tc2m < tc1m:
		difh = difh - 1
		tc2m += 60
		difm = tc2m - tc1m
		difs = tc2s - tc1s
    
	elif tc2s < tc1s:
		difm = tc2m - tc1m 
		difm -= 1
		tc2s += 60
		difs = tc2s - tc1s
	else:  
		difm = tc2m - tc1m 
		difs = tc2s - tc1s
        
print("Diferença: {} horas {} minutos {} segundos".format(difh,difm,difs))


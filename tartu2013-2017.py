from pprint import pprint

vk = {}

i=1
j=1

l = {}

txt = open("tartu2013-2017.txt",'r').readlines()

for line in txt:
	st = line.split(" ")
	if len(st)>0 and st[0].count("*")==len(st[0]):
		v = line.strip("* \n")
		lev=st[0].count("*")
		if lev==1:
			vk[v]=[j, None]
			j += 1
			#print(vk[v], v)

cur=None

for line in txt:
	st = line.split(" ")
	if len(st)>0 and st[0].count("*")==len(st[0]):
		v = line.strip("* \n")
		lev=st[0].count("*")
		if lev==1:
			cur=vk[v][0]
		elif lev==2:
			vk[v]=[j, cur]
			j += 1
			#print(vk[v], v)

#pprint(vk, width=156)


valdkond = None
inlist = -1
inordlist = -1
sup="NULL"
insup = "NULL"

for line in txt:
	
	line=line.strip(" \n")
	
	if len(line)==0:
#		inlist=-1
#		sup="NULL"
		continue
		
	st = line.split(" ")
	if len(st)>0 and st[0].count("*")==len(st[0]):
		v = line.strip("* \n")
		try:
			valdkond = vk[v][0]
		except KeyError:
			pass
		sup = "NULL"
		inlist=-1
		if len(st[0])==1:
			#print(v.upper(), vk[v])
			pass
		else:
			#print("#", v, vk[v])
			pass
		continue

	if line[len(line)-1]==":":
		l[i]=[sup, valdkond, line]
		inlist=0
		sup = str(i)
		#print(">>> (" + str(sup) + ") "  +line)
	elif len(st)>=3 and st[1]=="–":
		if sup!="NULL":
			#print("* [" + str(sup) + "] "  +line)
			l[i]=[sup, valdkond, line]
		else:
			#print(line)
			l[i]=["NULL", valdkond, line]
	else:
		if sup!="NULL":
			#print("* [" + str(sup) + "] "  +line)
			l[i]=[sup, valdkond, line]
		else:
			#print(line, "(" + str(sup) + ")")
			l[i]=["NULL", valdkond, line]
		inlist=-1
		sup="NULL"

	i+=1
	if inlist >= 0: inlist+=1

lid=-1
lnr=-1

for x in l:
	st = l[x][2].split(". ")
	if len(st)>0 and st[0].isnumeric():
		if st[0]=="1":
			lid=x-1
			lnr=1
		if lnr>int(st[0])-3 and lnr<int(st[0])+3: # lubame hüppavaid numberloendeid
			#print(lnr, l[x][2][0:20])
			l[x][0]=lid
			lnr = int(st[0])+1
		else:
			#print(lnr, l[x][2][0:20])
			lid=-1
			lnr=-1

lid=None
oid=None
vid=None


for x in l:
	if vid != l[x][1]:
		for title, idv in vk.items():
			if idv[0] == l[x][1]:
				#print(idv[0], title)
				vid = idv[0]
				lid = None
				break

	if l[x][0] != "NULL" :
		st = l[x][2].split(". ")
		if len(st)>0 and st[0].isnumeric():
			#print(x, l[x][0], l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])
			pass
		else:
			#print(x, l[x][0], "\t* " + l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])
			pass
	else:
		#print(x, l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])
		pass

	if l[x][0]!="NULL": lid = l[x][0]






#pprint(l, width=156)

print("-- *** Lubaduste valdkonnad ***")

for v in vk:
		if vk[v][1] is not None:
			print("INSERT INTO lubadus_valdkond(valdkondid,ylemvaldkondid,pealkiri) VALUES ("+str(vk[v][0])+","+ str(vk[v][1]) + ",'"+ v +"');")
		else:
			print("INSERT INTO lubadus_valdkond(valdkondid,pealkiri) VALUES ("+str(vk[v][0])+",'"+ v +"');")


print("-- *** Lubadused ise ***")

for x in l:
	if vid != l[x][1]:
		for title, idv in vk.items():
			if idv[0] == l[x][1]:
				print("--", idv[0], title)
				vid = idv[0]
				lid = None
				break

	if l[x][0] != "NULL" :
		print("INSERT INTO lubadus(ylemlubadusid,lubadusid,mustpealkiri,valdkondid,koalitsioonid) VALUES ("+str(l[x][0])+", "+str(x)+", '"+ l[x][2] +"', "+str(l[x][1])+",19);")
	else:
		print("INSERT INTO lubadus(lubadusid,mustpealkiri,valdkondid,koalitsioonid) VALUES (" + str(x)+", '"+ l[x][2] +"', "+str(l[x][1])+",19);")

	if l[x][0]!="NULL": lid = l[x][0]

	#if valdkond is None:
	#	print("INSERT INTO lubadus(ylemlubadus,lubadusid,mustpealkiri) VALUES ("+sup+","+ str(i) + ",'"+ line +"');")
	#else:
	#	print("INSERT INTO lubadus(ylemlubadus,lubadusid,mustpealkiri) VALUES ("+sup+","+ str(i) + ",'"+ line +"', "+str(valdkond)+");")

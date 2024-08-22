mem=[] #main memory
memtab=[] #memGroup
proctab=[] #procedure
apptab=[] #application
mtns=[] #memGroup namespace
pcns=[] #procedure namespace
apns=[] #application namespace
mtli=0 #memtab last index
pcli=0 #proctab last index
apli=0 #apptab last index

#init  //each part of init is also a reference for applications

#init/mem
cnt=1024
while cnt:
  mem.append(0)
  cnt-=1

#init/SysMemGroup  //memGroup init ref
mcnt=8 #memGroupCount const
cnt=mcnt #memGroup count
while cnt:
  memtab.append([])
  msize=2 #memGroupSize const
  cnt0=msize #memGroup size
  while cnt0:
    memtab[mcnt-cnt].append((mcnt-cnt)*msize+msize-cnt0)
    cnt0-=1
  mtns.append('') #  //create an empty name
  cnt-=1

#init/SysApp  //register basic apps and procedures

#SysApp/namespace  //init SysApp for reserved names

#SysApp/namespace/memtab  //namespace ref
ccnt=4 #cnt const
cnt=ccnt #cnt var
nps='sys' #namePrefixString
while cnt:
  mtns[mtli+ccnt-cnt]=nps+str(ccnt-cnt)
  cnt-=1
mtli+=ccnt

ccnt=4 #cnt const
cnt=ccnt #cnt var
nps='sub' #namePrefixString
while cnt:
  mtns[mtli+ccnt-cnt]=nps+str(ccnt-cnt)
  cnt-=1
mtli+=ccnt

#SysApp/namespace/memNav  //namespace - memory association ref
def mn(obj): #memtab_namespace_addr  //returns memtab index
  return mtns.index(obj)
def ml(obj): #memtab_addr_list  //returns mem addresses inside
  return memtab[mn(obj)]
def mk(obj,addr): #memtab_addr  //returns mem addr
  return ml(obj)[addr]
def mm(obj,addr):
  return mem[mk(obj,addr)]

#SysApp/memory/proctab
mcnt=4 #procCount const
cnt=mcnt #procedure count
while cnt:
  proctab.append([])
  msize=2 #procMemSize const
  cnt0=msize #memGroup size
  while cnt0:
    proctab[mcnt-cnt].append(mtns[(mcnt-cnt)*msize+msize-cnt0])
    cnt0-=1
  pcns.append('') #  //create an empty name
  cnt-=1

#SysApp/namespace/proctab
ccnt=4 #cnt const
cnt=ccnt #cnt var
nps='proc' #namePrefixString
while cnt:
  pcns[pcli+ccnt-cnt]=nps+str(ccnt-cnt)
  cnt-=1
pcli+=ccnt

#debug
print(memtab)
print(mtns)
print(proctab)
print(pcns)
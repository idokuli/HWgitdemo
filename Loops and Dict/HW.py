#Lab From Class
list1 =[]
print("enter names of servers")
name = input()
list1.append(name)
print("enter names of servers")
name = input()
list1.append(name)
print("enter names of servers")
name = input()
list1.append(name)
print(f"the names of the servers are: {list1}")
dict = {}
for servername in list1:
    print(f"enter an IP for {servername}")
    srvip = input()
    dict [servername]= srvip
print(dict)
print("enter a server name to look for")
srvname = input()
if dict.get(srvname):
    print(srvname)
else:
    print("server name not found")
print("do you want to change ip? if so enter server name to change ip to")
srvname = input()
if dict.get(srvname):
    print("enter a new ip")
    newip = input()
    dict[srvname] = newip
print(dict)
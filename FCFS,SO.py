print("FIRST COME FIRST SERVE SCHEDULLING")
n= int(input("Masukan Jumlah Proses : "))
d = dict()
 
for i in range(n):
    key = "P"+str(i+1)
    a = int(input("Masukkan Arrival Time Proses"+str(i+1)+": "))
    b = int(input("Masukan Burst Time Proses"+str(i+1)+": "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l
 
d = sorted(d.items(), key=lambda item: item[1][0])
 
Eks = []
for i in range(len(d)):
    # first process
    if(i==0):
        Eks.append(d[i][1][1])
 
    # get prevET + newBT
    else:
        Eks.append(Eks[i-1] + d[i][1][1])
 
TAT = []
for i in range(len(d)):
    TAT.append(Eks[i] - d[i][1][0])
 
WT = []
for i in range(len(d)):
    WT.append(TAT[i] - d[i][1][1])
 
avg_WT = 0
for i in WT:
    avg_WT +=i
avg_WT = (avg_WT/n)
 
print("Proses | Arrival | Burst | Eksekusi | Turn Around | Wait |")
for i in range(n):
      print("   ",d[i][0],"  |   ",d[i][1][0]," |   ",d[i][1][1]," |   ",Eks[i],"  |   ",TAT[i],"  |  ",WT[i],"  |  ")
print("Average Waiting Time: ",avg_WT)
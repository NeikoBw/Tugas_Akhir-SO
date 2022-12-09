import os
import copy
import random
from time import sleep

class Queue:
    def __init__(self):
        self.queue = []
        self.showQ = []
        self.size = 0
        self.firstArrival = 0

    def enqueue(self,data):
        if self.isEmpty():
            self.firstArrival = data[2]
            data[2] = 0
            self.queue.append(data)
            self.size += 1
        else:
            data[2] -= self.firstArrival
            self.queue.append(data)
            self.size += 1
    
    def dequeue(self):
        execP = self.queue.pop(0)
        for i in self.showQ:
            if i == execP:
                self.showQ.remove(i)
                break
        self.size -= 1
        return execP
    
    # def waitingT(self):
    #     for i in range(len(self.queue)):
    #         if i != 0:
    #             et = 0
    #             for j in range(i):
    #                 et += self.queue[j][1]
    #             et -= self.queue[i][2]
    #             self.wtList.append(et)
    #         else:
    #             self.wtList.append(0)
    #     return sum(self.wtList) / len(self.wtList)

    # def turnaroundT(self):
    #     for i in range(len(self.queue)):
    #         tt = self.wtList[i] + self.queue[i][1]
    #         self.ttList.append(tt)
    #     return sum(self.ttList) / len(self.ttList)

    def isEmpty(self):
        return self.size == 0


if __name__ == '__main__':
    #bagian input user
    i = 1
    readyQ = Queue()
    inputloop = True
    while inputloop:
        arrivalt = int(input(f'Masukkan Waktu Kedatangan nasabah {i}: '))
        burstt = random.randint(5,30)
        readyQ.enqueue([f'Nasabah {i}',burstt,arrivalt])
        readyQ.queue.sort(key = lambda a: a[2])
        i += 1
        loopcheck = input('Ingin tambah antrian lagi? (ketik n bila tidak)\n')
        if loopcheck.lower() == 'n':
            inputloop = False
    os.system('cls')
    
    #pencadangan dan penghitungan rata2 (karena baris selanjutnya akan menghapus data dalam queue)
    listCadangan = copy.deepcopy(readyQ.queue)

    #penampilan serta penghapusan data (berdasarkan prinsip FCFS)
    count = 0
    while readyQ.isEmpty() == False:           
        exec = readyQ.dequeue()
        while exec[1] > 0:
            print(f'time count = {count} menit')
            print('\nNasabah sedang dilayani')
            print(f'|{exec[0]}  {exec[1]}',end='menit |\n\n')
            for i in readyQ.queue:
                if i[2] == count:
                    readyQ.showQ.append(i)
            print('Nasabah dalam antrian')
            for j in readyQ.showQ:
                print(f'|{j[0]}  {j[1]}',end='menit |')
            exec[1] -= 1
            count += 1
            print()
            sleep(2)
            os.system('cls')

    #tampilan hasil akhir
    print('Gantt Chart')
    print('|',end='')
    for i in listCadangan:
        print(i[0],' ',i[1],end='menit |')
    # print('\n\nArrival Time')
    # for i in listCadangan:
    #     print(i[0],':',i[2])
    # print('\nRata-rata Waiting Time =',avgWT)
    # print('Rata-rata Turnaround Time =',avgTT)
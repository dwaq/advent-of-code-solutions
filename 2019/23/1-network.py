import threading
from queue import Queue
import time

class intCode(threading.Thread):
    def __init__(self, queue, args=(), kwargs=None):
        threading.Thread.__init__(self, args=(), kwargs=None)
        self.queue = queue
        self.daemon = True
        self.network_address = args[0]
        self.network_assigned = False
        self.output = []
        self.input = Queue()

    def getInput(self):
        # start by setting network address
        if (self.network_assigned == False):
            self.network_assigned = True
            print("Assigned network address", self.network_address)
            return self.network_address
        # then get data from queue
        else:
            # start by checking input queue
            if(not self.input.empty()):
                return self.input.get()

            # then move onto spare queue
            # return -1 if empty
            if (self.queue.empty()):
                #print("Empty queue!")
                #time.sleep(1)
                return -1
            else:
                # this allows you to see the queue without popping data
                # (so that other intcode computers can access it)
                data = self.queue.queue[0]
                #print("Data:", data)
                # only use the data if it was assigned 
                if (data[0] == self.network_address):
                    # getting it pops it from the queue
                    data = self.queue.get()
                    print(self.network_address, "getting data:", data)
                    # append X and Y to input queue
                    self.input.put(data[1])
                    self.input.put(data[2])

                    # return whatever is on top
                    return self.input.get()
                # otherwise return -1 again
                else:
                    return -1

    def sendOutput(self, o):
        #print("output:", o)
        # append data to output array
        self.output.append(o)
        # when it's full (3 items)
        if (len(self.output) == 3):
            print(self.network_address, "sending packet:", self.output)

            # check for the answer to this part
            if (self.output[0] == 255):
                print("First Y value sent to address 255:", self.output[2])
                exit()

            # put that packet on the queue for another device to take it
            self.queue.put(self.output)
            # clear output queue
            self.output = []

    def run(self):
        # relative base
        relativeBase = 0

        intcode =[]
        with open("intcode.txt", "r") as fp:
            for f in (fp):
                instructions = f.split(",")

        # convert all numbers to int
        instructions = [int(x) for x in instructions]

        # append a bunch of stuff to instructions so it doesn't get overrun
        for i in range(8000):
            instructions.append(0)

        # current instruction pointer
        ip = 0

        # end at 99
        while(instructions[ip] != 99):
            # current op code (lowest 2 digits)
            i = instructions[ip]%100
            
            # get mode of each parameter
            # // does floor division (no floats)
            # %10 only gets that digit
            mode1 = (instructions[ip]//  100)%10
            mode2 = (instructions[ip]// 1000)%10
            mode3 = (instructions[ip]//10000)%10

            if (mode1 == 0):
                try:
                    a = instructions[instructions[ip+1]]
                except:
                    a = None
            elif(mode1 == 1):
                try:
                    a = instructions[ip+1]
                except:
                    a = None
            elif (mode1 == 2):
                try:
                    a = instructions[instructions[ip+1]+relativeBase]
                except:
                    a = None
            else:
                print("Mode1 Error")

            if (mode2 == 0):
                try:
                    b = instructions[instructions[ip+2]]
                except:
                    b = None
            elif(mode2 == 1):
                try:
                    b = instructions[ip+2]
                except:
                    b = None
            elif (mode2 == 2):
                try:
                    b = instructions[instructions[ip+2]+relativeBase]
                except:
                    b = None
            else:
                print("Mode2 Error")

            if (mode3 == 0):
                try:
                    c = 0
                except:
                    c = None
            elif(mode3 == 1):
                try:
                    # issue
                    print("Mode3==1 not accounted for!")
                    break
                    #c = instructions[ip+3]
                except:
                    c = None
            elif (mode3 == 2):
                try:
                    c = relativeBase
                except:
                    c = None
            else:
                print("Mode3 Error")

            #if(mode3):
            #    print(instructions[ip], i, (mode1, mode2, mode3), (a, b), relativeBase)
            #print( i, (a, b), relativeBase)
            #print(instructions)

            if(i==1):
                instructions[instructions[ip+3]+c] = a+b

                ip += 4
            elif(i==2):
                instructions[instructions[ip+3]+c] = a*b

                ip += 4
            elif(i==3):
                # take an input and store it at address given by parameter
                if (mode1 == 0):
                    instructions[instructions[ip+1]] = self.getInput()
                elif(mode1 == 1):
                    instructions[ip+1] = self.getInput()
                elif (mode1 == 2):
                    instructions[instructions[ip+1]+relativeBase] = self.getInput()
                ip += 2
            elif(i==4):
                # outputs the value of its only parameter
                #outputValue = a
                self.sendOutput(a)
                #print("Output at", ip, "is", a)
                ip += 2
            elif(i==5):
                # jump if true
                if (a != 0):
                    ip = b
                else:
                    ip += 3
            elif(i==6):
                # jump if false
                if (a == 0):
                    ip = b
                else:
                    ip += 3
            elif(i==7):
                # less than
                instructions[instructions[ip+3]+c] = int(a<b)

                ip+=4
            elif(i==8):
                # equals
                instructions[instructions[ip+3]+c] = int(a==b)

                ip+=4
            elif(i==9):
                # adjusts the relative base by the value of its only parameter
                relativeBase += a
                ip += 2
            else:
                print("ERROR")


if __name__ == '__main__':
    threads = []
    # 50 computers
    for t in range(50):
        q = Queue()
        threads.append(intCode(q, args=(t,)))
        threads[t].start()

    for t in threads:
        t.join()
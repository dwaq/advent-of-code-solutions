class Intcode:
    def __init__(self, phase, tape):
        self.phase = phase
        self.t = tape
        self.ip = 0
        self.isHalted = False
        self.output = 0
        # Incremented to keep track of how many inputs have been entered before.
        self.inputOccurrence = 0

    def halted(self):
        return self.isHalted

    def getOutput(self):
        return self.output

    def run(self, inp):
        while True:
            # current op code (lowest 2 digits)
            op = self.t[self.ip]%100

            # get mode of each parameter
            # // does floor division (no floats)
            # %10 only gets that digit
            mode1 = (self.t[self.ip]//  100)%10
            mode2 = (self.t[self.ip]// 1000)%10
            mode3 = (self.t[self.ip]//10000)%10

            try:
                a = self.t[self.ip+1] if mode1 else self.t[self.t[self.ip+1]]
            except IndexError:
                pass

            try:
                b = self.t[self.ip+2] if mode2 else self.t[self.t[self.ip+2]]
            except IndexError:
                pass

            #print(self.t)
            #print(self.t[self.ip], op, mode1, mode2, mode3)

            if(op==1):
                self.t[self.t[self.ip+3]] = a+b

                self.ip += 4
            elif(op==2):
                self.t[self.t[self.ip+3]] = a*b

                self.ip += 4
            elif(op==3):
                # take an input and store it at address given by parameter
                # first time takes the phase, after that, take the input
                inputData = self.phase if self.inputOccurrence==0 else inp
                self.t[self.t[self.ip+1]] = inputData
                # increase number of times seen
                self.inputOccurrence+=1
                self.ip += 2
            elif(op==4):
                # outputs the value of its only parameter
                self.output = a
                self.ip += 2
                # move to next amp
                break
            elif(op==5):
                # jump if true
                if (a != 0):
                    self.ip = b
                else:
                    self.ip += 3
            elif(op==6):
                # jump if false
                if (a == 0):
                    self.ip = b
                else:
                    self.ip += 3
            elif(op==7):
                # less than
                if (mode3):
                    self.t[self.ip+3] = int(a<b)
                else:
                    self.t[self.t[self.ip+3]] = int(a<b)

                self.ip+=4
            elif(op==8):
                # equals
                if (mode3):
                    self.t[self.ip+3] = int(a==b)
                else:
                    self.t[self.t[self.ip+3]] = int(a==b)

                self.ip+=4
            elif(op == 99):
                self.isHalted = True
                break
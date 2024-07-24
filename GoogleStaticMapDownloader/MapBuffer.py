class Circular512:
    def __init__(self, buffer_size=10):
        self.buffer_size = buffer_size
        self.buffer = [None]*buffer_size
        self.tailIndex = -1
        self.headIndex = 0
        self.size = 0

    def enQueue(self,newElement):
        if self.size == self.buffer_size:
            print("Buffer is full")
            return
        else:
            self.tailIndex = (self.tailIndex + 1) % self.buffer_size
            self.buffer[self.tailIndex] = newElement
            self.size = self.size + 1 
        
    def deQueue(self):
        tmp = 0
        if self.size == 0:
            print("Buffer is empty")
        else:
            tmp = self.buffer[self.headIndex]
            self.headIndex = (self.headIndex + 1) % self.buffer_size
            self.size = self.size - 1
            return tmp

    def display(self):
        if self.size == 0:
            print("Buffer is empty")
        else:
            index = self.headIndex
            for i in range(self.size):
                print(self.buffer[index])
                index = (index + 1) % self.buffer_size


#######################################################
#                     Çalıştı                         #
# obje = CircularBufferV1()                           #  
# while True:                                         #
#     print("DENEME  bir kaç işlem\n eq-dq-dp-quit")  #  
#     command = input("Enter command: ")              #      
#     if command == "quit":                           #      
#         break                                       #                  
#     elif command == "eq":                           #          
#         print("Enter a value for enqueueing: ")     #                  
#         element = int(input("Value: "))             #                          
#         obje.enQueue(element)                       #                      
#     elif command == "dq":                           #              
#         obje.deQueue()                              #                  
#     elif command == "dp":                          #                       
#         obje.display()                              #                  
#     else:                                           #                          
#         print("Invalid operation. Try again.")      #              
#######################################################
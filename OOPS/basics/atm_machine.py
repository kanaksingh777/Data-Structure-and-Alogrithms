class Atm:
    __counter =8  # serializing the atm ,with a class variable/static variable  making it private also 



    #special method /magic method / dunder method


    def __init__(self):  #constructor   #hdfc is self -- basically the instance is self
        print("constructor Initiated")
        self.__pin = ""
        self.__balance = 0

        self.serial_no = Atm.__counter   #class variable are accessed by class name and then class variable
        Atm.counter = Atm.counter + 1




        print(id(self))
        


        self.__menu()

    def get_pin(self):
        return self.__pin
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("Pin changed successfull")

    @staticmethod
    def get_counter():
        return Atm.__counter
    

    @staticmethod
    def set_counter(new):
        if type(new) == int :
            Atm.__counter == new
        else: 
            print("Not allowed")


    def __menu(self):
        while True: 
            
            user_input = input("""   
                            Hello , How would you like to proceed? 
                            1.Enter 1 to create pin
                            2.Enter 2 to deposit 
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to exit
                                """)
            
            if user_input == "1":
                self.create_pin()
                

            elif user_input == "2" :
                self.deposit()
                

            elif user_input == "3":
                self.withdraw()
                
            elif user_input == "4":
                self.check_balance()
            
            elif  user_input == "5":
                print("bye")
                break 

    def create_pin(self):
        print("inside_print")
        self.__pin = input("enter your pin")
        print("pin set successfully")

    def deposit(self):
        temp_pin = input("enter you pin")
        if temp_pin == self.__pin:

            amount = int(input("Enter the amount you want to deposit."))
            self.__balance = self.__balance + amount 
            print("deposit successful")

        else: 
            print("Invalid pin")

    def withdraw(self):
        temp_pin = input("enter you pin")
        if temp_pin == self.__pin:
            amount = int(input("Enter the amount you want to withdraw."))
            if amount > self.__balance:
                print("Insufficient funds")
                return 
                
            self.__balance = self.__balance - amount 
            print("withdrawal successful")
        else: print("invalid pin")

    def check_balance(self):
        temp_pin = input("enter you pin")
        if temp_pin == self.__pin:
            print(f"Balance : {self.__balance}")

        else : 
            print ("invalid pin")


    


hdfc = Atm()
sbi = Atm()
llyod = Atm()

print(hdfc.serial_no)

print(sbi.serial_no)

print(llyod.serial_no)




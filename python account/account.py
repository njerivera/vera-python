from datetime import datetime
class Account:
    def __init__ (self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.loan=0
    def welcome(self):
        return "Hello {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
    def deposit(self,z):
        time = datetime.now()

        object = {"time":time,"amount":z}
        self.deposits.append(object)
        
        self.balance=self.balance + z
        text="Hello {} {} you have deposited {}".format(self.first_name,self.last_name,z)
        return text
    def withdraw(self,p):
        time = datetime.now()
        object = {"time":time,"amount":p}
        self.withdrawals.append(object)
        withdraw=p
        if p>self.balance:

           return "can't withdraw"
        else :
            self.balance=self.balance -p
            message="Hello {} {} you have withdrawn {}".format(self.first_name,self.last_name,p)
            return message
        
    def showbalance(self):
        showbalance = self.balance
        text="Hello {} {} your new balance is {}".format(self.first_name,self.last_name,self.balance)
        return text
    def show_deposits(self):
        for z in self.deposits:

             time = z["time"]

             formatted_time = time.strftime("%c")
             amount = z["amount"]
             print("On {} you deposited {}".format(formatted_time,amount))
        # for m in self.deposits:
    #     #     print(m)
    def show_withdrawals(self):
        for p in self.withdrawals:
            time = p["time"]
            formatted_time=time.strftime("%c")
            amount = p["amount"]
            print("On {} you withdrew {}".format(formatted_time,amount))
        # for m in self.withdrawals:
        #     print(m)

    def give_loan(self,get_loan):

        loan = get_loan
        total = 0
        for x in self.deposits:
            amount = x["amount"]
            total+=amount

        

        if len(self.deposits)>=5 and get_loan<=total/3 and self.loan==0:
            self.loan = self.loan + get_loan
            print("Dear customer your loan request of {} has been approved".format(get_loan))
        else:
            print("loan denied")
        

        

        
    def repay_loan(self,pay):


        loan = pay
        self.loan.extend(pay)
        self.loan = self.loan-pay
        excess_payment = self.deposit.append(deposit)
        message = "Hello {} {} you have paid {} you remainder is {}".format(pay,self.loan)
        print(message)
        
        # if pay<self.loan:

          
 #            print("Dear customer your remaining loan balance is {}".format(self.loan))
 #        elif pay>self.loan:
 #            extra_money = pay - self.loan
 #            self.loan = pay - extra_money - self.loan
           
 #            self.balance = extra_money+self.balance
 #        elif pay == self.loan:
 #            self.loan = self.loan-pay
 # #           
class Line:
    
    def __init__(self,coor1,coor2):
      self.coor1 = coor1
      self.coor2 = coor2
        
    
    def distance(self):
        self.difference2 = self.coor2[1] - self.coor1[1]
        self.difference1 = self.coor2[0]  - self.coor1[0]
        sum = self.difference1 ** 2 + self.difference2 ** 2
        
        return sum**.5
    
    def slope(self, ):
       self.difference2 = self.coor2[1] - self.coor1[1]
       self.difference1 = self.coor2[0]  - self.coor1[0]
       slope1 = self.difference2/self.difference1
       return slope1
      
l1 = Line((1,2), (3,2)) 
print(l1.slope())
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
         vol = (self.radius ** 2) * 3.14 
         return vol 
    def surface_area(self):
        sa  = self.radius  * 2 * 3.14
        return sa
        pass
c1 = Cylinder(2, 3)      
print(c1.volume())
""" For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn."""
class Account:
  def __init__(self, owner, balance):
    self.balance = balance
    self.owner = owner
  def __str__(self):
    return 'Account owner: {}, Account balance: {}'.format(self.owner, self.balance)
  def deposit(self, num):
    self.balance = num + self.balance
    print("{} has been Deposited!".format(num))
    return ('Updated balance: {}'.format(self.balance))
  def withdraw(self, num):
    self.balance = self.balance - num
    print("{} has been Withdrawed!".format(num))
    return ('Current balance: {}'.format(self.balance))
a1 = Account('Sduah', 10000)
print(a1.withdraw(5010))
print()
    
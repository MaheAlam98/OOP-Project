class Shoping:
    def __init__(self,name):
        self.name = name
        self.cart=[]
    def addCart(self,item,price,quantity):
        product={'item':item, 'price':price, 'quantity':quantity}
        self.cart.append(product)
    
    def deleteitem(self,itemname):
        for items in self.cart:
            if items['item']==itemname:
                self.cart.remove(items)
            
    def CheckOut(self,amount):
        total=0
        for items in self.cart:
            total += int(items['price']) * int(items['quantity'])
        
        if total > amount:
            print(f"Your total Cost->{total}\nYou provide ->{amount}Tk")
            print(f"Please Provide->{total-amount} Tk More\n")

        elif total < amount:
            print(f"Your total Cost->{total}Tk\nYou provide->{amount}Tk")
            print(f"Here is your product and extra money {amount-total} Tk \nThanks for Shoping Our shop..")

        else:
            print(f"Your total Cost-{total}Tk\nYou provide -{amount}Tk")
            print("Here is your Product\n Thanks for Shoping Our shop..")

    



# t=Shoping("tuhin" )
# t.addCart("alu","40",5)
# t.addCart("oil","200",3)
# t.addCart("suger","160",5)
# t.addCart("milk","80",3)
# t.addCart("kokonat","90",3)
# print(t.cart)
# print("\n\n\n")
# t.deleteitem("kokonat")
# print(t.cart)
# print("\n\n\n")
# t.CheckOut(500)
name=input("Enter Your Name:")
print(f"Welcome to our shop {name}")
selcct_item=0
while True:    
    print(f"select choice\n1.Add Product in Cart\n2.Remove Product from Cart\n3.Show Select item\n4.Check Out")
    choice=int(input("Enter your choice:"))
    
    if choice==1 :
        item=input("Enter item name :")
        price=input("Enter item price :")
        quentity=input("Enter item quentity :")
        name=Shoping(name)
        name.addCart(item,price,quentity)
        print("Add item successfully")
        selcct_item += 1
            
        
    elif choice==2:
        itemname=input("Enter Item Name:")
        name.deleteitem(itemname)
        print("delete item successfully")
        selcct_item -=1
    elif choice==3:
         if selcct_item > 0:
            print(f"Total select item:{selcct_item}\nhere the item:{name.cart}")
         else:
            print("You don't select any product .\n please select product If you want to buy")
             
    elif choice==4:
        if selcct_item > 0:
            amount=int(input("please provide money:"))
            name.CheckOut(amount)
            break
        else:
            print("You don't select any product .\n please select product If you want to buy")
    

   


    
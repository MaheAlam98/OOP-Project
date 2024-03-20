"""1.Create a Product class and a Shop class.
2.Inside the Shop class, create a method name add_product which adds 
products using the Product class to the Shop class.
3.Inside the Shop class, create a method name buy_product which is used 
to buy a product and check whether this product is available or not. 
If you successfully buy a product, then throw a Congress message.
4.What is Inheritance? Explain with examples
5.What are Encapsulation and Access Modifiers? Explain with examples
"""
class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price



class Shop:
    def __init__(self):
        self.productlist=[]

    def add_product(self,product):
        self.productlist.append(product)
       

p1=Product("chair",500)
p2=Product("table",1000)
p3=Product("laptob",100000)

s1=Shop()
s1.add_product(p1)
s1.add_product(p2)
s1.add_product(p3)
i=1
for p in s1.list.productlist:
    
    print(f"Product item {i}-{(p)}:")
    i+=1



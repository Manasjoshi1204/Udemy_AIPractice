class Chai:
    pass

print(type(Chai)) #Class is also an object
ginger_tea = Chai()
print(type(ginger_tea))
print(type(ginger_tea) is Chai)

class Chai:
    origin = "India"
    
print(Chai.origin)
Chai.is_hot = True
print(Chai.is_hot)

masala = Chai()
print(masala.origin)
print(masala.is_hot)

masala.is_hot = False
print(masala.is_hot)
print(Chai.is_hot) #Changing object doesn't change the main class

masala.flavor = "Masala" #This doesn't exist in class
del masala.is_hot
print(masala.is_hot) #Attribute shadowing


class Chaicup:
    size = 150
    def describe(self):
        return f"A {self.size}ml chai cup"
cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup)) 

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))

 
                ### __init__  objects (Constructor)
                
class ChaiOrder:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size
        
    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala",150)
print(order.summary())


                     ###Inheritance
                     
class BaseChai:
    def __init__(self,type_):
        self.type = type_
    def prepare(self):
        print(f"Preparing {self.type} chai....")
        
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding ....")
        
                  #COMPOSITION
        
class ChaiShop:     
    chai_cls = BaseChai
    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in shop")
        self.chai.prepare()
        
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai 
    
shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve()
fancy.serve()
fancy.chai.add_spices()


class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.sttrength = strength
        
class BaseChai(Chai):
    def __init__(self,type_,strength,spice_level):
        Chai.__init__(self,type_,strength) #Explicit call
        self.spice_level = spice_level
         
class Base_Chai(Chai):
    def __init__(self,type_,strength,spice_level):
        super().__init__(type_,strength) #Super() call
        self.spice_level = spice_level
         
         

                      #Method Resolution Order (MRO)

class A:
    label = "A"
    
class B(A):
    label = "B"
    
class C(A):
    label = "C"
    
class D(B,C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)


                       ###Static Methods    
    
class ChaiUtils:
    @staticmethod   #Decorator
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
raw = " water , milk , ginger ,  honey"
obj = ChaiUtils
obj.clean_ingredients(raw)
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)


     ###Class Method (Controling the constructor) (Overwriting the constructor)

#@classmethod is useful when:
#Data comes in combined / messy / external format
#You need to convert it before creating object

class ChaiOrder:
    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
        
    @classmethod
    def from_dict(cls,order_data):
        return cls(   #calls constructor like ChaiOrder(...)
            order_data.get("tea_type"),
            order_data.get("sweetness"),
            order_data.get("size")
        ) 
        
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size = order_string.split("-")
        return cls(tea_type,sweetness,size)
    
class ChaiUtils:
    
    @staticmethod
    def is_valid_size(size):
        return size in ["Small","Medium","Large"]
    
print(ChaiUtils.is_valid_size("Medium"))        
    
order_first = {"tea_type":"Masala","sweetness":"Medium","size":"Large"}    
order1 = ChaiOrder.from_dict(order_first)
print(order1.__dict__)
print(order1.tea_type)

order_second = "Lemon-Less-Small"
order2 = ChaiOrder.from_string(order_second)

print(order2.__dict__)
print(order2.size)


        
                      ###Property Decorator
#We use getters and setters in Python to:
# control how attributes are accessed and modified

class TeaLeaf:
    def __init__(self,age):
        self._age = age            ## used as _attribute for representing
         
    @property                       ##Getter
    def age(self):
        return self._age + 2

    @age.setter
    def age(self,age):
        if 1<= age <=5:
            self._age = age
        
        else:
            raise ValueError("Tea leaf age must be 1-5 years")
    
leaf = TeaLeaf(2)
print(leaf.age) #No need of age()
leaf.age =6
print(leaf.age)
#Pydantic is used for data validation and settings management(for loading config or .env files) using Python type annotations(are hints that tell what type of data a variable, parameter, or return value should have).
 
                            ##Basic Syntax
 
# from pydantic import BaseModel

# class User(BaseModel):
#     id: int
#     name: str
#     is_active: bool = True
    
# input_data = {'id':101,'name':'Manas','is_active': False}
# user = User(**input_data)
# user2 = User(id=12,name="Joshi")
# print(user,'\n',user2) 

                         ##Mixing with typing

# from Pydantic import BaseModel
# from typing import List,Dict,Optional

# class Cart(BaseModel):
#     user_id : int
#     items : List[str]
#     quantities: Dict[str,int]
    
# class BlogPost(BaseModel):
#     title:str
#     content:str
#     image_url: Optional[str] = None
    
# cart_data = {
#     "user_id" : 123,
#     "items": ["laptop","mouse","keyboard"],
#     "quatities":20 
# }

# cart = Cart(**cart_data)

                      ##Field
    
# from typing import Optional
# from pydantic import BaseModel,Field
# import re

# class Employee(BaseModel):
#     id:int
#     name: str = Field(
#         ..., ###Required Field
#         min_length=3,
#         max_length=50,
#         description="Employee_name",
#         examples="Manas Joshi"
#     )
#     department: Optional[str] = 'General' #Can be str or none
#     salary : float = Field(
#         ...,
#         ge=10000,
#         le=100000,
#     )
    
#     class User(BaseModel):
#         email : str = Field(
#             ...,
#             regex = r''
#         )
#         discount : float = Field(
#             ...,
#             ge=0,
#             lt = 100,
#             description='Discount percentage'
#         )
    
# from pydantic import BaseModel,field_validator,model_validator

# class User(BaseModel):
#     username : str 
    
#     @field_validator('username')
#     def username_length(cls,v):
#         if len(v)<4:
#             raise ValueError("Name should be atleast 4 char") 
#         return v
    
# class SignupData(BaseModel):
#     pwd : str
#     cnfrm_pwd : str   
    
#     @model_validator(mode='after')
#     def pwd_match(cls,values): #cls -> before object is created
#         if values.pwd != values.cnfrm_pwd:
#             raise ValueError("Password do not match")
#         return values 

    
                      ###Computed Property
                      
# from pydantic import BaseModel,computed_field,Field

# class Product(BaseModel):
#     price : float
#     quant : int
    
#     @computed_field
#     @property
#     def total_price(self) -> float:  #self -> after object is created
#         return self.price * self.quant #The original data dosent change whereas in fieldvalidator the original value changes 
    

# class Booking(BaseModel):
#     user_id : int
#     room_id : int
#     nights : int = Field(
#         ...,
#         ge=1,
#     )
#     rate_per_night : float
    
#     @computed_field
#     @property
#     def total_amount(self) -> float:
#         return self.nights * self.rate_per_night
    
# booking = Booking(
#     user_id=123,
#     room_id=456,
#     nights=3,
#     rate_per_night=100
# )
# print(booking.total_amount)
# print(booking.model_dump())    
    
    
                        ###Advance_validators
                        
# from pydantic import BaseModel,field_validator,model_validator
# from datetime import datetime

# class Person(BaseModel):
#     first_name : str
#     last_name : str
    
#     @field_validator('first_name','last_name')
#     def names_must_be_capitalized(cls,v):
#         if not v.istitle():
#             raise ValueError("Names must be capitalized")
#         return v                   
    
# class User(BaseModel):
#     email : str
#     @field_validator("email")
#     def normalize_email(cls,v):
#             return v.lower().strip()
        
# class Product(BaseModel):
#     price : str # $4.44
#     @field_validator('price',mode='before')
#     def parse_price(cls,v):
#         if isinstance(v,str):
#             return float(v.replace('$',''))
#         return v
    
# class DateRange(BaseModel):
#     start_date: datetime
#     end_date : datetime
    
#     @model_validator
#     def validate_date(cls,values):
#         if values.end_date >= values.start_date:
#             raise ValueError("End date ,ust be after")
#         return values
    

                   ###Nested Models
                   
# from pydantic import BaseModel
# from typing import List,Optional

# class Address(BaseModel):
#     street : str
#     city : str
#     postal_code : str
    
# class User(BaseModel):
#     id: int
#     name : str
#     adress : Address   
# adress = Address(
#     street = "123 something",
#     city="Haldwani",
#     postal_code="123_abc"
# )
# user = User(
#     id =1,
#     name="Manas",
#     adress= adress
# )
# print(user.model_dump)

##Self referencing model (recursive)

# from typing import List,Optional,Union
# from pydantic import BaseModel

# class Comment(BaseModel):
#     id:int
#     content:str
#     replies: Optional[List['Comment']] = None
    
# Comment.model_rebuild() #Forward refrences used for self referencing
# comment = Comment(
#     id = 2,
#     content="First Comment",
#     replies=[
#         Comment(id=1,content="replies=1"),
#         Comment(id=3,content="replies=2"),
#         Comment(id=4,content="replies=3",replies= [Comment(id=5,content="NESTED REPLY")]),
#     ] 
# )

#Advance nested models

#Optional data type
# class Address(BaseModel):
#     street : str
#     city : str
#     postal_code : str

# class Company(BaseModel):
#     name:str
#     address: Optional[Address] = None
    
# class Employee(BaseModel):
#     name: str
#     company : Optional[Company] = None
    
# #Mixed data type     
# class TextContent(BaseModel):
#     type : str = 'text' #Instead of text : str
#     content : str
       
# class ImageContent(BaseModel):
#     type : str = 'image'
#     url : str
#     alt_text : str
    
# class Article(BaseModel):
#     title: str
#     sections: List[Union[TextContent,ImageContent]]
    
#Deeply nested structure

# class Country(BaseModel):
#     name:str
#     code:str
    
# class State(BaseModel):
#     name:str
#     country : Country
    
# class city(BaseModel):
#     name:str
#     state: State
    
# class Address(BaseModel):
#     street : str
#     city : city
#     postal_code : str

# class Organization(BaseModel):
#     name : str
#     head_quater : Address
#     branches : List[Address] = []
    
#Always do the opp of what we did....define leaf models first and build upward


                        ###Pydantic Serialization

#Converting complex pydantic structures to easily understable,stored,processed,transmitted models
#like Dicts,Json,XML

from pydantic import BaseModel,ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city: str
    postal_code:str
    
class User(BaseModel):
    id : int
    name : str
    address: Address
    email : str
    is_active : bool = True
    created_at : datetime
    tags : List[str] = []
    model_config = ConfigDict(
        json_encoders={datetime:lambda v: v.strftime('%d-%m-%Y %H:%M:%S')} #Dict key-value pair
    )   
    
    #hi this is a test
    #Hello we have changed
    print("hello")
    print("Hello World")
    
    #New message here
    
    

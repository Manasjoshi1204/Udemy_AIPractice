import pytest

def test_equal():
    assert 3 == 3
    assert 7>4
    
def test_instance():
    assert isinstance('this is a string',str)
    assert not isinstance('10',int)
    
def test_boolean():
    valid = True
    assert valid is True
    assert ('hello' == 'world') is False    
    
def test_type():
    assert type('Hello' is str)
    assert type('World' is not str)
    
def test_list():
    num_list = [1,2,3,4]
    any_list = [False,False]
    
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)
    
 
class Student:
    def __init__(self,first_name:str,last_name:str,major:str,years:int):
           self.first_name = first_name
           self.last_name = last_name
           self.major = major
           self.years = years
           
@pytest.fixture
def default_employee():
     return Student('John','Doe','Computer Science',3)          
           
def test_person_initialization(default_employee):
    #p = Student('John','Doe','Computer Science',3)
    assert default_employee.first_name == 'John','First name should be john'
    assert default_employee.last_name == 'Doe','First name should be doe'
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3
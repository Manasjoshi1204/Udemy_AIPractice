from fastapi import FastAPI,HTTPException,Path,Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional

app = FastAPI()

#Loading and dumping data
def load_data():
    with open('patients.json','r') as f:
        data = json.load(f) #reads json data from f object and converts it into Python object
    return data

def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data,f)

#Pydatic Validation for PUT OR POST
class Patient(BaseModel):
    id : Annotated[str,Field(...,description='Id of patient',examples=['P001'])]
    name : Annotated[str,Field(...,description="Name of the patient",)]
    city : Annotated[str,Field(...,description="City of patient")]
    age : Annotated[int,Field(...,gt=0,lt=120,description="Age of patient")]
    gender : Annotated[str,Literal['male','female','others'],Field(...,description="Gender of patient")]
    height : Annotated[float,Field(...,gt=0,description='Height in m')]
    weight : Annotated[float,Field(...,gt=0,description="Weight in kgs")]
    
    @computed_field
    @property
    def bmi(self) -> float: #function name becomes key name in output
        return round(self.weight/self.height**2,2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Overweight'
        
class Update_Patient(BaseModel):
    
    name : str|None =Field(default=None,description="Name of the patient",)
    city : Optional[str] =Field(default=None,description="City of patient")
    age : Optional[int] = Field(default=None,gt=0,lt=120,description="Age of patient")
    gender : Optional[Literal['male','female','others']]=Field(default=None,description="Gender of patient")
    height : Optional[float] = Field(default=None,gt=0,description='Height in m')
    weight : float | None = Field(default=None,gt=0,description="Weight in kgs")


                  ###Retrieval

@app.get("/")
def hello():
    return {'message':'Patient Management System'}

@app.get("/about")
def about():
    return {'message':'A fully functioning API to manage your patients'}

@app.get('/view')
def view():
    data = load_data()
    return data

             ##Path Parameter (patient_id)
             
#Path parameter is a variable part of the URL that can be used to identify a specific resource. 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description='ID of the patient in the DB',example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")

#Https status codes are standardized codes that indicate the outcome of an HTTP request.       

                ##Query Parameter 
                
#Query parameters are additional parameters that can be added to the URL to provide more information about the request. They are typically used for filtering, sorting, or searching data.

@app.get('/sort')
def sort_patients(sort_by : str = Query(...,description='Sort on the basis of height/weight/bmi'),order : str = Query('asc',description='Sort in asc or desc')):
    
    valid_fields = ['height','weight','bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Select from valid fields {valid_fields}")
        
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f"Select from valid order: asc or desc")
    
    data = load_data()
    sort_order = False if order == 'asc' else True
    
    sorted_data = sorted(data.values(),key= lambda x : x.get(sort_by,0),reverse= sort_order)
    
    return sorted_data

                     ###CREATE 
     
#Request body is the data sent by the client to the server in an HTTP request. It typically contains information that the server needs to process the request, such as form data, JSON payloads, or file uploads.

@app.post('/create')
def create_patient(patient:Patient):
    old_data = load_data()
    #Check if patient already exists
    if patient.id in old_data:
        raise HTTPException(status_code=400,detail="Patient already exists") 
    #Create new key by unpacking json response into dictionary
    old_data[patient.id] = patient.model_dump(exclude= {'id'})
    
    save_data(old_data)
    return JSONResponse(status_code=201,content={'message':'patient created successfully'})

                    ###Update
                    
@app.put("/edit/{patient_id}",summary="Update patient details")
def update_patient(patient_id:str,patient_update: Update_Patient):
    
    data = load_data()
    #Check if patient in db or not
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    
    existing_data = data[patient_id]
    
    #Convert only non-none fields into dictionary
    updated_patient_info = patient_update.model_dump(exclude_unset=True) 
    
    #Changing the values
    for key,value in updated_patient_info.items():
        existing_data[key] = value
        
    #Convert existing_data into pydantic object for computed fields
    existing_data['id'] = patient_id #Because there is id field in our pydantic model
    patient_pydantic_obj = Patient(**existing_data) 
    
    data[patient_id] = patient_pydantic_obj.model_dump(exclude={'id'})
    save_data(data)
    
    return JSONResponse(status_code=200,content={'message':'Patient updated'})

@app.delete('/delete/{patient_id}')
def delete(patient_id:str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200,content="Patient deleted")
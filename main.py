from fastapi import FastAPI

app = FastAPI()

# CREATE MY FIRST GET ENDPOINT
@app.get("/")
def home():
    return "Hii This is my FAST API  practic file!"
    

@app.post("/create")
def taskcreate(data:dict):
    return {
        "data": data ,
        "msg": "post created successfully"
    }

@app.put("/update/{id}")
def taskupdate(id:str , data:dict):
    return{
        "data":data,
        "msg":"task updated successfully!"
    }

@app.delete("/delete/{id}")
def taskupdate(id:str ):
    return{
        
        "msg":"task deleted successfully!"
    }
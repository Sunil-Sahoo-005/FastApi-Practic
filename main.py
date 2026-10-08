from fastapi import FastAPI

app = FastAPI()

# CREATE MY FIRST GET ENDPOINT
@app.get("/")
def home():
    return "Hii This is my FAST API  practic file!"
    
from fastapi import FastAPI, HTTPException
from utils import write_to_file, encrypt, decrypt
import uvicorn

app = FastAPI()

@app.get("/test")
def get_test():
    return {"message": "hi from test"}

@app.get("/test/{name}")
def get_by_name(name):
    write_to_file(name)
    print("The name entered into the data.")
    return {"message": "saved user"}

@app.post("/caesar")
def craete_cipher(body:dict):
    if body["mode"] == "encrypt":
        return {"encrypted_text":encrypt(body["text"], body["s"])}
        
    if body["mode"] == "decrypt":
        return {"decrypted_text":decrypt(body["text"],body["s"])}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
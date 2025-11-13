from fastapi import FastAPI, HTTPException
from utils import write_to_file, encrypt_caesar, decrypt_caesar
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
def cipher_by_caesar(body:dict):
    if body["mode"] == "encrypt":
        print("encrypt")
        return {"encrypted_text":encrypt_caesar(body["text"], body["s"])}
        
    if body["mode"] == "decrypt":
        print("decrypted")
        return {"decrypted_text":decrypt_caesar(body["text"],body["s"])}

# GET /fence/encrypt?{text=str}"
@app.get("/fence/encrypt")
def get_text(text:str):
    return {"text":text}

# POST /fence/decrypt"
@app.post("/fence/decrypt")
def cipher_by_fence(body:dict):
    return body
    

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
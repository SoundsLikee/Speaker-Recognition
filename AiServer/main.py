import os
import uuid
from fastapi import FastAPI, UploadFile

UPLOAD_USER_DIR = "../SpeakerRecognition/data/user_data"
UPLOAD_ADMIN_DIR = "../SpeakerRecognition/data/admin_data"

app = FastAPI()

@app.post("/upload/user")
async def create_upload_file(file: UploadFile):
    content = await file.read();
    
    filename_split = file.filename.split('.')
    file_ext = "." + filename_split[-1]
    upload_filename = "input" + file_ext

    with open(os.path.join(UPLOAD_USER_DIR, upload_filename), "wb") as fp:
        fp.write(content)

    result = runSpeechRecognition()
    os.remove(UPLOAD_USER_DIR + '/' + upload_filename)
    
    return result;

def runSpeechRecognition():
    os.system('./run_ai.sh')

    with open('../SpeakerRecognition/result.txt', 'r') as text_file:
        results = text_file.readlines()
    results = [result.rstrip('\n') for result in results]
    results[2] = results[2][7:13]
    
    return {"isAdmin": results[0], "accuracy": results[2]}

@app.post("/upload/admin")
async def create_admin_file(file: UploadFile):
    content = await file.read();
    
    filename_split = file.filename.split('.')
    file_ext = "." + filename_split[-1]
    upload_filename = f"{str(uuid.uuid4())}" + file_ext

    with open(os.path.join(UPLOAD_ADMIN_DIR, upload_filename), "wb") as fp:
        fp.write(content)

    return {"status": "200 OK"}
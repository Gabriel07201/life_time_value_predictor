from pipeline import Pipeline
from fastapi import FastAPI, UploadFile, File, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
import os
import uvicorn
import json

app = FastAPI()

@app.get("/")
def home():
    file_name = "teste.json"
    file_path = os.getcwd() + "/" + file_name
    return FileResponse(path=file_path, media_type='application/json', filename=file_name)


@app.post("/predict/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    string = json.loads(contents.decode('utf-8'))
    dados = json.dumps(string)
    pipe = Pipeline(dados)
    df_final = pipe.execute_pipe()
    # print(df_final)

    return Response(df_final)


@app.post('/df_final/')
async def df_final(file: UploadFile = File(...)):
    contents = await file.read()
    string = json.loads(contents.decode('utf-8'))
    dados = json.dumps(string)
    pipe = Pipeline(dados)
    df_final = pipe.execute_pipe()
    with open('df_final.json', 'w') as f:
        json.dump(df_final, f)
    file_name = "df_final.json"
    file_path = os.getcwd() + "/" + file_name

    return FileResponse(path=file_path, media_type='application/json', filename=file_name)

if __name__ == '__main__':
    uvicorn.run('main:app', port=5000, log_level='info')
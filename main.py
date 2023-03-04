from pipeline import Pipeline
from fastapi import FastAPI, UploadFile, File, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse
import os
import uvicorn
import json

app = FastAPI()

@app.post("/predict/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    aleatoria = json.loads(contents.decode('utf-8'))
    dados = json.dumps(aleatoria)
    pipe = Pipeline(dados)
    df_final = pipe.execute_pipe()
    print(df_final)

    return Response(df_final)


if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
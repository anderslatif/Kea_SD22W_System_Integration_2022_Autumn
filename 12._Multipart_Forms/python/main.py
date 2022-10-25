from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/basicform")
async def basicform(username: str = Form(...), password: str = Form(default=..., min_length=8)):
    print(password)
    return username

@app.post("/fileupload")
async def fileupload(file: UploadFile):
    print(file)
    return file.filename
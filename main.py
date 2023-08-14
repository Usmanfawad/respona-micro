from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every

import httpx

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



URL_API_PYTHONANYWHERE = "http://mysteryshops.pythonanywhere.com/home"
URL_API_LOCAL = "http://127.0.0.1:5000/home"


# @repeat_every(seconds=10)
# Running after every 2 hours.
@app.on_event("startup")
@repeat_every(seconds=30)
async def root():
    print("Root route initiated!")
    WORKER_THREAD = True
    try:
        async with httpx.AsyncClient() as client:
            print("Here hitting the API")
            resp = await client.get(URL_API_PYTHONANYWHERE, timeout=None)
            # resp = await client.get(URL_API_LOCAL, timeout=None)
            print(resp)
    except Exception as e:
        print(e)
    return {"200": "success"}
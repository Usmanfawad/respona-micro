from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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



from fastapi_utils.tasks import repeat_every

# Root route that runs every 30 seconds.
@app.on_event("startup")
@repeat_every(seconds=30)
# Running after every 2 hours.
# @repeat_every(seconds=60*120)
@app.get("/")
async def root():
    return {"200": "success"}
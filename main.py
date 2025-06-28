from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/service-timing")
def get_service_timing(region: str = "USA"):
    if region == "Europe":
        return {"timing": "5-10 minutes between drink orders"}
    elif region == "Caribbean":
        return {"timing": "Relaxed pace, 10-15 minutes"}
    elif region == "Asia":
        return {"timing": "Highly attentive, 3-6 minutes"}
    return {"timing": "3-6 minutes standard pace"}

from fastapi import FastAPI
from app.api.scan import router as scan_router
from fastapi.middleware.cors import CORSMiddleware

cors_origins = [
    "http://localhost:3000",
]
     

app = FastAPI(
    title="Mini CSPM Scanner",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
   

app.include_router(scan_router, prefix="/api/v1")

@app.get("/")
def health_check():
    return {"status": "ok"}

from pydantic import BaseModel

class ScanRequest(BaseModel):
    access_key: str
    secret_key: str
    region: str

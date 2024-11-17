from fastapi import FastAPI, Depends, HTTPException, Request
from dify_tools.router import router

app = FastAPI(
    title="Dify Tool API",
    description="これはDifyのサンプルToolのAPIです。",
    version="0.1.0",
    servers=[
        {
            "url": "http://192.168.11.123:8000",  # 自分のローカルIPを指定
            "description": "Local server",
        }
    ],
)

# デモのキーです。
API_KEY = "demo_key"


def verify_api_key(request: Request):
    api_key = request.headers.get("Authorization")
    if not api_key:
        raise HTTPException(status_code=401, detail="API Key is missing")
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")


app.include_router(router, prefix="/api", dependencies=[Depends(verify_api_key)])

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import datetime



app = FastAPI(
    title="Sample Azure App Service API",
    version="1.0.0",
    description="FastAPI sample running on Azure App Service with Docker",
)


@app.get("/", response_class=JSONResponse)
async def root():

    # 現在の日時を取得
    now = datetime.datetime.now()

    # 文字列に変換 (24時間表記)
    formatted_now = now.strftime("%Y/%m/%d %H:%M:%S")
    s = f'Hello from Azure App Service FastAPI! {formatted_now}'

    return {
        "service": "root",
        "message": s,
        "status": "ok",
    }

@app.get("/image", response_class=JSONResponse)
async def root():
    return {
        "service": "root",
        "message": "Hello from Azure App Service FastAPI!",
        "status": "ok",
    }




@app.get("/help", response_class=JSONResponse)
async def help():
    return {
        "service": "help",
        "usage": {
            "GET /": "Returns basic service status.",
            "GET /help": "Returns help information for this API.",
        },
        "status": "ok",
    }

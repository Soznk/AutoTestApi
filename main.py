from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/santiago-time")
def get_santiago_time():
    # 获取当前的UTC时间
    utc_now = datetime.utcnow()

    # 定义圣地亚哥的时区
    santiago_tz = pytz.timezone("America/Los_Angeles")

    # 将UTC时间转换为圣地亚哥时间
    santiago_time = utc_now.astimezone(santiago_tz)

    # 返回圣地亚哥时间
    return {"santiago_time": santiago_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")}


@app.get("/")
def read_root():
    return {"message": "Welcome to the AutoTestApi!"}

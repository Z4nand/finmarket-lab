from fastapi import FastAPI

app = FastAPI()


@app.get("/api/status")
def get_status():
    return {"status": "stopped"}


@app.post("/api/collector/start")
def start_collector():
    return {"status": "running"}


@app.post("/api/collector/stop")
def stop_collector():
    return {"status": "stopped"}
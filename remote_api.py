from fastapi import FastAPI
import remote_tools
app = FastAPI()
tool = remote_tools.Tool()

@app.get("/")
async def root():
    return {"memory":tool.get_mem(),
            "disk":tool.get_disk(),
            "CPU":tool.get_cpu()}



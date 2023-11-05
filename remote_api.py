from fastapi import FastAPI
import remote_tools
import tools_config
#configurations for api 
app = FastAPI()
tool = remote_tools.Tool()
path = tools_config.Path().server_path
#modifies get call to return server information
@app.get(path)
async def root():
    return {"memory":tool.get_mem(),
            "disk":tool.get_disk(),
            "CPU":tool.get_cpu()}



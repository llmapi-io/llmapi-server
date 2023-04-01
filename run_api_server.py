import uvicorn
from server.config import config_init

config_init()

if __name__ == "__main__":
    config = uvicorn.Config("server.api_server:app", port=5050, log_level="info")
    server = uvicorn.Server(config) 
    server.run()

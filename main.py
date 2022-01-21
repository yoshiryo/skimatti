import uvicorn
import routers.server as server 
if __name__ == "__main__":
   uvicorn.run(server.fastapi, host = "0.0.0.0", port = 80)
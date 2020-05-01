import uvicorn

from server import init_app
from server.configurations.environment import env

if __name__ == "__main__":
    app = init_app()
    uvicorn.run(app, host=env.api_host(), port=env.api_port())

import uvicorn

from server import init_app
from server.configurations.environment import env

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host=env.api_host(), port=env.api_port())


from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def top():
    return 'Top here'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

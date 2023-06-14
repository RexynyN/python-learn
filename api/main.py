# https://github.com/bitfumes/fastapi-course
# https://www.youtube.com/watch?v=7t2alSnE2-I&list=PLe30vg_FG4OSKH_8zpLlnf4WpNlzL526E
from fastapi import FastAPI

# https://www.youtube.com/watch?v=GN6ICac3OXY
app = FastAPI()

@app.get("/")
def root():
    return { "Hello" : "Warudo!"}


# uvicorn main:app
# https://github.com/bitfumes/fastapi-course
# https://www.youtube.com/watch?v=7t2alSnE2-I&list=PLe30vg_FG4OSKH_8zpLlnf4WpNlzL526E
from fastapi import FastAPI, status, HTTPException

# https://www.youtube.com/watch?v=GN6ICac3OXY
app = FastAPI()

@app.get("/")
def root():
    return { "Hello" : "Warudo!"}

@app.get("/notfound")
def client():
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")


# uvicorn main:app
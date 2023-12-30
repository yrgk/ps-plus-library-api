from fastapi import FastAPI


app = FastAPI()

# Routing
@app.get('/')
def main_page():
    return {"message": "Main page"}
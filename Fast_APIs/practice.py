from fastapi import FastAPI
import uvicorn
app=FastAPI(
    title='My First Api',
    description='I am gald its My First Api',
    version='1.0.0'
)
@app.get('/')
def something_return():
    return f"Welcome into new era"
@app.get('/hello/{name}')
def somee(name : str):
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("practice:app", port=5000,host='127.0.0.1',log_level="info",reload=True)


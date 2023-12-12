from fastapi import FastAPI, HTTPException, Request, Depends, Path
from fastapi.responses import JSONResponse
from fastapi.logger import logger
import pickle
import uvicorn 
from typing import List , Union
import json  # Import the json module

app = FastAPI()

@app.get("/prediction",response_model=List[dict])
async def prediction(data):
    try:
    
       print(data)
       print(type(data))
       data_dict = eval(data)
       print(data_dict)
       print(type(data_dict))
       data_list = [list(data_dict.values())]
       print(data_list)
       response = get_department(data_list)
       print(response)
       if response["status"] == "success":
           return response["data"]
    except Exception as e:
        logger.error(e)
        raise HTTPException(status_code=500, detail=str(e))

# internal function
def get_department(data):
    try:
        f = open('random_forest_model.pickle', 'rb')
        classifier = pickle.load(f)
        f.close()
        # print("hello")
        prediction = classifier.predict(data)
        return {"status": "success", "data": prediction}
    except Exception as e:
        logger.error(e)
        return {"status": "failed", "data": None, "message" :str(e)}
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
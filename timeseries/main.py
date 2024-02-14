from pymongo import MongoClient
from fastapi import FastAPI, HTTPException
from datetime import datetime
from model_classes import *
from typing import List

# Connecting to mongo client
client = MongoClient(
    host="localhost", port=27017, username="mongoadmin", password="turbit!"
)

db = client["turbine_data"]

# Expose with FastAPI
app = FastAPI()


@app.on_event("shutdown")
def shutdown_event():
    client.close()


# Endpoint
@app.get("/{turb_id}", response_model=List[Turbs])
async def get_data(turb_id: int, startt: str, endt: str):
    startdate = datetime.strptime(startt, "%Y-%m-%dT%H:%M")
    enddate = datetime.strptime(endt, "%Y-%m-%dT%H:%M")
    myquery = db.Collection.find(  # for multiple criteria on one key
        {"$and": [{"turb_id": turb_id}, {"date": {"$gte": startdate, "$lte": enddate}}]}
    )
    if myquery is not None:
        return myquery
    raise HTTPException(
        status_code=404, detail=f"Turbine {id} or chosen time range not found"
    )

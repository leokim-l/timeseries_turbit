from pymongo import MongoClient
import pandas as pd
import os
import json
from datetime import datetime

# ==========================================================================
# Setup
local_path = os.path.dirname(os.path.realpath(__file__))
local_db = "/".join(local_path.split("/")[0:-2]) + "/raw_timeseries/"


# ==========================================================================
# Connect to mongodb instance running in docker
client = MongoClient(
    host="localhost", port=27017, username="mongoadmin", password="turbit!"
)

db = client["turbine_data"]

# ==========================================================================
# Import data
for i in range(1, 3):  # loop over two turbines
    fp = local_db + "Turbine" + str(i)

    # Here I insisted on using pandas because I know it. Down the pipeline
    # this may have turned on me, but I managed to solve issues coming up
    df = pd.read_csv(fp + ".csv", sep=";", header=[0, 1], skipinitialspace=True)
    rename_clmn = []

    # Merge the first two rows into one, with extra-work due to pandas
    for j, k in df.columns:
        if f"{k}".startswith("Unnamed"):
            rename_clmn.append(f"{j}")
        else:
            rename_clmn.append(f"{j}_{k}")
    df.columns = rename_clmn

    # Make datetime type and use isoformat
    df["Dat/Zeit"] = pd.to_datetime(df["Dat/Zeit"], format="%d.%m.%Y, %H:%M")

    # Add turbine id, reconvert to datetime and insert into DB
    records = json.loads(df.T.to_json(date_format="iso")).values()
    for rec in records:
        rec["Dat/Zeit"] = datetime.strptime(rec["Dat/Zeit"], "%Y-%m-%dT%H:%M:%S.%f")
        rec["turb_id"] = i
    db.Collection.insert_many(records)

client.close()

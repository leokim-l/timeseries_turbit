import os

local_path = os.path.dirname(os.path.realpath(__file__))
local_db = "/".join(local_path.split("/")[0:-2]) + "/raw_timeseries"
print(local_db)

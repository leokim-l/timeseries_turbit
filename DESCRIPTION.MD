# A short description of the project

The structure is very simple, with a docker-compose file (`docker-compose.yml`) in the main folder to run a MongoDB instance in docker. The directory /timeseries contains three relevant scripts:

1. timeseries/import_data.py, to be run once, which connects to the MongoDB client, takes .csv data from a local folder and populates the database. Some probably-unnecessary extra-work was carried out due to my initial idea and later my insistence on using pandas, simply because of prior experience with it. The data is then then run through the outermost for loop, with one cycle per turbine. Since there are two rows of header, they are merged into one for later convenience. Pandas will automatically generate tags starting with "Unnamed" for empty fields, which are eliminated. The "Dat/Zeit" column is then transformed into a datetime.datetime object, put into iso format, and subsequently the pandas DataFrame transformed to json. Finally, a for loop goes through the JSON records and does two things: it overwrites the - by now - strings with date and time with proper datetime objects and it adds a field for the turbine id, 1 or 2. Now the data is ready to be inserted into one single MongoDB Collection.

2. timeseries/model_classes.py contains the pydantic response model.

3. timeseries/main.py finally creates a FastAPI instance, with a trivial shutdown application and one GET method as endpoint. This takes the turbine id `turb_id` as well as two further strings, encoding the start time and the end time which one desires to query. Since the (aliased) `data` field in the database contains datetime.datetime format, the input strings are transformed in datetime instances through the datetime.strptime method. The query then uses $gte and "$lte" as well as turbine id to produce the relevan output. Somewhat sadly, all of this works without error messages, yet I cannot seem to be able to run it on my browser obtaining the results nicely displayed.

# Still todo/improvements:

1. Get rid of explicit paths in docker-compose.yml, which should be trivial, but would not always work if simply substituting by ${PWD}.

2. Conclude the whole task and be able to visually see the output on browser.

3. Add test functions.
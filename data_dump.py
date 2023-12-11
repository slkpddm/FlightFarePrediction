import pymongo
import pandas as pd
import json
from FlightFarePredictor.config import mongo_client
# Provide the mongodb localhost url to connect python to mongodb.
#client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
#client=pymongo.MongoClient("mongodb+srv://slkpddm:Swathi8294@cluster0.nxrfndf.mongodb.net/?retryWrites=true&w=majority")
data_file_path=r"C:\Users\slkpd\Flight Fare prediction\Flight Fare Prediction.csv"
database_name="flight"
collection_name="fare1"

if __name__=="__main__":
   df=pd.read_csv(data_file_path)
   print(f"Rows and Columns:{df.shape}")
   print(mongo_client.test)
   # convert dataframe to json format so that we can dump these records into mongo db
   df.reset_index(drop=True,inplace=True)

   json_record=list(json.loads(df.T.to_json()).values())
   print(json_record[0])

   # insert converted json record to mongo db
   mongo_client[database_name][collection_name].insert_many(json_record)



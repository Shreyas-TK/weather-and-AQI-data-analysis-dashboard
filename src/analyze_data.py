import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os 

load_dotenv()
password = quote_plus(os.getenv("DB_PASS"))
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{password}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

weather_df = pd.read_sql("SELECT * FROM weather_data",engine)
aqi_df  = pd.read_sql("SELECT * FROM aqi_data",engine)

print(weather_df,"\n")
print(aqi_df)

#Export data to CSV 
weather_df.to_csv("/Users/shreyastk/Documents/smartcity-dashboard/data/clean/weather.csv", index=False)
aqi_df.to_csv("/Users/shreyastk/Documents/smartcity-dashboard/data/clean/aqi.csv", index=False)

print("Finished storing data as CSV file..!!")

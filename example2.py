import pandas as pd
import mysql.connector
import json
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin@123",
  database="new_db"
)
df =  pd.read_csv(r"C:\Users\V\Downloads\new testing 5k.csv")
number = []
for i,j in df.iterrows():
    list_row = []
    if df["phoneNumber"][i] not in number:
        #list_row = []
        number.append(df["phoneNumber"][i])
        extra_detail=dict()
        for key,value in list(j.items())[2:]:
            key=str("".join(key.split()))
            na_value=str(value)
            if na_value!="nan":
                extra_detail[key]=value
        
    list_row.append((1,str(df["phoneCode"][i]),str(df["phoneNumber"][i]),json.dumps(extra_detail)))
    print(list_row)
    # mycursor = connection.cursor()
    # sql = f"insert into customer_data (id,phone_code,phone_number,extra_data) VALUES (%s %s %s %S)"
    # mycursor.execute(sql,list_row)
    # connection.commit()


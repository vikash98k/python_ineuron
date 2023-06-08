leadsetdata_details=dict()
for i, row in  portfolio1.iterrows():
    
    extra_detail=dict()
    for key,value in list(row.items())[2:]:
        
        key=str("".join(key.split()))
        na_value=str(value)
        if na_value!="nan":
            extra_detail[key]=value
            
        
            mydb = mysql.connector.connect(
            host="demo1.collaberus.com",
            user="cron",
            password="D1alM@2020",
            database="asterisk"
            )
            
            mycursor = mydb.cursor()
            val = json.dumps(extra_detail)
            sql=f"update customer_data set extra_data='{val}' where list_id={leadsetfile.pk} and phone_number='{list(row.items())[1][1]}'"
            mycursor.execute(sql)
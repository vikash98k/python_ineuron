import MySQLdb
import csv

database = MySQLdb.connect(host="127.0.0.1",user="root",passwd="Mysumapa071@",db="mysql")

cursor = database.cursor()

csv_data = csv.reader(open('stationdata.csv'))

for i in csv_data:
    print(i)
    cursor.execute('insert into station_data(id,city,state,lat_n,long_w) values(%s,%s,%s,%s,%s)',i)

cursor.close()
database.commit()
database.close()



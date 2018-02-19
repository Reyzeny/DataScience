import csv

lst = ['TMAX','TAVG','TMIN','PRCP','SNWD','SNOW']

for key in lst:
    data_exists = False
    zero_count=0
    space_count=0
    with open ("Clarksville_weather_history.csv") as dataIn:
        dataIn = csv.DictReader(dataIn)
        print(key)
        csv_col = []
        date = []
        for row in dataIn:
            valu = row[key]
            if(valu.isnumeric() and valu!='0'):
                csv_col.append(int(row[key]))
                date.append(row["DATE"])
                data_exists = True
            elif(('.' in valu) and float(valu)!=0.0 and float(valu)!=0.00):
                csv_col.append(float(row[key]))
                date.append(row["DATE"])
                data_exists = True
            elif(valu=="" or valu==" "):
                space_count+=1
            elif(float(valu)==0.0 or float(valu)==0.00):
                zero_count+=1
            

        if (data_exists):
            max_val = max(csv_col)
            min_val = min(csv_col)
            index_for_max = csv_col.index(max_val)
            date_for_max = date[index_for_max]
            index_for_min = csv_col.index(min_val)
            date_for_min = date[index_for_min]
            print("Column is " + key)
            print("Max is " + str(max_val))
            print("Min is " + str(min_val))
            print("Date for max value is " + str(date_for_max))
            print("Date for min value is " + str(date_for_min))
            print("Number of zeros: " + str(zero_count))
            print("Number of spaces: " + str(space_count))

            print("")
            print("")
        else:
            print("Column is " + key)
            print("No max")
            print("No min")
            print("Number of zeros: " + str(zero_count))
            print("Number of spaces: " + str(space_count))

            print("")
            print("")

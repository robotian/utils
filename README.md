# Misc. Util scripts

## gps_to_map_frame
Create a csv file containing GPS coordinates in the 'data' directory. In the table in the csv file, 5 and 6th columns should have latitude and longitude data, respectively. The first row will be considered as a header, so it will skip the first row. 

job_table_big_1.csv
```
id,node_id,status,assigned_to,lat,long,x,y
1,,,,45.081685333,-84.774548812,,
2,,,,45.081685376,-84.774544238,,
3,,,,45.081685419,-84.774539665,,
4,,,,45.081685462,-84.774535091,,
5,,,,45.081685505,-84.774530518,,
```


```
cd scripts
python3 gps_to_map_frame.py job_table_big_1.csv 45.081679 -84.774588
```

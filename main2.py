from fastapi import FastAPI
import mysql.connector

fastapi_obj=FastAPI()
connection_object=mysql.connector.connect(
    host="localhost",
    user="root",
    database="gen_ai_demo",
    password="10000Coders"
) # py + mysql + connect +obj

cursor_obj=connection_object.cursor() # querue execute method


@fastapi_obj.get("/") # @f_obj.method("/route")
def get_min_response():
    cursor_obj.execute("select * from employees")
    data=cursor_obj.fetchall()
    return data


@fastapi_obj.post("/post_data")
def post_data(name:str,loc:str,sal:int):
    # rec data --> table insert 
    # --> table loki yela veltadi 


    query="insert into employees(id,name,location,salary) values (%s,%s,%s,%s)"
    values=(1,name,loc,sal)

    cursor_obj.execute(query,values)
    connection_object.commit()
    return {
        "id":1,"name":name,"location":loc,"salary":sal
    }


# apis build
# 4 hhtp methods / 4 http request methods


# fe :-- get 
# fe :-- post 
# fe :-- put
# fe :-- delete
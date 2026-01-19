from flask import Flask , request , render_template,abort,redirect,flash
#from SQLAlchemy import sqlalchemy
from Db2 import engine,Users
from sqlalchemy.orm import sessionmaker
from datetime import datetime as d

Session=sessionmaker(bind=engine)
s=Session()



app=Flask(__name__)

@app.route('/',methods=["POST","GET"])

def home():
  
    if request.method == "POST":
        content=request.form.get('contents')
        newTask=Users(tasks=content,date=d.now().date())
        s.add(newTask)
        s.commit()
    data=s.query(Users).all()   
    return render_template("index.html",tasks=data)
        
@app.route('/update/<int:id>',methods=["POST","GET"])
def updateTask(id):
    #if request.method == "GET":
        data=s.query(Users).filter(Users.id==id).one_or_none()
        if not data:
           abort(404) 
           
        if request.method == "POST":
           data.tasks=request.form.get("update_task")
           s.commit()
           return redirect("/")
        
        return render_template("update.html",contents=data.tasks)
        

@app.route('/delete/<int:id>',methods=["POST"]) 
def deleteTask(id):
   data=s.query(Users).filter(Users.id==id).one_or_none()
   
   if not data:
           abort(404) 
   #if request.method== "POST":
   #   return "delete=>Post"
   if request.method== "POST":
      #return "delete=>GET"
      s.delete(data)
      s.commit()
   return redirect("/")
          
    
if __name__ == "__main__" :
    app.run(debug=True)
   

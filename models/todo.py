from db import db, ma 

class Todo(db.Model):
    __tablename__ = 'todo'
    
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(100))
    date = db.Column(db.Date)
  
class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'job', 'date')
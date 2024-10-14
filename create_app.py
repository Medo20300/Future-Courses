from pythonic import db
from pythonic import create_app  

app = create_app()  
with app.app_context():  
    db.create_all()  
print('Database created successfully') 

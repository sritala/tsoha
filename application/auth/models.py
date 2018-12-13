from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"
  
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    projects = db.relationship("Project", backref='account', lazy=True)
  
    def __init__(self, name):
        self.name = name
        
    def get_id(self):
        return self.id
  
    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_users_with_no_projects():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Project ON Project.account_id = Account.id"
                    " WHERE (Project.done IS null OR Project.done = truec)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Project.id) = 0")
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        return response
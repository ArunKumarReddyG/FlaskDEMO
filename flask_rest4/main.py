from flask import Flask,jsonify,request
from flask_restful import Api,Resource,reqparse,abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'

db = SQLAlchemy(app)

app.app_context().push()

class Task_model(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(20), nullable=True)
    age= db.Column(db.Integer, nullable=True)
    task= db.Column(db.String(20), nullable=True)

#db.create_all()

task_post_args = reqparse.RequestParser()
task_post_args.add_argument('name', type=str, help='name is required', required=True)
task_post_args.add_argument('age', type=int, help='age is required', required=True)
task_post_args.add_argument('task', type=str, help='task is required', required=True)

task_put_args = reqparse.RequestParser()
task_put_args.add_argument('name', type=str)
task_put_args.add_argument('age', type=int)
task_put_args.add_argument('task', type=str)

resource_fields={
    'id': fields.Integer,
    'name': fields.String,
    'age': fields.Integer,
    'task': fields.String
}

plans={}

def ID_notExists(p_id):
    if p_id not in plans:
        abort(404, message="ID not Exists")

def TID_notExists(p_id):
    res= Task_model.query.filter_by(id= p_id).first()
    if not res:
        abort(404, message='Task Id not found')
      

class TaskAPI(Resource):
    def get(self,p_id):
        ID_notExists(p_id)
        return plans[p_id]
    
    def post(self,p_id):
        args= task_post_args.parse_args()
        return {p_id: args}
    
    def put(self,p_id):
        ID_notExists(p_id)
        args= task_put_args.parse_args()
        plans[p_id] = args
        return plans[p_id],201
    
    def delete(self,p_id):
        ID_notExists(p_id)
        del plans[p_id]
        return plans,204

class TMres(Resource):
    @marshal_with(resource_fields)
    def get(self,t_id):
        TID_notExists(t_id)
        res= Task_model.query.filter_by(id= t_id).first()
        return res
    
    @marshal_with(resource_fields)
    def post(self,t_id):
        args= task_post_args.parse_args()
        res= Task_model.query.filter_by(id=t_id).first()
        if res:
            abort(409,message='ID Already Exists')

        p= Task_model(id=t_id, name= args['name'], age= args['age'], task=args['task'])
        db.session.add(p)
        db.session.commit()
        return p,201
    
    @marshal_with(resource_fields)
    def put(self,t_id):
        args= task_put_args.parse_args()
        res= Task_model.query.filter_by(id= t_id).first()
        if not res:
            abort(404, message='Task Id not found')
        if args['name']:
            res.name = args['name']
        if args['age']:
            res.age = args['age']
        if args['task']:
            res.task= args['task']
        db.session.commit()
        return res
    
    def delete(self,t_id):
        res= Task_model.query.filter_by(id= t_id).first()
        if not res:
            abort(404, message='Task Id not found')
        db.session.delete(res)
        db.session.commit()
        return "one task deleted", 204


api.add_resource(TaskAPI, "/task/<int:p_id>")
api.add_resource(TMres, "/mtask/<int:t_id>")

if __name__ == '__main__':
    app.run(debug=True)
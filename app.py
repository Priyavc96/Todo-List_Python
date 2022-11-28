from flask import Flask,render_template,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
class Todo(db.Model):
    task_id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))

class User(db.Model):
    u_id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    prime_account = db.Column(db.Boolean)

# @app.route('/')
# def login():
#     user = User.query.all()
#     return render_template('login.html',todo_list = user)

@app.route('/checklogin',methods=['POST'])
def checklogin():
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.get(username)
    db.session.commit()
    return render_template('redirect_user.html',user = user,password = password)
    # print("test")
    # if(user):
    #     print("in if")
    # for i in user or []:
    #     return redirect(url_for("home"))
    #     if(u.password == password):
    #         session['loggedin']=True
    #         session['u_id']=user.u_id
    #         return redirect(url_for("home"))
    # elif(user):
    #     return redirect(url_for("login"))
    # else:
    #     return redirect(url_for("register"))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerUser',methods=['POST'])
def registerUser():
    username = request.form.get("username")
    password = request.form.get("password")
    new_user = User(username=username,password=password,prime_account=False)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("login"))

# @app.route('/home')
@app.route('/')
def home():
    # if 'response' in session:
    todo_list = Todo.query.all()
    return render_template('base.html',todo_list = todo_list)
    # else:
    #     return redirect(url_for("login"))

@app.route('/add',methods=['POST'])
def add():
    # if 'response' in session:
    title = request.form.get("title")
    description = request.form.get("description")
    image = request.form.get("image")
    new_todo = Todo(title=title,description=description,image=image)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))
    # else:
    #     return redirect(url_for("login"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    # if 'response' in session:
    todoData = Todo.query.get(todo_id)
    db.session.commit()
    # return redirect(url_for("updateTask.html",tododata = todoData))
    return redirect(url_for("home"))
    # else:
    #     return redirect(url_for("login"))

@app.route('/updateData/')
def updateData():
    title = request.form.get("title")
    description = request.form.get("description")
    image = request.form.get("image")
    update_todo = Todo(title=title,description=description,image=image)
    todo = Todo.query.update(update_todo)
    db.session.commit()
    return redirect(url_for("base"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # if 'response' in session:
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))
    # else:
    #     return redirect(url_for("login"))

if __name__ == '__main__':
    app.run()
from flask import Flask,render_template,request,redirect,url_for,session
for i in user or []:
    if(u.password == password):
        session['loggedin']=True
        session['u_id']=user.u_id
        return redirect(url_for("home"))
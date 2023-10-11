from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import requests
import pickle
app= Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/true')
def true():
    return render_template('true.html')

@app.route('/false')
def false():
    return render_template('false.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        sex=request.form['sex']
        age=int(request.form['age'])
        height=int(request.form['height'])
        weight=int(request.form['weight'])
        waistline=float(request.form['waistline'])
        sight_left=float(request.form['sight_left'])
        sight_right=float(request.form['sight_right'])
        hear_left=request.form['hear_left']
        hear_right=request.form['hear_right']
        sbp=float(request.form['sbp'])
        dbp=float(request.form['dbp'])
        blds=float(request.form['blds'])
        tot_chole=float(request.form['tot_chole'])
        HDL_chole=float(request.form['HDL_chole'])
        LDL_chole=float(request.form['LDL_chole'])
        triglyceride=float(request.form['triglyceride'])
        hemoglobin=float(request.form['hemoglobin'])        
        urine_protein=request.form['urine_protein']
        serum_creatinine=float(request.form['serum_creatinine'])
        SGOT_AST=float(request.form['SGOT_AST'])
        SGOT_ALT=float(request.form['SGOT_ALT'])
        gamma_GTP=float(request.form['gamma_GTP'])
        SMK_stat_type_cd=request.form['SMK_stat_type_cd']

        scaled = scaler.transform(np.array([sex,age,height,weight,waistline,sight_left,sight_right,hear_left,hear_right,sbp,dbp,blds,tot_chole,HDL_chole,LDL_chole,triglyceride,hemoglobin,urine_protein,serum_creatinine,SGOT_AST,SGOT_ALT,gamma_GTP,SMK_stat_type_cd]).reshape(1, -1))
        prediction = model.predict(scaled)[0]
        output = ""
        if prediction == 0:
            output="false"
        else:
            output="true"
    return redirect(url_for(output))


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)

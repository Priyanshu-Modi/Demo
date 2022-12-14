from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np




app = Flask(__name__)



@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST','GET'])
   
def predict():
    
    item_weight= float(request.form['item_weight'])
    item_fat_content=float(request.form['item_fat_content'])
    item_visibility= float(request.form['item_visibility'])
    item_type= float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year= float(request.form['outlet_establishment_year'])
    outlet_size= float(request.form['outlet_size'])
    outlet_location_type= float(request.form['outlet_location_type'])
    outlet_type= float(request.form['outlet_type'])
    
    X = np.array([[ item_weight,item_fat_content,item_visibility,item_type,item_mrp,
                  outlet_establishment_year,outlet_size,outlet_location_type,outlet_type ]])


    scaler_path= r'C:\Users\Education\Desktop\Demo\models\sc.sav'

    sc=joblib.load(scaler_path)
     
 
    X_std= sc.transform(X)

    model_path=r'C:\Users\Education\Desktop\Demo\models\lr.sav'

    model= joblib.load(model_path)

    Y_predict =model.predict(X_std)

    Y_pred = round(Y_predict[0],2) 

    return render_template('predict.html', op = Y_pred)
    
 

if __name__ == "__main__":
    app.run(debug=True, port=5500)
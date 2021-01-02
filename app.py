from flask import Flask,render_template,url_for,request,jsonify
import pandas as pd
import pickle



app=Flask(__name__)


with open('model-XGB' ,'rb') as f1:
    loaded_model = pickle.load(f1)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
       Area_labels = request.form.get("Area_Labels_Category")
       if (Area_labels=='0-5 Marla'):
           Area_Category_Labels = 1
       elif(Area_labels=='5-10 Marla'):
           Area_Category_Labels = 2
       elif(Area_labels=='10-15 Marla'):
           Area_Category_Labels = 3
       elif(Area_labels=='15-20 Marla'):
           Area_Category_Labels = 4
       elif(Area_labels=='1-5 Kanal'):
           Area_Category_Labels = 5
       elif(Area_labels=='5-10 Kanal'):
           Area_Category_Labels = 6
       elif(Area_labels=='10-15 Kanal'):
           Area_Category_Labels = 7
       elif(Area_labels=='15-20 Kanal'):
           Area_Category_Labels = 8
       elif(Area_labels=='20-30 Kanal'):
           Area_Category_Labels = 9
       elif(Area_labels=='30-40 Kanal'):
           Area_Category_Labels = 10
       elif(Area_labels=='40-50 Kanal'):
           Area_Category_Labels = 11
       elif(Area_labels=='50-60 Kanal'):
           Area_Category_Labels = 12
       elif(Area_labels=='60-70 Kanal'):
           Area_Category_Labels = 13
       elif(Area_labels=='70-80 Kanal'):
           Area_Category_Labels = 14
       elif(Area_labels=='80-90 Kanal'):
           Area_Category_Labels = 15
       elif(Area_labels=='90-100 Kanal'):
           Area_Category_Labels = 16
       elif(Area_labels=='100-200 Kanal'):
           Area_Category_Labels = 17
       elif(Area_labels=='200-300 Kanal'):
           Area_Category_Labels = 18
       elif(Area_labels=='400-500 Kanal'):
           Area_Category_Labels = 19
       elif(Area_labels=='500-600 Kanal'):
           Area_Category_Labels = 20
       elif(Area_labels=='600-700 Kanal'):
           Area_Category_Labels = 21
       elif(Area_labels=='700-800 Kanal'):
           Area_Category_Labels = 22
           
           
       Purpose = request.form.get("purpose")
       if (Purpose=='For Sale'):
           purpose_for_sale = 1
       elif(Purpose=='For Rent'):
           purpose_for_sale = 0
       
        
       bedrooms=request.form.get("bedroom")
       if (bedrooms=="1"):
           Bedrooms=2
       elif(bedrooms=="2"):
           Bedrooms = 3
       elif(bedrooms=="3"):
           Bedrooms=4
       elif(bedrooms=="4"):
           Bedrooms=7
       elif(bedrooms=="5"):
           Bedrooms=8
       elif(bedrooms=="6"):
           Bedrooms=9
       elif(bedrooms=="7"):
           Bedrooms=11
       elif(bedrooms=="8"):
           Bedrooms=10
       elif(bedrooms=="9"):
           Bedrooms=12
       elif(bedrooms=="10"):
           Bedrooms=14
       elif(bedrooms=="11"):
           Bedrooms=15
       elif(bedrooms=="12"):
           Bedrooms=17
       elif(bedrooms=="13"):
           Bedrooms=6
       elif(bedrooms=="14"):
           Bedrooms=13
       elif(bedrooms=="15"):
           Bedrooms=18
       elif(bedrooms=="16"):
           Bedrooms=19
       elif(bedrooms=="18"):
           Bedrooms=21
       elif(bedrooms=="21"):
           Bedrooms=0
       elif(bedrooms=="25"):
           Bedrooms=20
       elif(bedrooms=="27"):
           Bedrooms=16
       elif(bedrooms=="28"):
           Bedrooms=1
       elif(bedrooms=="0"):
           Bedrooms=5
           
           
       Property=request.form.get("property")
       if (Property=='Room'):
           Propert_Types=0
       elif(Property=='Lower Portion'):
           Propert_Types = 1
       elif(Property=='Upper Portion'):
           Propert_Types = 2
       elif(Property=='Flat'):
           Propert_Types=3
       elif(Property=='Penthouse'):
           Propert_Types=4
       elif(Property=='House'):
           Propert_Types=5
       elif(Property=='Farm House'):
           Propert_Types=6
       
        
       
        
       baths=request.form.get("bath")
       if (baths=="1"):
           Baths=1
       elif(baths=="2"):
           Baths = 2
       elif(baths=="3"):
           Baths=3
       elif(baths=="4"):
           Baths=4
       elif(baths=="5"):
           Baths=6
       elif(baths=="6"):
           Baths=7
       elif(baths=="7"):
           Baths=8
       elif(baths=="8"):
           Baths=10
       elif(baths=="9"):
           Baths=9
       elif(baths=="10"):
           Baths=12
       elif(baths=="11"):
           Baths=14
       elif(baths=="12"):
           Baths=11
       elif(baths=="13"):
           Baths=13
       elif(baths=="14"):
           Baths=0
       elif(baths=="0"):
           Baths=5
           
           
           
       cityy=request.form.get("city")
       if (cityy=='Faisalabad'):
           City=0
       elif(cityy=='Rawalpindi'):
           City= 1
       elif(cityy=='Islamabad'):
           City=2
       elif(cityy=='Karachi'):
           City=3
       elif(cityy=='Lahore'):
           City=4
           
           
      
        
       province=request.form.get("prov")
       if (province=='Islamabad Capital'):
           Province=0
       elif(province=='Punjab'):
           Province= 1
       elif(province=='Sindh'):
           Province=2
           
           
       Area_Size=float(request.form.get("size"))
       
       
       
       
       Type = request.form.get("areatype")
       if (Type=='Marla'):
           Area_Type_Marla = 1
       elif(Type=='Kanal'):
           Area_Type_Marla = 0
           
           
       data={'Area Category Labels':[Area_Category_Labels],
       'purpose_For Sale':[purpose_for_sale],
       'Bedrooms':[Bedrooms],
       'Propert_Types':[Propert_Types],
       'Baths':[Baths],
       'City':[City],
       'Province':[Province],
       'Area Size':[Area_Size],
       'Area Type_Marla':[Area_Type_Marla]
       }
       
       final = pd.DataFrame (data, columns=['Area Category Labels','purpose_For Sale','Bedrooms','Propert_Types','Baths','City','Province','Area Size','Area Type_Marla'])
       prediction=loaded_model.predict(final)
       return render_template('index.html', prediction_text="The calculated price is Rs.{}".format(prediction))
       
       
       
       
        
       
        
if __name__=="__main__":
    app.run()

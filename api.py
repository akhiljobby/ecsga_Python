
from flask import Flask, request
import pandas as pd
app=Flask (__name__)

@app.route("/")
def api():
   
    return "Hello World"
    # use http://localhost:5000 in the browser

#@app.route("/preview")
#def preview():
#    df=pd.read_csv("physician_rx.csv")
#    preview_df=df.head()
#    #return preview_df.to_json(orient="records")
#    return preview_df.to_html()
#    # use http://localhost:5000/preview in the browser

@app.route("/column/<column_name>")
def column_preview(column_name):
    df=pd.read_csv("physician_rx.csv")
    return df[[column_name]].to_html()
    # use http://localhost:5000/column/CroMax_RX in the browser

    # return df[column_name].to_frame.to_html()    
    # You can use "to_frame" instead of double square brackets [[]]
    # command in the return statement (line 23) to covert the pandas series type to dataframe 
    

@app.route("/preview")
def preview():
    df=pd.read_csv("physician_rx.csv")
    rows_count=request.args.get("rows", type=int, default= 5)
    preview_df=df[0:rows_count]
    return preview_df.to_html()
    # use http://localhost:5000/preview?rows=3 in the browser  3 or 4 or 7 or empty(complete)
    # or use default=5 to return 5 records instead of all (~preview?rows=)

if __name__=='__main__':
    app.run()
from flask import Flask,current_app,render_template
import subprocess
app=Flask(__name__,static_url_path="")
app.debug=True
@app.route('/')
def index():
	return current_app.send_static_file('index.html')


def query_crop():
        import urllib2,json
        data =  {

                "Inputs": {

                        "input1":
                            {
                                "ColumnNames": ["Year", "State", "District", "Crop", "Season", "Area(in Hectares)", "Production(in Tonnes)", "Yield"],
                                "Values": [ [ "0", "ORISSA", "CUTTACK", "Jute", "Kharif", "0", "0", "" ] ]
                            },        },
                        "GlobalParameters": {
                        }
                }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/d1fc9bca76844334bedb27fa36b110a8/services/eb9cda47deff4ccaafaaa6512f853cef/execute?api-version=2.0&details=true'
        api_key = 'dAdYFj+yFUeT9ynnqE8JDInihmSV6UnpDxhMsT3qnYRAyzFOQ4TzcgUJyHYmFmxe7tWPECbLjfIFLm8WpJq05w==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib2.Request(url, body, headers) 
        try:
            response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)
    	    result = response.read()
    	    a=json.loads(result)
    	    print type(a)

            return a
        except urllib2.HTTPError, error:
            print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())

        print(json.loads(error.read()))    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=12345)
import json
import requests

Jenkins_url = "http://localhost:8088"
token = "lex-automation"

def trigger_jenkins(region, instance_type, cloud, env, app_name):
    
    AWS_JENKINS_URL="{0}/job/terraform-poc/job/aws-deployment/buildWithParameters".format(Jenkins_url)
    AZURE_JENKINS_URL="{0}/job/terraform-poc/job/azure-deployment/buildWithParameters".format(Jenkins_url)
    
    auth = ('admin', 'admin') 
    jenkins_headers={'Content-type':'application/json', 'Accept':'application/json'}
    
    aws_json_payload={"app_name" : app_name, \
                      "app_environment": env, \
                      "aws_region": region, \
                      "instance_type": instance_type }
    
    azure_json_payload={"app_name" : app_name, \
                      "app_environment": env, \
                      "rg_location": region
                     }

    crumb_data= requests.get("{0}/crumbIssuer/api/json".format(Jenkins_url), \
        auth = auth,headers={'content-type': 'application/json'})
    
    if str(crumb_data.status_code) == "200":
        if cloud == 'aws':
            json_data=json.dumps(aws_json_payload)
            print("Json data to be posted : {}".format(str(json_data)))
            
            data = requests.get("{0}?token={1}".format(AWS_JENKINS_URL, token), \
            auth=auth,params=json_data, \
            headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})

        elif cloud == 'azure':
            json_data=json.dumps(azure_json_payload)
            print("Json data to be posted : {}".format(str(json_data)))
            
            data = requests.get("{0}?token={1}".format(AZURE_JENKINS_URL, token), \
            auth=auth,params=json_data, \
            headers={'content-type': 'application/json','Jenkins-Crumb':crumb_data.json()['crumb']})
        
        print("Respose headers from execution : {}".format(str(data.headers)))
        print("Respose from execution : {}".format(str(data)))
        
        if str(data.status_code) == "201":
            return "{} execution initiated for your request in the backend system. Please note your build number for future reference. Thanks you!".format(data.headers['Location'])
        else:
            return "There was an error encounted while initiating your request. Please contact deployment team for the same. Thank you!"
    
def lambda_handler(event, context):
    print('received request: ' + str(event))
    print(event['currentIntent'])
    slots = event['currentIntent']['slots']
    
    region = slots['region']
    instance_type = slots['instance'] 
    cloud = slots['cloud']
    env =  slots['env']
    app_name = "DemoApp"
    
    status = trigger_jenkins(region, instance_type, cloud, env, app_name)
    
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": status
            },
        }
    }

    return response

# OpsBot Using Amazon Lex and Slack
We are using the [multi-cloud deployment](https://github.com/ganeshcpote/terraform-multicloud-example) example from Jenkins to the below demo. The slack bot will interact with us followed by required questions to start the Jenkins build (Jenkins Parameter) to provision AWS infrastructure. Onde deployment is done, an email notification will trigger to the user and online hosted online on AWS environment

## Step 1 : Write Lambda Code
* Create Python based Lambda function "TriggerJenkins" which process the user inputs
* The code is located in /lambda/lambda_function.py file
* It looks like below in AWS console
![opsbot](/images/lambda_code.png)

## Step 2 : Create Amazon Lex Bot
* Create Bot in Amazon Lex called as "OpsBot"
* Create new intent call "CreateVM"
* Add following utterances into intent
![opsbot](/images/utterances.png)
* Add following slots 
![opsbot](/images/slots.png)
* Add Confirmation Prompt and lambda integration (select the lambda function created in Step 1)
![opsbot](/images/lambda.png)
* Save the bot 

## Step 3 : Slack Inegration
* [Step 1 : Create New Slack Application](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-app.html)
* [Step 2 : Integrate the Slack Application with the Amazon Lex Bot](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-assoc-create-assoc.html)
* [Step 3 : Complete Slack Integration](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-back-in-slack-console.html)
* [Step 4 : Test Integration](https://docs.aws.amazon.com/lex/latest/dg/slack-bot-test.html)

## Demo - Interact with Slack "Cloud Service" Bot
![Watch the Video](/video/play.gif)

## Jenkins Execution
* ![opsbot](https://github.com/ganeshcpote/terraform-multicloud-example/blob/master/images/jenkins.PNG)

## Email Notification
* ![opsbot](https://github.com/ganeshcpote/terraform-multicloud-example/blob/master/images/email.png)

## AWS Apache Website
* ![opsbot](https://github.com/ganeshcpote/terraform-multicloud-example/blob/master/images/aws-web.png)

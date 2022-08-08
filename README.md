# Create Database through Lambda function, SSM and Secret Manager 

## Introduction:
In this article we will create a Database using Lambda function and get the username and password details from SSM and Secret Manager.
We use Parameter Store from SSM Service to fetch the Username and Endpoint, and for the Password we use Secret Manager.
Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management.
AWS Secrets Manager is a secrets management service that helps you protect access to your applications, services, and IT resources.

Following are the steps to create databse using Lambda:
1. Install pymysql locally.
2. Write you lambda code in the same directory.
3. Create a Lambda function.
4. Upload the Zip folder of pymysql module and code to the lambda function.

## Step-By-Step Explanation:
1. Install pymysql Locally:
      * Use the following command to install pymysql- pip install pymysql
      
2. Lambda Code:
      * In the same directory write your lambda code and name the file as lambda_function.py

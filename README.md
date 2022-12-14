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

## Step-By-Step Explanation:
1. Install pymysql Locally:
      * Create a Project directory.
      * Use the following command to install pymysql- pip install pymysql
      
2. Lambda Code:
      * In the same directory write your lambda code and name the file as lambda_function.py
      * [Refer the file](https://github.com/KAJOLMEHTAA/Database/blob/main/lambda_function.py) for the Lambda Code 
      
3. Create a Lambda Function:
      * Open Lambda Console, Create Function
      * Enter the function Name, Select Python 3.9, create a IAM role with required policies and attach the same to the Lambda function. 
      * Click on Create Function, will redirect to the Function page with Basic Lambda Code.
      * Select upload from .zip from dropdown and upload the zipped files(pymysql module and lambda code)
      
## Useful Links
https://www.youtube.com/watch?v=yyBSeGkuPqk 

## Databse access commands
To view all database: show databases; 
Go inside the database: use test; #Define the database name
show tables;

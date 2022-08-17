import json
import boto3
import pymysql
def lambda_handler(event, context):
    print(event)

    #parameter Client
    ssm = boto3.client('ssm')
    
    #retrieve Username from Parameter store
    parameter = ssm.get_parameter(Name='Username', WithDecryption=True)
    username = parameter['Parameter']['Value']
    
    #retrieve Endpoint from Parameter store
    end = ssm.get_parameter(Name='Endpoint', WithDecryption=True)
    endpoint = end['Parameter']['Value']
    
    #Print statements
    print("Username", username)
    print("Endpoint", endpoint)

    #Secret Manager client
    client= boto3.client('secretsmanager')
    
    #retrieve password from secret manager
    response= client.get_secret_value(
        SecretId='rdsecret'
    )
    secret= json.loads(response['SecretString'])
    passw= secret['Password']
    print (passw)
    
    # establish connection to MySQL
    mydb = pymysql.connect(
        # specify host
        host=endpoint,
        # specify root account
        user=username,
        # specify password for root account
        password=passw,
        # default port number is 3306 fro MySQL
        port=3306
    )
    
    # make a cursor to run sql queries
    cursor= mydb.cursor()
    password = "secret"
    pass_formt = "'{}'".format(password)
    create_user = "CREATE USER 'testuser'@'localhost' IDENTIFIED BY " + pass_formt
    cursor.execute(create_user)
    cursor.execute("CREATE database test") #Define a new database evrytime you create
    cursor.execute("grant all privileges on test.* to 'testuser'@'localhost'")
    cursor.execute("Flush Privileges")
    
    # close connection to MySQL
    mydb.close()
    
    

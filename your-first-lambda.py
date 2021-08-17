def lambda_handler(event, context):
    print("Inside the lambda handler")

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "Emily, Niesoth, Usna & Ehelsan, Rahat! You have successfully invoked your first Lambda. Great job!"
    }

    return response
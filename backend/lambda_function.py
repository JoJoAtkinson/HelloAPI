

import json

def lambda_handler(event, context):
    """ Handles function event and context """

    # https://dev.to/vahdet/creating-a-ci-cd-pipeline-for-a-python3-lambda-function-through-aws-cloudformation-4ck6

    # TODO implement further business logic
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
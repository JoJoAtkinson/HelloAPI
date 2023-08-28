
import boto3, json
from boto3_type_annotations.dynamodb.service_resource import ServiceResource

def lambda_handler(event, context):
    """ Handles function event and context """

    # https://dev.to/vahdet/creating-a-ci-cd-pipeline-for-a-python3-lambda-function-through-aws-cloudformation-4ck6

    db: ServiceResource = boto3.resource("dynamodb", region_name="us-east-2")
    
    tbl = db.Table("demo_table")
    tbl.put_item(Item={"id": "hello", "value": "world"})

    # TODO implement further business logic
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

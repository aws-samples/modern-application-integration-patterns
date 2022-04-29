import boto3
import os
import json
import traceback

connections_table = os.environ.get("CONNECTIONS_TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(connections_table)


def lambda_handler(event, context):
    try:
        print(event)
        event_body = json.loads(event["body"])
        executionArn = event_body["executionArn"]
        websocket_connectionId = event["requestContext"]["connectionId"]

        table.put_item(
            Item={"ExecutionArn": executionArn, "WsClientId": websocket_connectionId},
        )

    except Exception as e:
        err_msg = (
            "Error on connect, please check logs and ensure you have supplied valid body & executionArn parameters, error details:\n"
            + traceback.format_exc()
        )
        print(err_msg)
        return {
            "statusCode": 500,
            "body": err_msg,
        }

    return {"statusCode": 200, "body": "Connected"}

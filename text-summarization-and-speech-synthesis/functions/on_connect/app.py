import boto3
import os
import json

connections_table = os.environ.get("CONNECTIONS_TABLE_NAME")

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(connections_table)


def lambda_handler(event, context):
    try:
        print(event)
        event_body = json.loads(event.get("body"))
        executionArn = str(event_body.get("executionArn"))
        websocket_connectionId: str = str(event["requestContext"]["connectionId"])

        table.put_item(
            Item={"ExecutionArn": executionArn, "WsClientId": websocket_connectionId},
        )

        result = {
            "state_machine_execution": executionArn,
            "connectionId": websocket_connectionId,
        }
    except Exception as e:
        print(e)

    return {"statusCode": 200, "body": "Connected"}

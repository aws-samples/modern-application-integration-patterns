import boto3
import os
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

execution_table = os.environ.get("TABLE_NAME")

dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(execution_table)


class DatabaseException(Exception):
    pass


def lambda_handler(event, context):
    print(event)

    websocket_connectionId = event["requestContext"]["connectionId"]
    websocket_connection_index_name = table.global_secondary_indexes[0]["IndexName"]

    try:
        connection_query_resp = table.query(
            IndexName=websocket_connection_index_name,
            KeyConditionExpression=Key("WsClientId").eq(websocket_connectionId),
        )

        print("query_results", connection_query_resp)

        if connection_query_resp.get("Items"):
            item = connection_query_resp["Items"][0]
            print(item)
            execution_id = item["ExecutionArn"]
            table.delete_item(Key={"ExecutionArn": execution_id})
    except ClientError as error:
        raise DatabaseException from error
    else:
        return

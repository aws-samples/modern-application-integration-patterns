import os
import boto3
from urllib.parse import urlparse

DEFAULT_EXPIRATION = 900
API_REGION = os.environ.get("API_REGION")

s3_client = boto3.client("s3", region_name=API_REGION)

INPUT_PARAMETER_NAME = "inputUri"


class InvalidInputUriException(Exception):
    pass


def lambda_handler(event, context):
    uri_to_sign = event.get(INPUT_PARAMETER_NAME)

    if not uri_to_sign:
        raise InvalidInputUriException

    link_expiration = event.get("link_expiry", DEFAULT_EXPIRATION)

    url_path = urlparse(uri_to_sign).path
    split_path = url_path.split("/")
    s3_bucket = split_path[1]
    s3_object = split_path[2]

    params = {"Bucket": s3_bucket, "Key": s3_object}
    signed_link = s3_client.generate_presigned_url(
        "get_object", Params=params, ExpiresIn=link_expiration
    )

    print("s3 pre-signed URL: " + signed_link)

    return {"signed_s3_link": signed_link}

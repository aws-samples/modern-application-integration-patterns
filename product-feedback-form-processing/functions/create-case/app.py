import uuid

def lambda_handler(event, context):
    case_id = str(uuid.uuid4())
    return case_id


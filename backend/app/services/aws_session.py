import boto3

def create_session(access_key: str, secret_key: str, region: str):
    return boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

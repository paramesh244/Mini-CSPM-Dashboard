def fetch_s3_buckets(session):
    s3 = session.client("s3")
    buckets = s3.list_buckets()["Buckets"]

    results = []

    for bucket in buckets:
        name = bucket["Name"]

        results.append({
            "name": name,
            "type": "S3",
            "encryption": is_encrypted(s3, name),
            "public": is_public(s3, name),
            "logging": has_logging(s3, name),
            "versioning": has_versioning(s3, name)
        })

    return results


def is_encrypted(s3, bucket):
    try:
        s3.get_bucket_encryption(Bucket=bucket)
        return True
    except:
        return False


def is_public(s3, bucket):
    try:
        pab = s3.get_public_access_block(Bucket=bucket)
        return not all(pab["PublicAccessBlockConfiguration"].values())
    except:
        return True


def has_logging(s3, bucket):
    try:
        response = s3.get_bucket_logging(Bucket=bucket)
        return "LoggingEnabled" in response
    except:
        return False


def has_versioning(s3, bucket):
    try:
        response = s3.get_bucket_versioning(Bucket=bucket)
        return response.get("Status") == "Enabled"
    except:
        return False

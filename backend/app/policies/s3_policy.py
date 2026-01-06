def evaluate_s3(bucket):
    if (
        not bucket["encryption"]
        or bucket["public"]
        or not bucket["logging"]
        or not bucket["versioning"]
    ):
        return "High Risk"
    return "Low Risk"

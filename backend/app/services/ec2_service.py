def fetch_ec2_instances(session):
    ec2 = session.client("ec2")
    response = ec2.describe_instances()

    instances = []

    for reservation in response.get("Reservations", []):
        for inst in reservation.get("Instances", []):
            instances.append({
                "id": inst["InstanceId"],
                "type": "EC2",
                "state": inst["State"]["Name"],
                "public_ip": inst.get("PublicIpAddress")
            })

    return instances

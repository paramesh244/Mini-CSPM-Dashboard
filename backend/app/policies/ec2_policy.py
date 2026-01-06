def evaluate_ec2(instance):
    if instance["state"] == "running" and instance["public_ip"]:
        return "High Risk"
    return "Low Risk"

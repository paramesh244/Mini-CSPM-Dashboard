from app.policies.ec2_policy import evaluate_ec2

def test_running_public_ec2_is_high_risk():
    instance = {
        "state": "running",
        "public_ip": "1.2.3.4"
    }
    assert evaluate_ec2(instance) == "High Risk"


def test_stopped_or_private_ec2_is_low_risk():
    instance = {
        "state": "stopped",
        "public_ip": None
    }
    assert evaluate_ec2(instance) == "Low Risk"

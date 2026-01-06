from fastapi import APIRouter, HTTPException
from botocore.exceptions import ClientError

from app.schemas.scan import ScanRequest
from app.services.aws_session import create_session
from app.services.ec2_service import fetch_ec2_instances
from app.services.s3_service import fetch_s3_buckets
from app.policies.ec2_policy import evaluate_ec2
from app.policies.s3_policy import evaluate_s3

router = APIRouter()

@router.post("/scan")
def scan_resources(payload: ScanRequest):
    try:
        session = create_session(
            payload.access_key,
            payload.secret_key,
            payload.region
        )

        ec2_instances = fetch_ec2_instances(session)
        s3_buckets = fetch_s3_buckets(session)

        resources = []
        high_risk = 0

        for inst in ec2_instances:
            risk = evaluate_ec2(inst)
            if risk == "High Risk":
                high_risk += 1

            resources.append({
                "id": inst["id"],
                "type": "EC2",
                "status": inst["state"],
                "risk": risk
            })

        for bucket in s3_buckets:
            risk = evaluate_s3(bucket)
            if risk == "High Risk":
                high_risk += 1

            resources.append({
                "name": bucket["name"],
                "type": "S3",
                "risk": risk
            })

        return {
            "total_assets": len(resources),
            "high_risk_assets": high_risk,
            "resources": resources
        }

    except ClientError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )

# Architecture & System Design

This document describes the proposed production architecture for the **Mini CSPM Dashboard**, focusing on scalability, security, and operational simplicity.

---

## 1. High-Level Overview

The application consists of:
- A **React-based frontend** for user interaction
- A **FastAPI backend** that scans AWS resources and evaluates security posture
- **AWS-managed services** for secure, scalable deployment

The system is designed to be **stateless**, with no persistent storage of credentials or scan results.

---

## 2. Deployment Strategy

### Frontend Deployment
- The React application is built into static assets.
- Assets are hosted in an **Amazon S3 bucket** configured for static website hosting.
- **Amazon CloudFront** is used as a CDN to:
  - Improve performance
  - Enforce HTTPS
  - Provide global edge caching

### Backend Deployment
- The FastAPI backend is containerized using Docker.
- Containers are deployed on **Amazon ECS with Fargate**.
- An **Application Load Balancer (ALB)**:
  - Terminates TLS (HTTPS)
  - Routes traffic to ECS tasks
- Backend services run in **private subnets** within a VPC.

### Security
- HTTPS is enforced using **AWS Certificate Manager (ACM)**.
- AWS credentials provided by users are:
  - Encrypted in transit via TLS
  - Used only in memory
  - Never logged or persisted
- IAM roles are used for ECS task permissions.

---

## 3. Service Selection & Justification

### Backend: ECS Fargate vs Lambda
**Chosen:** ECS Fargate

**Why ECS Fargate:**
- Long-running API service (not event-based)
- Better suited for:
  - Boto3-based AWS scans
  - Network-bound operations
  - Predictable performance
- Easier debugging and observability compared to Lambda

**Why not Lambda:**
- Cold start latency
- Execution time limits
- Less suitable for multi-service AWS scans

---

### Storage: No Database (Intentional)
- The application is **stateless**
- Scan results are computed on-demand
- No need for RDS or DynamoDB

**Future extension (optional):**
- DynamoDB could be added for scan history or audit logs

---

### Frontend: S3 + CloudFront
**Chosen:** S3 + CloudFront

**Why:**
- Fully managed
- Cost-effective
- Highly scalable
- Native HTTPS support
- Ideal for static React applications

---

### Networking
- VPC with:
  - Public subnets for ALB
  - Private subnets for ECS tasks
- Security groups restrict traffic:
  - ALB → ECS only
  - No direct public access to backend containers

---

## 4. Infrastructure Diagram

### Mermaid Diagram
```mermaid
graph TD
    User -->|HTTPS| CloudFront
    CloudFront --> S3[React Frontend]
    CloudFront --> ALB[Application Load Balancer]
    ALB --> ECS[ECS Fargate - FastAPI]
    ECS --> AWS[AWS APIs (EC2, S3)]

## 5. Scalability & Reliability

- Horizontal scaling via ECS Service Auto Scaling

- Stateless backend enables easy scaling

- CloudFront reduces backend load

- ALB health checks ensure high availability

## 6. Observability & Operations

- CloudWatch Logs for backend logging

- ALB access logs for traffic analysis

- Container-level monitoring via ECS metrics

## 7. Security Considerations

- Enforced HTTPS for all external traffic

- No credential persistence

- Least-privilege IAM policies

- Backend isolated in private subnets

## 8. Future Improvements

- Use AWS STS AssumeRole instead of static credentials

- Add authentication for dashboard access

- Persist scan results for historical analysis

- Add CI/CD using GitHub Actions and ECS blue/green deployments

## 9. Summary

- This architecture prioritizes:

- Security-first design

- Operational simplicity

- Scalability

- Clear separation of concerns

- It reflects a production-ready CSPM system while remaining intentionally minimal for clarity and maintainability.
![Unit Tests](https://github.com/piotr-muzyka/aws-iam-hound/workflows/unit-tests.yml/badge.svg)
![Trivy - Dependency Vulnerability Scan](https://github.com/piotr-muzyka/aws-iam-hound/actions/workflows/trivy-scan.yml/badge.svg)


# AWS Hound

## Table of Contents

- [Purpose](#purpose)
- [Repository Structure](#repository-structure)
- [Features](#features)
- [Workflows](#workflows)
  - [Python Unit-Tests Workflow](#1-python-tests-workflow-python-unit-testsyml) 
  - [Security Scanning Workflow](#2-security-scanning-workflow-trivy-scanyml)
- [Deployment Instructions](#deployment-instructions)
  - [Prerequisites](#prerequisites)
  - [Deploying with GitHub Actions](#deploying-with-github-actions)
  - [Manual Deployment](#manual-deployment)
- [Testing the Solution](#testing-the-solution)
  - [Using the Test Resources Workflow](#using-the-test-resources-workflow)
  - [Manual Testing](#manual-testing)

AWS Hound is a monitoring solution intended to alert AWS security events in your AWS environment. It monitors for IAM user creation, access key generation, S3 bucket policy changes, and security group modifications that could potentially expose resources publicly.

## Setup
Tested with:
- Terraform  `v1.5.7`
- hashicorp/aws `v5.91`

## Repository Structure

```
/
├── main.py                     # Lambda function entry point
├── event_processor.py          # Core logic for processing security events
├── sns_client.py               # SNS notification functionality
├── requirements.txt            # Python dependencies
├── deploy/terraform/                  # Terraform configuration
│   ├── main.tf                 # Main Terraform configuration
│   ├── variables.tf            # Input variables
│   ├── outputs.tf              # Output values
│   └── modules/                # Modular Terraform components
│       ├── lambda/             # Lambda function configuration
│       ├── cloudwatch/         # CloudWatch event rules
│       ├── sns/                # SNS topic for notifications
│       ├── iam/                # IAM roles and policies
│       └── cloudtrail/         # CloudTrail configuration
├── tests/                      # Modular Terraform components
│   ├── test_event_processor.py
│   ├── test_main.py
│   ├── test_sns_client.py
│   ├── test_utils.py
│   └── terraform/
│       ├── main.tf             # Lambda function configuration
│       ├── provider.tf         # CloudWatch event rules
│       └── variables.tf         # SNS topic for notifications
└── .github/
    └── workflows/
        ├── deploy.yml          # Main deployment workflow
        ├── deploy-test-resources.yml  # Test resources deployment
        └── python-tests.yml    # Python unit tests workflow
```

## Workflows

### 1. Python Unit-Tests Workflow (`unit-tests.yml`)

This workflow runs unit tests for the Python code.

- **Trigger**: Runs on pushes to main/master branch or pull requests
- **Actions**:
    - Runs pytest on the Python codebase

### 2. Security Scanning Workflow (`trivy-scan.yml`)

This workflow performs comprehensive security scanning of the codebase using Trivy, a vulnerability scanner that detects security issues in code, dependencies, and infrastructure configurations.

- **Trigger**: Runs on pushes to main/master branch, pull requests, weekly schedule, or manual trigger
- **Actions**:
    - Scans repository for vulnerabilities and misconfigurations
    - Identifies vulnerable dependencies in requirements.txt
    - Provides detailed vulnerability information with severity levels
    - Suggests remediation steps for identified issues

## Deployment Instructions

### Prerequisites

1. AWS account with appropriate permissions
2. GitHub repository with this code
3. GitHub repository secrets:
    - `AWS_ACCESS_KEY_ID`: Your AWS access key
    - `AWS_SECRET_ACCESS_KEY`: Your AWS secret key

### Deploying with GitHub Actions

1. **Set up GitHub repository secrets**:
    - Go to your repository on GitHub
    - Navigate to Settings > Secrets and variables > Actions
    - Add the required secrets (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`)
2. **Trigger the deployment workflow**:
    - Go to the Actions tab in your repository
    - Select the "Deploy Lambda with Terraform" workflow
    - Click "Run workflow"
    - Select the branch to deploy from
    - Click "Run workflow" again
3. **Monitor the deployment**:
    - The workflow will show progress in real-time
    - Once complete, it will output information about the deployed resources

### Manual Deployment

If you prefer to deploy manually:

1. **Install prerequisites**:

```bash
# Install Terraform
brew install terraform  # macOS
# or
sudo apt-get install terraform  # Ubuntu

# Install AWS CLI
pip install awscli
aws configure  # Set up your AWS credentials (don't user root account! Create a custom account for terraform deployment, below is a set of required policies
```

```
# Deployment account permissions
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:GetFunction",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:DeleteFunction",
                "lambda:AddPermission",
                "lambda:RemovePermission",
                "lambda:GetPolicy",
                "lambda:ListVersionsByFunction",
                "lambda:GetFunctionCodeSigningConfig"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateUser",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:GetRole",
                "iam:GetPolicy",
                "iam:GetPolicyVersion",
                "iam:ListPolicyVersions",
                "iam:ListRolePolicies",
                "iam:PutRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:AttachRolePolicy",
                "iam:DetachRolePolicy",
                "iam:CreatePolicy",
                "iam:ListAttachedRolePolicies",
                "iam:ListInstanceProfilesForRole",
                "iam:PassRole",
                "iam:DeletePolicy",
                "iam:GetRolePolicy",
                "iam:TagUser",
                "iam:GetUser",
                "iam:ListGroupsForUser",
                "iam:DeleteUser",
                "iam:CreateAccessKey",
                "iam:ListAccessKeys",
                "iam:DeleteAccessKey"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sns:CreateTopic",
                "sns:DeleteTopic",
                "sns:GetTopicAttributes",
                "sns:SetTopicAttributes",
                "sns:Subscribe",
                "sns:Unsubscribe",
                "sns:ListTagsForResource",
                "sns:GetSubscriptionAttributes"
            ],
            "Resource": "arn:aws:sns:us-east-1:120569630424:iam-user-creation-alerts"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:DeleteLogGroup",
                "logs:DescribeLogGroups",
                "logs:CreateLogStream",
                "logs:DeleteLogStream",
                "logs:DescribeLogStreams",
                "logs:PutRetentionPolicy",
                "logs:DescribeLogGroups",
                "logs:ListTagsLogGroup",
                "logs:ListTagsForResource"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:ListTagsLogGroup"
            ],
            "Resource": "arn:aws:logs:us-east-1:120569630424:log-group::log-stream*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "events:PutRule",
                "events:DeleteRule",
                "events:DescribeRule",
                "events:PutTargets",
                "events:RemoveTargets",
                "events:ListTagsForResource",
                "events:ListTargetsByRule",
                "events:PutRule"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy",
                "s3:PutBucketAcl",
                "s3:GetBucketAcl",
                "s3:PutBucketVersioning",
                "s3:GetBucketVersioning",
                "s3:PutBucketPublicAccessBlock",
                "s3:GetBucketPublicAccessBlock",
                "s3:ListAllMyBuckets",
                "s3:DeleteObject",
                "s3:ListBucket",
                "s3:ListBucketVersions",
                "s3:DeleteBucketPolicy",
                "s3:DeleteBucketWebsite",
                "s3:DeleteObjectVersion",
                "s3:GetObject",
                "s3:GetObjectVersion",
                "s3:GetBucketCORS",
                "s3:GetBucketWebsite",
                "s3:GetAccelerateConfiguration",
                "s3:GetBucketRequestPayment",
                "s3:GetBucketLogging",
                "s3:GetReplicationConfiguration",
                "s3:GetLifecycleConfiguration",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketObjectLockConfiguration",
                "s3:GetBucketTagging"
            ],
            "Resource": "arn:aws:s3:::cloudtrail-iam-logs-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:PutBucketPolicy",
                "s3:GetBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::hound-test-bucket-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudtrail:CreateTrail",
                "cloudtrail:DeleteTrail",
                "cloudtrail:UpdateTrail",
                "cloudtrail:StartLogging",
                "cloudtrail:StopLogging",
                "cloudtrail:DescribeTrails",
                "cloudtrail:GetTrailStatus",
                "cloudtrail:GetEventSelectors",
                "cloudtrail:LookupEvents",
                "cloudtrail:AddTags",
                "cloudtrail:ListTags",
                "cloudtrail:RemoveTags",
                "cloudtrail:PutEventSelectors"
            ],
            "Resource": "*"
        }
    ]
}
```

2. **Create Lambda deployment package**:

```bash
mkdir -p package
pip install -r requirements.txt --target ./package
cp *.py package/
cd package
zip -r ../lambda_function.zip .
cd ..
```

3. **Deploy with Terraform**:

```bash
cd terraform
terraform init
terraform plan -var="lambda_zip_path=../lambda_function.zip"
terraform apply -var="lambda_zip_path=../lambda_function.zip"
```


## Testing the Solution

### Using the Test Resources Workflow

1. **Trigger the test workflow**:
    - Go to the Actions tab in your repository
    - Select the "Deploy Test Resources" workflow
    - Click "Run workflow"
    - Configure options:
        - Choose whether to automatically destroy resources after testing
        - Set how long to wait before destroying resources
    - Click "Run workflow" again
2. **Observe alerts**:
    - Check the SNS topic subscription (email) for alerts
    - You should receive notifications for:
        - IAM user creation
        - Access key creation
        - S3 bucket policy changes
        - Security group changes with public access
3. **Cleanup**:
    - Resources will be automatically destroyed if you selected that option
    - Otherwise, run the workflow again with the destroy option enabled

### Manual Testing

You can also test the solution manually by:

1. Creating an IAM user through the AWS console
2. Creating an access key for a user
3. Creating an S3 bucket and modifying its policy
4. Creating or modifying a security group to allow public access

Each of these actions should trigger an alert through your configured SNS topic.

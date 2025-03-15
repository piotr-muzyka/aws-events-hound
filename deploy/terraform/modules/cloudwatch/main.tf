# CloudWatch Event Rule to detect security-relevant events
resource "aws_cloudwatch_event_rule" "security_events" {
  name        = var.cloudwatch_event_rule_name
  description = "Capture security-relevant events (IAM user/key creation, S3 policy changes, SG changes)"

  event_pattern = jsonencode({
    detail = {
      eventSource = [
        "iam.amazonaws.com",
        "s3.amazonaws.com",
        "ec2.amazonaws.com"
      ],
      eventName = [
        "CreateUser",
        "CreateAccessKey",
        "PutBucketPolicy",
        "DeleteBucketPolicy",
        "AuthorizeSecurityGroupIngress",
        "ModifySecurityGroupRules"
      ]
    }
  })
}

# CloudWatch Event Target to invoke Lambda
resource "aws_cloudwatch_event_target" "invoke_lambda" {
  rule      = aws_cloudwatch_event_rule.security_events.name
  target_id = "InvokeLambda"
  arn       = var.lambda_function_arn
}


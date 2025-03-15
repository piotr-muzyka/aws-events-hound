# CloudWatch Event Rule to detect IAM user creation
resource "aws_cloudwatch_event_rule" "iam_user_creation" {
  name        = var.cloudwatch_event_rule_name
  description = "Capture IAM user creation events"

  event_pattern = jsonencode({
    detail = {
      eventSource = ["iam.amazonaws.com"],
      eventName   = ["CreateUser"]
    }
  })
}

# CloudWatch Event Target to invoke Lambda
resource "aws_cloudwatch_event_target" "invoke_lambda" {
  rule      = aws_cloudwatch_event_rule.iam_user_creation.name
  target_id = "InvokeLambda"
  arn       = var.lambda_function_arn
}

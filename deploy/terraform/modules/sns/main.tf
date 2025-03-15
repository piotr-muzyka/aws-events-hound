# SNS Topic for IAM user creation alerts
resource "aws_sns_topic" "iam_user_creation_alerts" {
  name = var.sns_topic_name
}

# SNS Topic Subscription (Email)
resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.iam_user_creation_alerts.arn
  protocol  = "email"
  endpoint  = var.sns_subscription_email
}

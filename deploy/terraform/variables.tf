variable "aws_region" {
  description = "The AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "iam-user-creation-monitor"
}

variable "sns_topic_name" {
  description = "Name of the SNS topic"
  type        = string
  default     = "iam-user-creation-alerts"
}

variable "sns_subscription_email" {
  description = "Email address to subscribe to the SNS topic"
  type        = string
}

variable "lambda_zip_file" {
  description = "Path to the Lambda function zip file"
  type        = string
  default     = "files/lambda_function.zip"
}

variable "cloudwatch_event_rule_name" {
  description = "Name of the CloudWatch Event Rule"
  type        = string
  default     = "iam-user-creation-rule"
}

variable "cloudtrail_name" {
  description = "Name of the CloudTrail"
  type        = string
  default     = "iam-events-trail"
}

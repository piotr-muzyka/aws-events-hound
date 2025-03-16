variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}

variable "lambda_zip_file" {
  description = "Path to the Lambda function zip file"
  type        = string
}

variable "lambda_role_arn" {
  description = "ARN of the IAM role for Lambda execution"
  type        = string
}

variable "sns_topic_arn" {
  description = "ARN of the SNS topic"
  type        = string
}

variable "cloudwatch_event_arn" {
  description = "ARN of the CloudWatch Event Rule"
  type        = string
}

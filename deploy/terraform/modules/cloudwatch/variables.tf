variable "cloudwatch_event_rule_name" {
  description = "Name of the CloudWatch Event Rule"
  type        = string
}

variable "lambda_function_arn" {
  description = "ARN of the Lambda function"
  type        = string
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
}

variable "cloudwatch_lambda_role_name" {
  description = "Name of the IAM role for CloudWatch to invoke Lambda"
  type        = string
  default     = "cloudwatch-lambda-role"
}

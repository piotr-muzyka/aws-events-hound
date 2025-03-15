

output "sns_topic_arn" {
  description = "The ARN of the SNS topic"
  value       = module.sns.sns_topic_arn
}

output "cloudtrail_arn" {
  description = "The ARN of the CloudTrail"
  value       = module.cloudtrail.cloudtrail_arn
}

output "cloudwatch_event_rule_arn" {
  description = "The ARN of the CloudWatch Event Rule"
  value       = module.cloudwatch.cloudwatch_event_rule_arn
}

output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = module.lambda.lambda_function_arn
}

output "lambda_role_arn" {
  description = "The ARN of the Lambda execution role"
  value       = module.iam.lambda_role_arn
}
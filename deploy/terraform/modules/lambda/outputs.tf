output "lambda_function_arn" {
  description = "The ARN of the Lambda function"
  value       = aws_lambda_function.iam_user_creation_monitor.arn
}

output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.iam_user_creation_monitor.function_name
}

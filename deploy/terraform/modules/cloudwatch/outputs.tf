output "cloudwatch_event_rule_arn" {
  description = "The ARN of the CloudWatch Event Rule"
  value       = aws_cloudwatch_event_rule.security_events.arn
}

output "cloudwatch_event_rule_name" {
  description = "The name of the CloudWatch Event Rule"
  value       = aws_cloudwatch_event_rule.security_events.name
}

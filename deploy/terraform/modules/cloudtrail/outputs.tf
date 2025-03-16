output "cloudtrail_arn" {
  description = "The ARN of the CloudTrail"
  value       = aws_cloudtrail.iam_events_trail.arn
}

output "cloudtrail_s3_bucket_name" {
  description = "The name of the S3 bucket for CloudTrail logs"
  value       = aws_s3_bucket.cloudtrail_bucket.id
}

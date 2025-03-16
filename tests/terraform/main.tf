data "aws_caller_identity" "current" {}

resource "aws_iam_user" "test_user" {
  name = "aws-hound-alert-test-user"
  path = "/"
}

resource "aws_iam_access_key" "test_user_key" {
  user = aws_iam_user.test_user.name
}

resource "aws_s3_bucket" "bucket_for_testing" {
  bucket = "hound-test-bucket-2${data.aws_caller_identity.current.account_id}"
  force_destroy = true
}

resource "aws_s3_bucket_policy" "test_bucket_policy" {
  bucket = aws_s3_bucket.bucket_for_testing.id
  
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "DenyGetObject"
        Effect    = "Deny"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.bucket_for_testing.arn}/*"
      }
    ]
  })

  depends_on = [aws_s3_bucket.bucket_for_testing]
}

# # Create a security group to test security group rule changes
# resource "aws_vpc" "test_vpc" {
#   cidr_block = "10.0.0.0/16"
  
#   tags = {
#     Name = "security-monitor-test-vpc"
#     Purpose = "Testing security monitoring solution"
#     Temporary = "true"
#   }
# }

# resource "aws_security_group" "test_sg" {
#   name        = "security-monitor-test-sg"
#   description = "Test security group for security monitoring"
#   vpc_id      = aws_vpc.test_vpc.id
  
#   tags = {
#     Purpose = "Testing security monitoring solution"
#     Temporary = "true"
#   }
# }

# resource "aws_security_group_rule" "test_public_access" {
#   type              = "ingress"
#   from_port         = 443
#   to_port           = 443
#   protocol          = "tcp"
#   cidr_blocks       = ["203.0.113.0/24"]
#   security_group_id = aws_security_group.test_sg.id
#   description       = "Allow HTTPS from a specific public range for testing"
# }
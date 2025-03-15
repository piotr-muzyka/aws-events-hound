# Get current account ID
data "aws_caller_identity" "current" {}

# SNS Module
module "sns" {
  source = "./modules/sns"

  sns_topic_name        = var.sns_topic_name
  sns_subscription_email = var.sns_subscription_email
}

# IAM Module
module "iam" {
  source = "./modules/iam"

  lambda_function_name = var.lambda_function_name
  sns_topic_arn        = module.sns.sns_topic_arn
}

# CloudTrail Module
module "cloudtrail" {
  source = "./modules/cloudtrail"

  cloudtrail_name = var.cloudtrail_name
  account_id      = data.aws_caller_identity.current.account_id
}

# # Lambda Module
module "lambda" {
  source = "./modules/lambda"

  lambda_function_name = var.lambda_function_name
  lambda_zip_file      = var.lambda_zip_file
  lambda_role_arn      = module.iam.lambda_role_arn
  sns_topic_arn        = module.sns.sns_topic_arn
  cloudwatch_event_arn = module.cloudwatch.cloudwatch_event_rule_arn
}

# CloudWatch Module
module "cloudwatch" {
  source = "./modules/cloudwatch"

  cloudwatch_event_rule_name = var.cloudwatch_event_rule_name
  lambda_function_arn        = module.lambda.lambda_function_arn
  lambda_function_name       = var.lambda_function_name
}

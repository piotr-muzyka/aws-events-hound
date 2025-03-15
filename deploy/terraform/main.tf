data "aws_caller_identity" "current" {}

module "sns" {
  source = "./modules/sns"

  sns_topic_name         = var.sns_topic_name
  sns_subscription_email = var.sns_subscription_email
}

module "iam" {
  source = "./modules/iam"

  lambda_function_name = var.lambda_function_name
  sns_topic_arn        = module.sns.sns_topic_arn
}

module "cloudtrail" {
  source = "./modules/cloudtrail"

  cloudtrail_name = var.cloudtrail_name
  account_id      = data.aws_caller_identity.current.account_id
}

module "lambda" {
  source = "./modules/lambda"

  lambda_function_name = var.lambda_function_name
  lambda_zip_file      = var.lambda_zip_file
  lambda_role_arn      = module.iam.lambda_role_arn
  sns_topic_arn        = module.sns.sns_topic_arn
  cloudwatch_event_arn = module.cloudwatch.cloudwatch_event_rule_arn
}

module "cloudwatch" {
  source = "./modules/cloudwatch"

  lambda_function_arn    = module.lambda.lambda_function_arn
  lambda_function_name   = var.lambda_function_name
  cloudwatch_event_rule_name = var.cloudwatch_event_rule_name
}

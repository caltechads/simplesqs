# The aws terraform provider
# ----------------------------
provider "aws" {
  region = "us-west-2"
}

# --------------------------------------------------------------------
# Caltech Contact Tracing statefile (for this Terraform stack)
# --------------------------------------------------------------------

terraform {
  backend "s3" {
    bucket = "caltech-terraform-remotestate-file"
    key     = "simplesqs-state"
    region  = "us-west-2"
  }
}


# ------------
# Reference
# ------------

module "reference" {
  source = "s3::https://s3-us-west-2.amazonaws.com/imss-code-drop/terraform-caltech-commons/terraform-caltech-commons-0.21.21.zip//modules/reference"
}

# Pipeline
# ------------------------------------

module "build-pipeline" {
  source = "s3::https://s3-us-west-2.amazonaws.com/imss-code-drop/terraform-caltech-commons/terraform-caltech-commons-0.21.21.zip//modules/codepipeline/recipes/bitbucket-archive-python"
  pipeline-name = "simplesqs"
  artifact-bucket-arn = "arn:aws:s3:::codepipeline-artifact-store"
  code-drop-bucket-arn = "arn:aws:s3:::imss-code-drop"
  codestar-connection-name = "bitbucket-imss-ads"
  slack-channel = "#ads_deploys"
  repository = "caltech-imss-ads/simplesqs"
  branch = "build"
  project = "simplesqs"
  environment = "prod"
  client = "IMSS"
  group = "ADS"
  contact = "imss-ads-staff@caltech.edu"
}


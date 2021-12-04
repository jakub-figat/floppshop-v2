variable "aws_region" {
  description = "AWS region"
  default     = "eu-central-1"
}

variable "az_count" {
  description = "Number of AZs to cover in region"
  default     = "2"
}
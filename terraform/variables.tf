variable "aws_region" {
  description = "AWS region"
  default     = "eu-central-1"
}

variable "az_count" {
  description = "Number of AZs to cover in region"
  default     = "2"
}

variable "app_port" {
  description = "Application port"
  default     = "8000"
}

variable "health_path" {
  description = "Endpoint for target group health checks"
  default     = "/health"
}
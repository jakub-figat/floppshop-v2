variable "aws_region" {
  description = "AWS region"
  default     = "eu-central-1"
}

variable "az_count" {
  description = "Number of AZs to cover in region"
  default     = "2"
}

variable "gateway_port" {
  description = "Application port"
  default     = "8000"
}

variable "health_path" {
  description = "Endpoint for target group health checks"
  default     = "/health"
}

variable "gateway_image" {
  description = "Dockerhub image"
  default     = "ansup17174/floppshop-v2-gateway:1.0.0"
}

variable "fargate_cpu" {
  description = "Fargate instance CPU units"
  default     = "1024"
}

variable "fargate_memory" {
  description = "Fargate instance RAM"
  default     = "2048"
}

variable "app_count" {
  description = "Number of ECS Service running tasks"
  default     = 3
}
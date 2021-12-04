resource "aws_ecs_cluster" "main" {
  name = "ecs-cluster"
}

data "template_file" "gateway" {
  template = file("./templates/ecs/gateway.json.tpl")

  vars = {
    gateway_image  = var.gateway_image
    gateway_port   = var.gateway_port
    fargate_cpu    = var.fargate_cpu
    fargate_memory = var.fargate_memory
    aws_region     = var.aws_region
  }
}

resource "aws_ecs_task_definition" "gateway" {
  family                   = "gateway-task"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  container_definitions    = data.template_file.gateway.rendered
}

resource "aws_ecs_service" "main" {
  name            = "main-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.gateway.arn
  desired_count   = var.app_count
  launch_type     = "FARGATE"

  network_configuration {
    security_groups  = [aws_security_group.ecs-cluster.id]
    subnets          = aws_subnet.private.*.id
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_alb_target_group.app.id
    container_name   = "gateway"
    container_port   = var.gateway_port
  }

  depends_on = [aws_alb_listener.app, aws_iam_role_policy_attachment.ecs_task_execution_role]
}
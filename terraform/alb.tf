resource "aws_alb" "main" {
  name            = "main-load-balancer"
  subnets         = aws_subnet.public.*.id
  security_groups = [aws_security_group.elb.id]
}

resource "aws_alb_target_group" "app" {
  name        = "app-target-group"
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"

  health_check {
    healthy_threshold   = 3
    interval            = "30"
    protocol            = "HTTP"
    matcher             = "200"
    timeout             = "3"
    path                = var.health_path
    unhealthy_threshold = "2"
  }
}

resource "aws_alb_listener" "app" {
  load_balancer_arn = aws_alb.main.id
  port              = var.app_port
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.app.id
  }
}
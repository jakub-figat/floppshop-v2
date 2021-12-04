[
  {
    "name": "gateway",
    "image": "${gateway_image}",
    "cpu": ${fargate_cpu},
    "memory": ${fargate_memory},
    "networkMode": "awsvpc",
    "portMappings": [
      {
        "containerPort": ${gateway_port},
        "hostPort": ${gateway_port}
      }
    ]
  }
]
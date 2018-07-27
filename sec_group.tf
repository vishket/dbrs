# export AWS_ACCESS_KEY_ID="anaccesskey"
# export AWS_SECRET_ACCESS_KEY="asecretkey"
# export AWS_DEFAULT_REGION="us-west-2"

# Create a security group to allow traffic on port 8888

resource "aws_security_group" "Jupyter NB" {
  name        = "Jupyter NB"
  description = "Allow inbound traffic on port 8888"

  ingress {
    from_port   = 8888
    to_port     = 8888
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

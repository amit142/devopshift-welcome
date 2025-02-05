data "aws_ami" "latest_amazon_linux" {
  most_recent = true  # Get the latest AMI

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]  # Amazon Linux 2
  }

  filter {
    name   = "owner-id"
    values = ["137112412989"]  # Amazon's official AWS account ID
  }
}

output "ami_id" {
  value = data.aws_ami.latest_amazon_linux.id
}
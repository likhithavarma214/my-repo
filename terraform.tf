resource "aws_s3_bucket" "bad" {
  bucket = "public-bucket"

  acl = "public-read"
}

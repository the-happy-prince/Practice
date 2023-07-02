variable "age" {
  type = number
}

variable "name" {
  type = string
}

output "printval" {
  value = "Hello, ${var.name}, your age is ${var.age}"
}
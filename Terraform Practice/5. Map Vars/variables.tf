variable "usersage" {
    type = map
    default = {
        prince  = "22"
        king = "125"
    }
}

variable "username" {
    type = string
}

output "userage" {
    value = "I am ${var.username} and my age is ${lookup(var.usersage, var.username)}"
}
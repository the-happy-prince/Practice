output "joinall" {
    value = "${join(",",var.users)}"
}

output "uppercase" {
    value = "${upper(var.users[0])}"
}
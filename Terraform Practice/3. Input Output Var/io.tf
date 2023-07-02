variable username {} 
output "printvar" {
  value = var.username 
}
output "printvar2" {
  value = "Hello, ${var.username}" 
}
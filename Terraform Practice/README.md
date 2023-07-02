# Ansible vs Terraform

### Terraform
- Terraform has been designed according to infrastructure
- Use terraform to create vm, establish connection between vms, keeping dbs private, etc.

### Ansible
- Ansible has been designed for automating the configurations
- Use ansible for perform jobs within those vms

# Best Practice to Run a Terraform
Create a directory for each `.tf` file and `cd` into the directory and run
```
terraform plan
```
#### Note:- When we destructure the file, we can define the variables in one file and use them in another.

# Running multiple output blocks
- The files will be loaded in an alphabetical order

# User Input
We can take user's input to create an instance that user wants such as an instance of fedora, ubuntu, etc.

To take the input in non-interactive mode, we can use the following command
```
terraform plan --var "username=Prince"
```
We can also use `default` keyword to define default variable in case we don't pass an args. Similarly, using `type` keyword, we can declare the variable type.

# TFVARs
What if we have 20 to 30 variables or more? It will be difficult to enter the value either by interactive mode or non-interactive mode. So, in this case we always need a file named `terraform.tfvars`, where we will define all ours variables.

`Terraform plan` will automatically read variables from this file, but if you have another tfvars file such as `prod.tfvars` then your terraform plan will work with command - `terraform plan -var-file=prod.tfvars`

# Reading variables from environment
Terraform will read the environment variables only if it is written like this:
`export TF_VAR_YOURVAR=value`

# Create Providers
For creating a provider visit https://registry.terraform.io/

# Destroy Providers
When we create a provider, terraform creates a `.tfstate` file in the directory. This file contains a custom JSON format that records a mapping from the Terraform resources in your configuration files to the representation of those resources in the real world.

You can distory the provider by running `terraform distory`.

# Validate
The `terraform validate` command validates the configuration files in a directory, referring only to the configuration and not accessing any remote services such as remote state, provider APIs, etc.

# Refresh
The `terraform refresh` command reads the current settings from all managed remote objects and updates the Terraform state to match.

# Console
The `terraform console` command provides an interactive console for evaluating expressions.

# Format
The terraform fmt command is used to rewrite Terraform configuration files to a canonical format and style. This command applies a subset of the Terraform language style conventions, along with other minor adjustments for readability.

# Dynamic Block
You can dynamically construct repeatable nested blocks like setting using a special dynamic block type, which is supported inside resource, data, provider, and provisioner blocks.

View More - https://developer.hashicorp.com/terraform/language/expressions/dynamic-blocks

# Taint
The `terraform taint` command informs Terraform that a particular object has become degraded or damaged. Terraform represents this by marking the object as "tainted" in the Terraform state, and Terraform will propose to replace it in the next plan you create.

Terraform does not recommend this commmand.

# Writing EOF
Here indentation should begn from the starting of the line.
```
template {
  data = <<EOH
LOG_LEVEL="{{key "service/geo-api/log-verbosity"}}"
EOH
}
```

Here indentation should begin from any point
```
template {
  data = <<-EOH
        LOG_LEVEL="{{key "service/geo-api/log-verbosity"}}"
EOH
}
```
You can also add file using `file("${path.module}/yourfile.sh")`

# Provisioners
Terraform provisioners are used for Passing data into virtual machines and other compute resources.

View More - https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax

# Datasource
Data sources allow Terraform to use information defined outside of Terraform, defined by another separate Terraform configuration, or modified by functions.

View More - https://developer.hashicorp.com/terraform/language/data-sources

# Graph
The `terraform graph` command is used to generate a visual representation of either a configuration or execution plan.


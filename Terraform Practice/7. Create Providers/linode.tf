terraform {
  required_providers {
    linode = {
      source = "linode/linode"
      version = "2.5.0"
    }
  }
}


provider "linode" {
  # Configuration options
  token = "e6d77c0ae6f950e6e5adfd7c85d1154f360cf0124d19dd3612c9db7fbf9872d5"
}

resource "linode_instance" "atc_deploy_server" {
    label = "atc_deploy_server"
    image = "linode/ubuntu22.04"
    region = "ap-west"
    type = "g6-nanode-1"
    root_pass = "terr4form-test"
    private_ip = true
}
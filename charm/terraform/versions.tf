# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

terraform {
  required_version = "~> 1.12"
  required_providers {
    juju = {
      source  = "juju/juju"
      version = "~> 1.0"
    }
  }
}

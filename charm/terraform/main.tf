# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

resource "juju_application" "__CHARM_NAME__" {
  name       = var.app_name
  model_uuid = var.model_uuid

  charm {
    name     = "__CHARM_NAME__"
    channel  = var.channel
    revision = var.revision
    base     = var.base
  }

  config             = var.config
  constraints        = var.constraints
  units              = var.units
  storage_directives = var.storage
}

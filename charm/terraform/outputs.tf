# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

output "__CHARM_NAME__" {
  description = "Name of the deployed application."
  value       = juju_application.__CHARM_NAME__.name
}

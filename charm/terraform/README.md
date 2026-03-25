<!-- Remember to update this file for your charm -- replace __CHARM_NAME__ and __REPO_PATH__ with the appropriate text. -->

# __CHARM_NAME__ Terraform module

This folder contains a base [Terraform][Terraform] module for the __CHARM_NAME__ charm.

The module uses the [Terraform Juju provider][Terraform Juju provider] to model the charm deployment onto any Kubernetes
environment managed by [Juju][Juju].

## Module structure

- **main.tf** - Defines the Juju application to be deployed.
- **variables.tf** - Allows customization of the deployment. Also models the charm configuration, except for exposing
  the deployment options (Juju model name, channel or application name).
- **output.tf** - Integrates the module with other Terraform modules, primarily by defining potential integration
  endpoints (charm integrations), but also by exposing the Juju application name.
- **versions.tf** - Defines the Terraform provider version.

## Using __CHARM_NAME__ base module in higher level modules

If you want to use `__CHARM_NAME__` base module as part of your Terraform module, import it like shown below:

```text
data "juju_model" "my_model" {
  name = var.model
}

module "__CHARM_NAME__" {
  source = "git::https://github.com/__REPO_PATH__//terraform"

  model = juju_model.my_model.name
  # (Customize configuration variables here if needed)
}
```

The complete list of available integrations can be found [in the Integrations tab][__CHARM_NAME__-integrations].

[Juju]: https://juju.is
[Terraform]: https://developer.hashicorp.com/terraform
[Terraform Juju provider]: https://registry.terraform.io/providers/juju/juju/latest
[__CHARM_NAME__-integrations]: https://charmhub.io/__CHARM_NAME__/integrations

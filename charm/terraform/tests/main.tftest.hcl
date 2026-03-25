# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

run "setup_tests" {
  module {
    source = "./tests/setup"
  }
}

run "basic_deploy" {
  variables {
    model_uuid = run.setup_tests.model_uuid
    channel    = "latest/edge"
    # renovate: depName="__CHARM_NAME__"
    revision = __CHARM_REVISION__
  }

  assert {
    condition     = output.app_name == "__CHARM_NAME__"
    error_message = "__CHARM_NAME__ app_name did not match expected"
  }
}

run "integration_test" {
  variables {
    model_uuid = run.setup_tests.model_uuid
  }

  module {
    source = "./tests/integration_test"
  }

  assert {
    condition     = data.external.app_status.result.status == "blocked"
    error_message = "__CHARM_NAME__ app_name did not match expected"
  }
}

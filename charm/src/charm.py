#!/usr/bin/env python3

# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

# Learn more at: https://documentation.ubuntu.com/juju/3.6/howto/manage-charms/#build-a-charm

"""__CHARM_TITLE__ charm."""

import logging
import typing

import ops

from state import CharmBaseWithState, CharmState

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)


class Charm(CharmBaseWithState):
    """Charm implementing holistic reconciliation pattern.

    The holistic pattern centralizes all state reconciliation logic into a single
    reconcile method that is called from all event handlers. This ensures consistency
    and reduces code duplication.
    See https://documentation.ubuntu.com/ops/latest/explanation/holistic-vs-delta-charms/
    for more information.
    """

    def __init__(self, *args: typing.Any):
        """Construct.

        Args:
            args: Arguments passed to the CharmBase parent constructor.
        """
        super().__init__(*args)

        self._state: CharmState | None = None

        self.framework.observe(self.on.install, self._on_install)
        self.framework.observe(self.on.config_changed, self.reconcile)

    def _on_install(self, _: ops.InstallEvent) -> None:
        """Handle install event."""
        # Handle any installation logic here, such as installing packages or setting up files.
        pass

    @property
    def state(self) -> CharmState:
        """Return the charm state, initializing it if necessary."""
        if self._state is None:
            self._state = CharmState.from_charm(self)
        return self._state

    def reconcile(self, _: ops.EventBase) -> None:
        """Holistic reconciliation method.

        This method contains all the logic needed to reconcile the charm state.
        It is idempotent and can be called from any event handler.
        """
        # TODO: implement charm reconciliation logic here This is where you would read the state,
        # configure the application, write data to relations, etc. And set the unit status
        # accordingly.
        self.unit.status = ops.ActiveStatus()


if __name__ == "__main__":  # pragma: nocover
    ops.main(Charm)

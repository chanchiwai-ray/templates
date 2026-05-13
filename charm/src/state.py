# Copyright 2026 __AUTHOR_NAME__
# See LICENSE file for licensing details.

"""Charm state: single source of truth for all adaptor data."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod

import ops
from pydantic import BaseModel, ConfigDict

logger = logging.getLogger(__name__)


class CharmState(BaseModel):
    """Single source of truth for all charm data."""

    model_config = ConfigDict(frozen=True)

    @classmethod
    def from_charm(
        cls,
        charm: ops.CharmBase,
    ) -> CharmState:
        """Build a CharmState from the charm instance.

        Loads charm configuration and aggregates relation data into a single
        state object. Accepts the handler rather than instantiating it here.

        Args:
            charm (ops.CharmBase): The charm instance, used to load configuration.

        Returns:
            CharmState: A CharmState with all necessary data.
        """
        # Load charm configuration using the CharmConfig class.
        # charm_config = CharmConfig.from_charm(charm)
        return cls()


class CharmBaseWithState(ops.CharmBase, ABC):
    """CharmBase that can build a CharmState."""

    @property
    @abstractmethod
    def state(self) -> CharmState | None:
        """The charm state."""

    @abstractmethod
    def reconcile(self, _: ops.HookEvent | None = None) -> None:
        """Reconcile configuration."""

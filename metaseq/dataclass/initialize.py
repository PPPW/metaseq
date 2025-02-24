# Copyright (c) Meta Platforms, Inc. and affiliates. All Rights Reserved.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""isort:skip_file"""

from dataclasses import _MISSING_TYPE
import logging

from hydra.core.config_store import ConfigStore

from metaseq.dataclass.configs import MetaseqConfig

logger = logging.getLogger(__name__)


def hydra_init(cfg_name="base_config") -> None:
    cs = ConfigStore.instance()
    cs.store(name=cfg_name, node=MetaseqConfig)

    for k in MetaseqConfig.__dataclass_fields__:
        f = MetaseqConfig.__dataclass_fields__[k]
        if not isinstance(f.default_factory, _MISSING_TYPE):
            v = f.default_factory()
        else:
            v = f.default
        try:
            cs.store(name=k, node=v)
        except BaseException:
            logger.error(f"{k} - {v}")
            raise

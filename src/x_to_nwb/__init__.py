"""
This package allows to create NeuroDataWithoutBorders v2 files from ABF and DAT files.

The main entry points are convert_cli for console scripts and convert for programmatic use.

"""

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .conversion import convert_cli, convert

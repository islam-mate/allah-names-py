"""
allah-names: 99 Names of Allah with meanings, transliterations, and search.
"""

__version__ = "1.0.0"

from .core import (
    AllahName,
    get_all_names,
    get_by_number,
    get_random_name,
    search_names,
)

__all__ = [
    "AllahName",
    "get_all_names",
    "get_by_number",
    "get_random_name",
    "search_names",
]

"""path"""

import os
import fsspec


def make_path_absolute(path: str) -> str:
    fs, p = fsspec.core.url_to_fs(path, use_listings_cache=False)
    if fs.protocol == "file":
        return os.path.abspath(p)
    return path

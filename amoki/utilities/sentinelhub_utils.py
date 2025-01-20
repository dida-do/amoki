"""
SentinelHub related utilities used by some of the notebooks
"""

from __future__ import annotations

from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def plot_image(
    image: np.ndarray,
    factor: float = 1.0,
    clip_range: tuple[float, float] | None = None,
    figsize: tuple[int, int] = (15, 15),
    **kwargs: Any,
) -> None:
    """Utility function for plotting RGB images."""
    _, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    if clip_range is not None:
        ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])


def get_volume_from_dem_array(dem_img: np.array, resolution: int = 10):
    """Returns the below-sea-level volume (in cubic kilometers) of a 2d DEM array."""
    # The minimum and maximum elevations of the image are useful
    min_elevation = dem_img.min()
    max_elevation = dem_img.max()

    # We clip the image to be only those pixels which are below sea level
    clipped_img = np.clip(dem_img, min_elevation, 0)

    # The volume is the integral of the non-zero pixels. This is just the sum, but the units are weird.
    # The units of the unnormalised volume are (10m)x(10m)x(1m), since the height is given in meters
    # and the resolution of the image is 10m, so each pixel represents a square of 10m x 10m.
    unnormalised_volume = np.abs(np.sum(clipped_img))

    # To normalise the volume, we multiply by the resolution sqaured so that the units are in cubic meters, then divide by 1000**3
    normalised_volume = (unnormalised_volume * (resolution**2)) / (1000**3)
    return normalised_volume


def get_cloud_coverage(cloud_mask: np.array):
    """Computes the percentage of cloud cover from a cloud mask"""

    return cloud_mask.sum() / (cloud_mask.shape[0] * cloud_mask.shape[1])

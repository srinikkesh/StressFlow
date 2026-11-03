# File:     uniformLatticeGenerator.py

# Author:   Srinikkesh Senthilkumar
# Date:     November 2, 2026
# License:  MIT License (see LICENSE in root directory)
# Copyright (c) 2026 Srinikkesh Senthilkumar

# Summary of File:

#   This file generates a uniform TPMS lattice

import numpy as np
from skimage.measure import marching_cubes
import trimesh

def generate_TPMS_lattice(bounds=(0,0,0,(2 * np.pi),(2 * np.pi),(2 * np.pi)), resolution=60, t=0.0, size=25.0, spatial_thickness=False):
    """
    Generates a TPMS lattice mesh and returns a trimesh object

    Args:
        bounds (tuple): (x_min, y_min, z_min, x_max, y_max, z_max)

    """
    print(f"Generating lattice at {resolution}^3 resolution")

    # Spatial grid mapping
    x = np.linspace(bounds[0], bounds[3], resolution)
    y = np.linspace(bounds[1], bounds[4], resolution)
    z = np.linspace(bounds[2], bounds[5], resolution)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    # Spatial thickness field function
    if spatial_thickness:
        R = np.sqrt(np.pow(X, 2) + np.pow(Y, 2) + np.pow(Z, 2))
        t = 1 - (0.1 * R)

    # Gyroid Implicit Equation cos(x)sin(y) + cos(y)sin(z) + cos(z)sin(x) - t
    field = np.cos(X)*np.sin(Y) + np.cos(Y)*np.sin(Z) + np.cos(Z)*np.sin(X) - t

    # Extract sufaces
    verts, faces, normals, values = marching_cubes(field, level=0.0)

    # Scale to physical dimensions (mm)
    verts = verts / resolution * size

    mesh = trimesh.Trimesh(vertices=verts, faces=faces, normals=normals)

    return mesh


if __name__ == "__main__":
    mesh = generate_TPMS_lattice(resolution=60, t=0.0, size=30.0)
    #mesh.export("data/uniform_gyroid_test.stl")
    print("Generated gyroid")
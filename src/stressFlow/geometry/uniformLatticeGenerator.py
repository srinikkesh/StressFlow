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

def generate_uniform_gyroid(resolution=60, t=0.0, size=25.0):
    """
    Generates a uniform Gyroid TPMS lattice mesh and returns a trimesh object
    """
    print("Generating Gyroid field at {resolution}^3 resolution")

    # Spatial grid mapping
    x = np.linspace(0, 2 * np.pi, resolution)
    y = np.linspace(0, 2 * np.pi, resolution)
    z = np.linspace(0, 2 * np.pi, resolution)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    # Gyroid Implicit Equation cos(x)sin(y) + cos(y)sin(z) + cos(z)sin(x) - t
    field = np.cos(X)*np.sin(Y) + np.cos(Y)*np.sin(Z) + np.cos(Z)*np.sin(X) - t

    # Extract sufaces
    verts, faces, normals, values = marching_cubes(field, level=0.0)

    # Scale to physical dimensions (mm)
    verts = verts / resolution * size

    mesh = trimesh.Trimesh(vertices=verts, faces=faces, normals=normals)

    return mesh

if __name__ == "__main__":
    mesh = generate_uniform_gyroid(resolution=60, t=0.0, size=30.0)
    #mesh.export("data/uniform_gyroid_test.stl")
    print("Generated gyroid")
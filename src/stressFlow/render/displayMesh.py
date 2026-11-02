# File:     uniformLatticeGenerator.py

# Author:   Srinikkesh Senthilkumar
# Date:     November 2, 2026
# License:  MIT License (see LICENSE in root directory)
# Copyright (c) 2026 Srinikkesh Senthilkumar

# Summary of File:

#   This file renders any given mesh

import pyvista as pv
from stressFlow.geometry.uniformLatticeGenerator import generate_uniform_gyroid

mesh = generate_uniform_gyroid(resolution=60, t=0.0, size=30.0)

pv_mesh = pv.wrap(mesh)

plotter = pv.Plotter()
plotter.add_mesh(pv_mesh, color="lightblue", show_edges=True)
plotter.add_axes() # type: ignore
plotter.show()

print("Render Complete")
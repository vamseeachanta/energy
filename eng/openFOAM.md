## Introduction

## Summary

## Case Studies

### PHD THesis - Marielle de Oliveira

Hello everyone from my LinkedIn community, here I present more results from my Ph.D about the blade-resolved CFD simulations of the NREL 5-MW baseline wind turbine for offshore applications, that I have being developing at the Fluids & Dynamics Research Group - Poli-USP at the Escola Politécnica da USP of the Universidade de São Paulo (Mechanical Engineering Department) under the scholarship from FAPESP and the supervision of Dr. Bruno Carmo and collaboration of my colleague Rodolfo Curci Puraca.

This video shows a comparison between two different spatial discretization the Mesh-1 and the Mesh-2, both meshes were developed in the OpenCFD Limited (software OF v.1912), considering the AMI method.

In both cases the resolution of the mesh close to the blades surface are equal since both cases respect the y+ parameter for the same turbulence model employed which was the URANS k-Omega SST. The main difference between the meshes is the size of the finite volume cells which surround the wind turbine and the ones placed in the wake region.

At the left side of the video for both Mesh-1 and Mesh-2, the results are presented in terms of the isosurfaces of the Q-criterion (0.05), colored by the vorticity magnitude. It is possible to notice that considering element of 0.5 m size, more vortical structures along of the blade span was captured by the Mesh-1.

At the right side of the video for both Mesh-1 and Mesh-2 the results are presented in terms of the axial velocity contours. It is possible to notice some differences in the wake pattern contour, and also a different gradient pattern behind the wind turbine with is propagated for the wake region.

The results for both Mesh-1 and Mesh-2 in terms of generated thrust and power production can be seeing in the graphic shown in the video, where the CFD simulations results were benchmarked with the results obtained through the National Renewable Energy Laboratory (NREL) OpenFAST code, considering the same environmental conditions.

In addition, we also performed a comparison in terms of computational costs and distributed forces along the blades for different azimuth angles for both meshes and all the information regarding the numerical methods employed in the CFD simulations can be found through the preprint of our journal submission which is already available in my ResearchGate and even without correction yet, I hope it can be useful for you!

Here follows the link to access the publication, which can also be cited in the preprint stage:

<https://lnkd.in/g6RE8YcW>

Ps: Click on the DOI link of the publication (DOI: 10.2139/ssrn.3957822) to be directed to the download page!

### References

- View the entire Naval Hydrodynamics video
  - <https://www.youtube.com/watch?v=PDDRRz478fs>   Naval Hydrodynamics I
  - <https://www.youtube.com/watch?v=Nr7tMtII-DU>   Naval Hydrodynamics II
  - Naval Hydro Pack - How to install it?

- Courses
  - <https://ocw.mit.edu/courses/2-29-numerical-marine-hydrodynamics-13-024-spring-2003/>
  - <https://ocw.mit.edu/courses/2-22-design-principles-for-ocean-vehicles-13-42-spring-2005/pages/readings/>
  - Numerical Fluid Dynamics <https://ocw.mit.edu/courses/2-29-numerical-fluid-mechanics-spring-2015/pages/lecture-notes-and-references/>
  - <https://ocw.mit.edu/courses/2-24-ocean-wave-interaction-with-ships-and-offshore-energy-systems-13-022-spring-2002/>

References

<https://www.youtube.com/watch?v=EDAn2uFJ6jU>
FoamPython - How does it work. Is it OpenFOam under the hood

<https://gitlab.com/share-renderluh/foampython-1.0> (Link not working)

Fluid Structure Interactions
<https://www.youtube.com/watch?v=Lnu4muOXV0Q>

Using blender to visualize OpenFOAM outputs?
<https://www.youtube.com/watch?v=yp9khQtP1g8>

<https://www.youtube.com/@openfoamjournal6606>

<https://www.jores.net/>

[Getting Started](<https://www.openfoam.com/documentation/tutorial-guide/1-introduction/1.1-getting-started#x4-30001.1>)

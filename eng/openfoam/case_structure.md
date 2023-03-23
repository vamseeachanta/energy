
## Case Structure

### Directory Structure

- A sample directory layout for a solver that requires only pressure and velocity (e.g. an incompressible solver for laminar flow).
- Note the entries with a trailing / are directories, while those without are plain text files.
-

<code>

0/
...U
...p
constant/
...polyMesh/
...transportProperties
...turbulenceProperties
system/
...controlDict
...fvSchemes
...fvSolution

</code>

### Typical File

- A header is included in each OpenFOAM file

### 0 Directory

-The 0 directory is a special time directory that contains the following for the simulation:
    -  the initial condition(s) .
    - boundary conditions ?.

- Inside of this directory there will be one text file for each field that is required for the particular solver executable that is being run (e.g. U for velocity, p for pressure, etc.)
  - Each file contains four main sections, including the header section.
  - A header is included in each OpenFOAM file to give the parameters of the file, which can be checked by the solver prior to reading.
  - An example of the header section for the p file located in the 0 directory is below:
    - The first 7 lines are comments, which are included by convention, but are not strictly necessary. All OpenFOAM files can be commented using C++ syntax.
    - FoamFile{...} section contains several properties of the file that may be checked by the solver prior to reading the field.
    - The FoamFile section is followed by the field data, which is a list of values for each cell in the mesh.
    
    <code>
    /*--------------------------------*- C++ -*----------------------------------*\
  =========                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  6.x                                   |
|   \\  /    A nd           | Website:  <https://openfoam.org>                  |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      p_rgh;
}
//* ************************************ //

    </code>

A header is included in each OpenFOAM file to give the parameters of the file, which can be checked by the solver prior to reading. Here is an example of the header section for the p file located in the 0 directory:

### Dimensions and Units

Position  Dimension  SI Unit
1  Mass  Kilogram (kg)
2  Length  Metre (m)
3  Time  Second (s)
4  Temperature  Kelvin (K)
5  Quantity  Mole (mol)
6  Current  Ampere (A)
7  Luminous intensity  Candela (cd)

### References

<https://maplekeylabs.com/understanding-the-openfoam-case-structure/>

# Objective

To summarize the steps to run the case study

# Errors

**Entry 'Umean' not found in dictionary in U.boundaryField.outflow**

Entry 'Umean' not found in dictionary "/home/vamsee/openfoam_others/wigley_hull/wigleyHull_LTS/0/U.boundaryField.outflow"
openfoam Entry 'Umean' not found in dictionary in U.boundaryField.outflow

Solution:
Added the "Umean           1.452;" line to the outflow boundary condition in 0_org/U file. See the updated file snippet below.

<code>
    outflow
    {
        Umean           1.452;
        type            outletPhaseMeanVelocity;
        alpha           alpha.water;
        UnMean           $Umean;
        value           $internalField;
    }
</code>

### Downstream error due to Umean error above

**openfoam not creating 0 folders**

<https://www.cfd-online.com/Forums/openfoam-pre-processing/217890-redistributepar-does-not-create-0-folder-new-processor-folders.html>

**Summary**

openfoam not creating 0 folders

**Details**

cannot find file "/home/vamsee/openfoam_others/wigley_hull/wigleyHull_LTS/processor0/0/p_rgh"
cannot find file "/home/vamsee/openfoam_others/wigley_hull/wigleyHull_LTS/processor2/0/p_rgh"
cannot find file "/home/vamsee/openfoam_others/wigley_hull/wigleyHull_LTS/processor3/0/p_rgh"

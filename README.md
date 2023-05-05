# FuzzTree
# Copyright (C) 2023 THEO BOURY 

# FuzzTree Project

This project present FuzzTree, a new tool to solve the Subgraph Isomorphism Problem in its "Fuzzy" version, that allows to take into account and search for neighborhoods of the requested pattern.

## Scope of this folder

This folder contains all the elements to launch the FuzzTree tool in its minimalistic version described in (TODO lien arXiV?) by Boury et al, 2023. Specific benchmarks and frameworks including the cartography example and test on multiple graphs are available in the WABI 2023 folder. README in WABI 2023 is specifically design to indicate what all the possible tests are.
## Prerequisite and launch

### Dependencies 
The tool uses the following non-standard libraries:

* infrared (see https://hal.archives-ouvertes.fr/hal-03711828/document by Hua-Ting Yao et al, 2022 for more details.)
* pickle (for graph imports). (natively installed for python above 3.7 ?)
* networkx (for graph vizualizations).
* varnaapi (for graph vizualizations). 

### Files and repositories
The project is entirely available on the current archive. 

The different files are:
* FuzzTree.py: core of the tool, search for Subgraph Isomorphism with neighborhoods.
* VarnaDrawing.py: contains necessary wrappers to launch Varna on graphs and their mapping.
* Launcher.py, a file that allow to launch the tool from command lines.


### Get started

First, this project will require Anaconda (or at least Miniconda), make sure that conda is installed or you can have a look at https://conda.io/en/latest/miniconda.html for the installation

Make sure next that conda path is known with environement variable:
```bash
export PATHTOCONDA=Your_path_to_conda/conda
```

First init conda :

```bash
conda init fish
```

It is not a mandatory for our method, but in order to obtain some mapping visualisations, we used Varna from VARNA: Interactive drawing and editing of the RNA secondary structure, Darty et al, Bioinformatics, 2009 that can be installed at https://varna.lri.fr/index.php?lang=en&page=downloads&css=varna
Executable for Varna should be placed in the current folder.

When conda setup is done, to install the dependencies package you can next type :

```bash
make dependencies
```


You can now launch the test by using, it will launch the test with pattern graph 53kink_turninto3NVI.pickle and target graph 3NVI.nxpickle: 

```bash
make tests
```
or 
```bash
make tests_no_varna
```
Depending if Varna was installed or not.

If no mistake appears here, you are good to go.

#### Input and output format

Input and output should be respectively a .pickle file and a .nxpickle file that described the pattern and the target graphs.
We advise to have the nucleotides in the .pickle graph to be nmerote from 1 to |PATTERN| in order to have a clean mapping and drawing as output.

#### Output format

With usevarna flag to True, the output is the drawing of one mapping found on the target.
With usevarna flag to False, the output is the list of all mappings found for the pattern in the target graph.

#### Execution script

To launch the FuzzTree method on, you just have to launch:

```
python3 Launcher.py --pattern GPATTERN.pickle -- target GTARGET.nxpickle OPTIONS
```

If no options are specified default parameters are used.

## Option for Fuzziness and parameters

Parameters in OPTIONS can be modified to customize the searched neighborhoods and indicate the pattern and target that are taken as arguments in above command line.
Here are the different options that can be added, none of them different from the inputs ones are necessary and default parameters are used when not specified:

Inputs:
--pattern, default 20kink_turninto5TBW, the pattern from which launch computation.
--target, default 3NVI.nxpickle, the target graph on which to search for the pattern.

Neighborhood Thresholds and parameters:
--L, default 20, specifies the threshold on the sum of distances in isostericity between labels in the searched pattern and corresponding labels in the found pattern. 
--E, default 4, specifies the threshold on the number of interactions that we allow to be missing (number of edges missing).
--G, default 20, specifies the threshold on the sum of geometrical distances covered by gaps.
--Dgap, default 10, specifies the geometric distance at which we allow to look for potential gap.
--Dedge, default 5, specifies the geometric distance at which we allow to look for potential missing edges. 
--samples, default 1000, the number of samples that are drawn during FuzzTree method.

Others:
--procs, default 1, the number of processors on which we want to work, only serve for preprocessing here.
--near, default False, if we consider the near edges or not.
--usevarna, default False, if we want to use Varna or not for a single query.


## Limitations

* In FuzzTree method, the set_target was put at a mean value of threshold over two, which favors to find quickly graphs with a bit of ``fuzziness", if for others usages focus is put on the usage for no fuzziness or high fuzziness it can be relevant to change this value, which should be done manually in this release by editing the FuzzTree.py file.

## Contributors

* Théo Boury
* Vladimir Reinharz







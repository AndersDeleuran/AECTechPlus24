## Dynamically Drawing and Reacting to Things with GHPython

There is more to running GHPython components in SDK Mode than compiling plugins. We will demonstrate, explore, and combine these overlooked features that are enabled once you step out of procedural mode. This includes full access to the Rhino display pipeline, enabling custom 2D and 3D drawing features (e.g. double-sided materials and other methods not exposed in vanilla Grasshopper), drawing into/above screen space for developing legends and heads up displays, and subscribing to Rhino events for developing dynamic geometry pipelines and mouse interaction. Although still in flux, everything we learn should be directly applicable to the IronPython mode of the Rhino 8 script editor.

This repo is for sharing files with workshop participants at [AECTech+ Barcelona 2024](https://www.aectech.us/aectech-barcelona).

## Prerequisites 

If you are unfamiliar or rusty with GHPython I would suggest flipping through [this beginners course](https://andersholdendeleuran.com/211103_Grasshopper103_CPH_Redacted.pdf):

![GH103](https://raw.githubusercontent.com/AndersDeleuran/AECTechPlus24/main/GH103_Exercises/211103_Grasshopper103_CPH_Redacted.png)

And perhaps having a quick fiddle with [some of its exercise snippets](https://github.com/AndersDeleuran/AECTechPlus24/tree/main/GH103_Exercises):

![Exercise Snippets](https://raw.githubusercontent.com/AndersDeleuran/AECTechPlus24/main/GH103_Exercises/210911_ExerciseSnippets_00.png)

## Dynamically Drawing and Reacting to Things with GHPython

There is more to running GHPython components in SDK Mode than compiling plugins. We will demonstrate, explore, and combine these overlooked features that are enabled once you step out of procedural mode. This includes full access to the Rhino display pipeline, enabling custom 2D and 3D drawing features (e.g. double-sided materials and other methods not exposed in vanilla Grasshopper), drawing into/above screen space for developing legends and heads up displays, and subscribing to Rhino events for developing dynamic geometry pipelines and mouse interaction. Although still in flux, everything we learn should be directly applicable to the IronPython mode of the Rhino 8 script editor.

## Prerequisites 

If you are unfamiliar or rusty with GHPython, I would suggest flipping through [this 197 page PDF slideshow](https://andersholdendeleuran.com/211103_Grasshopper103_CPH_Redacted.pdf) ([mirror](https://www.dropbox.com/scl/fi/bjqkaemgevhrnz8u1x3sc/211103_Grasshopper103_CPH_Redacted.pdf?rlkey=udzmq3f3z010zegonyfviref9&dl=0)) and its accompanying [exercise snippets](https://github.com/AndersDeleuran/AECTechPlus24/tree/main/Exercises_GH103). I have been using these when teaching our in-house BIG Academy GHPython beginners course (note that it has been slightly redacted for confidentiality).

![GH103](https://raw.githubusercontent.com/AndersDeleuran/AECTechPlus24/main/Images/211103_Grasshopper103_CPH_Redacted.png)

![Exercise Snippets](https://raw.githubusercontent.com/AndersDeleuran/AECTechPlus24/main/Images/210911_ExerciseSnippets_00.png)


## Slideshow & Exercises

I have prepared [this 44 page PDF slideshow](https://andersholdendeleuran.com/240418_AECTech2024.pdf) ([mirror](https://www.dropbox.com/scl/fi/r44su9z6tnutyyppkz9z9/240418_AECTech2024.pdf?rlkey=3dl5qx1jq3q2yel4sof4oi1ic&dl=0)) and a collection of [new accompanying exercise files](https://github.com/AndersDeleuran/AECTechPlus24/tree/main/Exercises) for our AECtech+ workshop, here at the McNeel Europe headquarters in Barcelona. You can click the green `Code` above and select `Download Zip` if want to download all the exercises at once.

![GH104](https://raw.githubusercontent.com/AndersDeleuran/AECTechPlus24/main/Images/240419_AECTech2024.png)





Tools to make your life in editing bases easier. 

Borrowing heavily from: https://wiki.vega-strike.org/Development:Base_Backgrounds
Read it for a description of the python that goes into making a base.

The base images, or textures are easily edited by the GIMP. With it's DDS plugin
it's possible to save the textures directly in the right format.

The Base_Coordinate_Calculator.ods included in this directory removes some of the
pain in editing the python scripts that place the active regions on screen. 
The active regions are just see-through buttons with a glowy mouseover texture. 

In the GIMP, when you have the base image open, and re-scaled to 1024x1024, you
will see the pixel coordinates on the lower left of the UI.

Enter the LOWER Left coordinates of the area that you want clickable in the spread-
sheet. Then repeat with the upper RIGHT corner of the area. The sheet will now
calculate the numbers that you can cut and paste into your python script for the 
base.

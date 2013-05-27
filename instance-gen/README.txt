ccd2data.py

********* Please read all of this short document *********


REQUIRES: Python 2.6/2.7

This is a tool to generate XML instances for CCDs to be used for testing persistence and qurying capabilities.

Save the default-ccd2data.cfg file  as ccd2data.cfg and edit the desired limits:
records= the total number of patient records to simulate
mininstances= the minimum number of instances to generate for each CCD.
maxinstances= the maximum number of instances to generate for each CCD.

The tool will select a random number of instances between the minimum and maximum for each CCD in each patient record.

These simulate records can then be imported into an XML database or mapped to another database for testing.

The test CCDs have realistic values set in order to make various query scenarios work.
The CCDs are located on HKCR.net and are included in this package for reference.
They are identified in the generated instances with the namespace on HKCR.net.

ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517.xsd - Demographics
ccd-949a53a0-0bc3-43ce-b900-1ff0b9c6798c.xsd - Vital Signs
ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517.xsd - Basic Metabolic Panel (BMP)

*THERE ARE NOT TO BE USED IN REAL APPLICATIONS*  they are only for system design testing purposes.

After creating the ccd2data.cfg as instructed above, execute the application with:
$python ccd2data.py


----------------------------------------------------------------------------------------------------------------
Direct all questions to: http://www.mlhim.org/forums

Thank you,
Tim Cook




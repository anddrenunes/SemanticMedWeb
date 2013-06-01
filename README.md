SemanticMedWeb Demo
=======================

This is an example application built on top of eXist-DB. 
The data instances were created using the instance generator from HKCR.net
based on CCDs from the CCD-Gen generator. For question about the CCD-Gen contact @twcook
Initially, a few basic queries have been added (see the modules folder). 

SMW Installation
============
1.  Install eXist-db 2.0 per the instructions for your platform.
2.  Clone this repository.
3.  To copy the repository into eXist-db using the Python installer use steps 5 - 9. These are also required to use the example Python API calls.
4.  Or, use one of the methods described here: http://exist-db.org/exist/apps/doc/uploading-files.xml to import the 'smw' folder into /db/apps/ and the 'data' folder into /db/
5.  Install Python 2.7.x http://www.python.org/download/releases/
6.  Install virtualenv https://pypi.python.org/pypi/virtualenv 
7.  Make your SemanticMedWeb folder a virtual environment:$virtualenv --no-site-packages SemanticMedWeb
8.  Change to your SemanticMedWeb folder
9.  Activate the virtualenv: $source bin/activate
10. Execute the installer: python smw_install.py

 
--Tim Cook

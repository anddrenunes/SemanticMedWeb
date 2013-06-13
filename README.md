What is the SemanticMedWeb?
===========================
The SemanticMedWeb (SMW) is more of a concept than a specific implementation. 
The concept is based on integration of diverse applications via a mechanism to exchange both the syntactic as well as semantic contexts of any healthcare related concept.
From patient data to basic science and back again (bench to beside) semantic interoperability. 


SemanticMedWeb Demo 1.0
=======================

This is an example application built on top of eXist-DB. 
The data instances were created using the instance generator from HKCR.net
based on CCDs from the CCD-Gen generator. For question about the CCD-Gen contact @twcook on GitHub

The SemanticMedWeb, initially focused on patient clinical, demographic and admin data only.
As of June 1, 2013 we are collaborating with Translational Researchers to develop an approach to semantic integration with biomedical databases. This is a foundational problem in the Translational Medicine domain that this project based on Multi-Level Healthcare Inforamtion Modelling approaches can address with success.

Prerequisites
=============
eXist-db 2.0 or later.
Be sure to NOT use IcedTea6 JRE. IcedTea7 or the Oracle JREs are okay. You can check your Java with:
$ java -version



SMW Installation
================
1.  Install eXist-db 2.0 per the instructions for your platform.
2.  Clone this repository.
3.  The SemanticMedWeb Demo contains an eXist-db application that can be imported directly into the database using the eXist client.
    Import the smwdemo subdirectory into your db/apps collection. The latest code is in the 1.0 branch.
4.  To activate the indexes (for improved performance) you should import the collection.xconf file into:
    db/system/config/db/apps/smwdemo it will be the only file in that collection. Now reindex your database. You can use the Java client for this.


Instance Generator
==================
There is a Python script to create sample instances from your CCDs.  However, as of 12 June, 2013 it is no longer in sync with the SemanticMedWeb Demo.  It will be updated in the comming weeks. 


Concept Constraint Definitions (CCDs)
=====================================
CCDs are the concept data models used by the SemanticMedWeb and other MLHIM based implementations.
They can be created using an XML Schema editor, the Concept Definition Designer (see the MLHIM/Tools repository) 
or the CCD-Gen web based application. The CCD-Gen is a subscription based application. You can get more inforamtion about it by asking on the MLHIM Google Plus page: http://gplus.to/MLHIM

CCDs can also be downloaded from the public HEalthcare Knowledge Component Repository (HKCR) http://hkcr.net
Be sure to only use the lastest CCDs (MLHIM version 2.4.2).



v1.0a1 - Provides an HTML view of the CCD types and semantics with clickable links. Add any (2.4.2 or later) CCDs to the 'ccdlib' collection in the demo and select CCD->List All from the menu.  Each CCD title is a clickable link to the CCD View page. 


_more to come_
 
--Tim Cook

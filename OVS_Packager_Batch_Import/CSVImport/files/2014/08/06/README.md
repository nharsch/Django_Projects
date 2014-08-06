General_OPS_Scripts
===================

General Scripts for Operations

Programs currently included:

Add MetaXML Merlin IDs – Iterates through .xml files in the input folder, and adds Merlin Series and Episode ID subelements.

Comcast ADI Bulk Upload - Modifies Comcast .xml files to update version minor to 5, and saves a copy as output.

MiniMudMaker – For the processing and packaging of ADI-ONLY MDUs for Comcast. .xml files are parsed, basic QC is performed, version numbers are updated, and File Not Included strings are added if needed. There are alternate excecutables for adding categories, as well as performing Verb Deletes.

Schedule Compiler – This is used to create the compiled film metadata that the Metadata Writer takes its data from. Takes VCIS .xls output files as its input.

Streampix Metadata Writer – Opens a .xls metadata file, and can automate the input of the film metadata, some alpha & genre categories, and content providers.

Unified Meta Maker - This module iterates through the input folders and creates dummy .meta files for the input SD & HD mezz .xml files.

XML Info - This parses .xml files for relevant metadata, and then outputs the info to an easily readable .csv file.

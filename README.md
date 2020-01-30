# Front Door Data Collaboration ![All Tests](https://github.com/SocialFinanceDigitalLabs/FrontDoorDataCollaboration/workflows/All%20Tests/badge.svg)


Welcome!

This code was originally developed by [Celine Gross](https://github.com/Cece78), [Chris Owen](https://github.com/chowen94) and [Kaj Siebert](https://github.com/kws) at Social Finance as part of a grant funded programme to support Local Authorities to collaborate on data analysis. The programme was called the ‘Front Door Data Collaboration’. It was supported financially by the Christie Foundation and Nesta (through the ‘What Worls Centre for Children’s Social Care’) and the LAs whose staff guided its development were Bracknell Forest, West Berkshire, Southampton, and Surrey. It also benefitted from advice from the National Performance and Information Managers Group.

We are happy to share this code hoping that other data analysts may benefit from a quick way to standardize Annex A to conduct more analysis. We will be sharing additional code to clean CIN Census and conduct analysis soon - stay tuned!

You can find more info about Social Finance Digital Labs on our website: https://www.sfdl.org.uk/


# How to run this programme

To run this programme, you will need to have installed Python and created a conda environment aligned with requirements.txt.

Once that is done, follow the steps detailed below:
1. Run the 10-MERGE step
2. Run the 20-CLEAN step
3. Run the 30-CUSTOM_CLEAN step (optional)

You're done!


## Step 1: 10-MERGE

The 10-MERGE file uploads all the Annex A files and merges them into a unique one. In the process, it checks column titles and data type within the columns. This programme will ouput three items:
- The merged Annex A ("merged.xlsx"): a unique Annex A file
- The Annex A column report ("column_names.xlsx"): a list of "column_name" from the Annex A guidance matched with the "header_name" found in your file. You may see that some columns were not matched if their titles were not aligned with the Annex A guidance.
- The Annex A error report: a list of values that were discarded because they didn't match the normal column type - e.g. a field with "Yes" where a date was expected. (currently disabled, but will get added in the next version)

To run this step, open the 10-MERGE notebook and run all the cells. You can input the path to your Annex A files by:
1. Giving a list of individual files names:
```
sources = find_sources('examples/example-A-2005.xls', 'examples/example-B-2004.xlsx', data_sources=data_sources)
```
2. Giving a 'glob' pattern to find the files within a folder:
```
sources = find_sources('examples/example-*.*', data_sources=data_sources)
```
You can follow the full, step-by-step walk-through of this step in docs/merger-components.ipynb.


## Step 2: 20-CLEAN

The 20-CLEAN file goes over the merged Annex A ("merged.xlsx") and aligns the values within the columns with the 2019 Annex A guidance. E.g. 'White British' (Ethnicity column) will be converted to 'a) WBRI'. This programme will output two items:
- The matching report ("matching_report.xlsx"): Excel table showing which original values were matched with Annex A-aligned values. Those that were not matched are shown as 'not matched'. The matching is done based on generic rules that should work for most users; however, you have the option to custom the matching in the 'custom clean' step.
- The cleaned Annex A ("cleaned.xlsx"): new Annex A file with values aligned with the 2019 Annex A guidance. The values that were not matched are replaced by 'not matched'. You can change this behaviour in the 'custom clean' step.

To run this step, open the 20-CLEAN notebook and run all the cells. You can change the file paths if required.


## Step 3: 30-CUSTOM_CLEAN

The 30-CUSTOM_CLEAN step enables you to custom the Annex A cleaning and output a new version of the cleaned Annex A. This programme will output one item:
- The cleaned Annex A ("final_cleaned.xslx"): new Annex A file including the edits you made in the matching report.

Go ahead and open the matching report ("matching_report.xlsx") generated by 20-CLEAN: you'll see that you can change how the original value ('former_value' column) is mapped to the Annex A-aligned value ('new_value' column). 

Let's imagine that your data had a row with "Contact Source" : "James Bond". Our generic cleaning rules would not pick that up and you would see the line "James Bond" : "not matched" in the matching report. You can edit this and change it into "James Bond" : "d) 1D: Individual". Do your edits and save the matching report. You're ready to go!

To run this step, open the 30-CUSTOM_CLEAN notebook and run all the cells. You can change the file paths if required.



## Final step: do amazing analysis!

You can now use the final_cleaned Annex A for your analysis right away, without worrying about cleaning it first!

We have focused on providing cleaning rules on the first 8 Annex A lists. If you're keen to add additional rules for the remaining lists, please get in touch and we'd be happy to collaborate.

# meth
tools for processing Pycometh output


### annotate Pycometh out 

When running `Meth_Comp` to determine differential methylation, it is not obvious from the Pycometh output which two-out-of-three samples have similar methylation profile, and the directionality (Methylated/Unmethylated). 

`closestNeighbors.py` uses the information in the 'med_llr_list' and 'raw_llr_list' of the raw `Meth_Comp` output to determine the two closest neighbours in a comparison of three samples for each interval with significant pvalue. 

The script adds two fields: 
- *pair* with the identificatives of the two out of three samples with most similar median methylation probability (from `med_llr_list`).  
- *state* directionality (Methylated/Unmethylated) of the mathylation state in the pair. 

 
`annotatePycomethReport.py --file MethComp_Allchr_d10_w500.pval.tsv > MethComp_Allchr_d10_w500.pval.annotated.tsv`


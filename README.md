# Tools for processing pycoMeth output

### `closestNeighbors.py` 

When running `Meth_Comp` to determine differential methylation, it is not obvious from the pycoMeth output which two-out-of-three samples have similar methylation profile, and the directionality (Methylated/Unmethylated). 

For each interval with significant pvalue, `closestNeighbors.py` uses the information in the 'med_llr_list' and 'raw_llr_list' of the raw `Meth_Comp` output to determine the two closest neighbours in a comparison of three samples. 

The script adds two fields to `Meth_Comp` output: 
- *pair* with the identificatives of the two out of three samples with most similar median methylation probability (from `med_llr_list`).  
- *state* directionality (Methylated/Unmethylated) of the methylation state in the pair. 

 
```
annotatePycomethReport.py --file MethComp_Allchr_d10_w500.pval.tsv > MethComp_Allchr_d10_w500.pval.annotated.tsv
```

### `annotateIntervals.py` 

pycoMeth `Meth_Comp` output includes a folder with data on genomic features close to genomic intervals showing significant differential methylation      

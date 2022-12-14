# Tools for processing pycoMeth output

### `closestNeighbors.py` 

When running `Meth_Comp` to determine differential methylation, it is not obvious from the pycoMeth output which two-out-of-three samples have similar methylation profile, and the directionality (Methylated/Unmethylated). 

For each interval with significant pvalue, `closestNeighbors.py` uses the information in the 'med_llr_list' and 'raw_llr_list' of the raw `Meth_Comp` output to determine the two closest neighbours in a comparison of three samples. 

The script adds two fields to `Meth_Comp` output: 
- *pair* with the identificatives of the two out of three samples with most similar median methylation probability (from `med_llr_list`).  
- *state* directionality (Methylated/Unmethylated) of the methylation state in the pair. 

 
```
closestNeighbors.py --file toydata/PycomethReportToy.tsv > myoutput

```

### `annotateIntervals.py` 

pycoMeth `Meth_Comp` output includes a folder with data on genomic features that are close to genomic intervals showing significant differential methylation in form of a tab separated values (.tsv). However there is no track of the interval identificative (number) or coordinates except in the name of the file. 
      
`annotateIntervals.py` reads and combines all files in a folder adding the information contained in the name of the file: 

- *ichrom* chromosome to which the interval maps 
- *istart* interval starting base 
- *iend* interval ending base 
- *iid* interval identificative (number) 

 
```
annotateIntervals.py --intervals toydata/intervals/ --out  myoutput 

```


to be revised 
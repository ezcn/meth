import sys, os 
import pandas as pd

"""
USAGE annotateIntervals.py --intervals toydata/intervals/ --out  myoutput --inames intervalnamesfile.bed
"""

mydir = sys.argv[sys.argv.index("--intervals") + 1]   ## use slash / at the end of the folder path 
myoutput = sys.argv[sys.argv.index("--out") + 1]

sys.stdout = open('intervalnamesfile.bed', 'w')
 
df = pd.DataFrame()
for root, dirs, files in os.walk(mydir, topdown = False):
   for name in files: 
        x=name.rstrip('.tsv').split('_')
        interval=x[1]; chrom,start,end=x[2].split('-') 
        print '\t'.join([chrom, start, end , interval])  
        myfile=mydir+name
        tmpdf=pd.read_table(myfile, sep="\t")
        tmpdf.columns = tmpdf.columns.str.replace(' ', '_')
        tmpdf=tmpdf.assign(ichrom=chrom, istart=start, iend=end, iid=interval )
        df=pd.concat([df,tmpdf], ignore_index=True) 

tmp=df[['ichrom', 'start','end', 'iid', 'istart', 'iend', 'distance_to_tss',  'transcript_id',  'transcript_name', 'feature_type', 'transcript_biotype', 'chromosome', 'gene_id','strand']]
tmp.to_csv(myoutput, sep="\t", index = False)


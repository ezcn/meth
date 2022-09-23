import sys, os 
import pandas as pd

"""
USAGE intersect.py --intervals toydata/intervals/ --out  myoutput 
"""

mydir = sys.argv[sys.argv.index("--intervals") + 1]   ## use slash / at the end of the folder path 
myoutput = sys.argv[sys.argv.index("--out") + 1]

 
df = pd.DataFrame()
for root, dirs, files in os.walk(mydir, topdown = False):
   for name in files: 
        x=name.rstrip('.tsv').split('_')
        interval=x[1]; chrom,start,end=x[2].split('-') 
        myfile=mydir+name
        tmpdf=pd.read_table(myfile, sep="\t")
        tmpdf=tmpdf.assign(ichrom=chrom, istart=start, iend=end, iid=interval )
        df=pd.concat([df,tmpdf], ignore_index=True) 

df.to_csv(myoutput, sep="\t", index = False)


    #    
    #    with open(myfile) as f:
     #       print ('\t'.join([ 'i_chrom', 'i_start', 'i_end', 'interval'] + next(f).rstrip().split('\t')) )
     #       for line in f:
     #           y=line.rstrip().split('\t') 
      #          print ('\t'.join([chrom, start, end, interval ] + y) )


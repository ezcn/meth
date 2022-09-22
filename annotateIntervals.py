import sys, os 

"""USAGE intersect.py --intervals toydata/intervals > myoutput 
"""

mydir = sys.argv[sys.argv.index("--intervals") + 1]  

for root, dirs, files in os.walk(mydir, topdown = False):
   for name in files: 
        x=name.rstrip('.tsv').split('_')
        interval=x[1]; chrom,start,end=x[2].split('-') 
        myfile=mydir+name
        with open(myfile) as f:
            print ('\t'.join(['interval', 'i_chrom', 'i_start', 'i_end'] + next(f).rstrip().split('\t')) )
            for line in f:
                y=line.rstrip().split('\t') 
                print ('\t'.join([interval, chrom, start, end] + y) )


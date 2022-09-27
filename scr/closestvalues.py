import sys, ast, re

"""USAGE closestvalues.py --file toydata/PycomethReportToy.tsv > myoutput
"""

def methunmeth(values): 
        unmeth=[i for i in values if i<0 ]
        meth=[i for i in values if i> 0 ]
        out= meth if len(meth)>1 else unmeth 
        return out 

myfile = sys.argv[sys.argv.index("--file") + 1]        
with open(myfile) as f:
    print ('\t'.join(['pair', 'state'] + next(f).rstrip().split('\t')) )
    for line in f:
        if re.search('Significant pvalue', line): 
            x=line.rstrip().split('\t') 
            labels=ast.literal_eval(x[10]); values=ast.literal_eval(x[11])
            tempd=dict(zip(map(str,values), labels))
            myclose=methunmeth(values)
            mypair=['-'.join(sorted([tempd[str(i)] for i in myclose]))] 
            #print(myclose)
            state=['Unmethylated' if (all(c < 0 for c in myclose)) else 'Methylated']
            print ('\t'.join(mypair + state + x) )

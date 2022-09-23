import sys, ast, re, numpy as np

"""USAGE closestNeighbors.py --file toydata/PycomethReportToy.tsv > myoutput
"""

def closest (values, N): 
        X = np.array(values).astype(np.float32)
        d = np.abs(X[None, :] - X[:, None])
        np.fill_diagonal(d, np.inf)
        min_array = d.min(0)
        par = np.argpartition(min_array, N)
        closestvalues=X[par[:N]]
        return closestvalues

myfile = sys.argv[sys.argv.index("--file") + 1]        
with open(myfile) as f:
    print ('\t'.join(['pair', 'state'] + next(f).rstrip().split('\t')) )
    for line in f:
        if re.search('Significant pvalue', line): 
            x=line.rstrip().split('\t') 
            labels=ast.literal_eval(x[10]); values=ast.literal_eval(x[11])
            tempd=dict(zip(map(str,values), labels))
            myclose=closest (values, 2)
            mypair=['-'.join(sorted([tempd[str(i)] for i in myclose]))] 
            #print(myclose)
            state=['Unmethylated' if (all(c < 0 for c in myclose)) else 'Methylated']
            print ('\t'.join(mypair + state + x) )

import pandas as pd
df = pd.read_csv("./data/corona.csv")

def filter(line):
    proteins = set()
    line = str(line)
    line = line.lower()
    
    if "(" not in line or "[" not in line:
        proteins.add(line.strip().replace(' ', '_'))
        
    if '(' in line:
        start = 0
        open_in = line.find('(')
        tmp = line[start:open_in].strip().replace(' ', '_')
        proteins.add(tmp)
        while open_in >=0:
            start = open_in+1
            end = line.find(')', start)
            proteins.add(line[start:end].strip().replace(' ', '_'))
            open_in = line.find('(', end)
            
    if '[' in line:
        raw = line[line.find('['):line.find(']')]
        #print("THIS IS RAW:", raw[15:-1])
        raw = raw[15:-1]
        lraw = raw.split("; ")
        for item in lraw:
            #print(item)
            if '(' in item:
                start = 0
                open_in = item.find('(')
                tmp = item[start:open_in].strip().replace(' ', '_')
                proteins.add(tmp)
            else:
                proteins.add(item.strip().replace(' ', '_'))
                
    
    return proteins
    
allProteins = []
i = 0
for u,p in zip(df['Entry'],df['Protein names']):
    print(u,"|",p)
    print("**********************")
    print(u,"|",filter(p))
    print("===================================================")
    i += 1
    if i>10:
        break
        
allProteins = []
for u,p in zip(df['Entry'],df['Protein names']):
    allProteins.append({"id":u, "names":filter(p)})
    

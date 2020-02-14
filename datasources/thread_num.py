import subprocess

def get_thread():
    a=subprocess.Popen(('top','-n','1','-b'),stdout=subprocess.PIPE)
    a=subprocess.check_output(('head','-n','12'),stdin=a.stdout)
    a=a.decode("utf-8").split('\n')
    sa=[]
    for d in a:
        sa.append(d.split())
    #print(sb)
    return sa
    #print(sa[2][7])
    #print(sb[7])
    #print(sb[8])
    #print(sb[9])
    #print(sb[10])
    #print(sb[11])

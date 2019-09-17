def deal(dir,cancer):
    ppifile=open(str(dir)+"//"+"all_interaction_final.txt","r")
    file=open(str(dir)+"//"+str(cancer)+"//G1.txt","r")
    outputefile=open(str(dir)+"//"+str(cancer)+"//association.txt","w")
    ppidata={}
    data = ppifile.readline()
    while True:#读取ppi文件的数据
        str1=ppifile.readline()
        if str1=="" or str1==None:
            break
        data=[ str(a) for a in str1.split()]
        if ppidata.get(data[0])==None:
            ppidata.update({data[0]:{data[1]:float(data[2])}})
        else:
            ppidata.get(data[0]).update({data[1]:float(data[2])})
    ppifile.close()

    while True:#比较两个文件的数据，然后根据情况替换值
        str1 = file.readline()
        if str1=="" or str1==None:
            break
        data = [str(a) for a in str1.split()]
        ppi=0
        if ppidata.get(data[0])==None:
            pass
        elif ppidata.get(data[0]).get(data[1])==None:
            pass
        else:
            ppi=ppidata.get(data[0]).get(data[1])
        if ppidata.get(data[1]) == None:
            pass
        elif ppidata.get(data[1]).get(data[0]) == None:
            pass
        else:
            ppi = ppidata.get(data[1]).get(data[0])

        #若ppi里的值大同于num的值，则替换。
        if ppi!=0:
            correction=float(ppi)
        else:
            correction=float(data[2])

        if correction==0 or correction==1:
            correction=int(correction)
        if correction<0.4:
            continue
        outputefile.write(data[0]+"\t"+data[1]+"\t"+str(correction)+"\n")
    file.close()
    outputefile.close()









deal("F://test//ganesh","BRCA")
deal("F://test//ganesh","COAD")
deal("F://test//ganesh","GBM")
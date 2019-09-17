def calculate(dir,cancer):  #选择频率大于0.6的基因作为候选regulator
    file=open(str(dir)+"//"+str(cancer)+"//"+str(cancer)+"_Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes","r")
    frenquencyfile=open(str(dir)+"//"+str(cancer)+"//"+str(cancer)+"_regulator.txt","w")
    file.readline()
    genenames=[]
    while True:
        str1=file.readline()
        mutuationnum=0
        if str1==None or str1=="":
            break
        datas=str1.split()
        genenames.append(datas[0])
        for data in datas:
            if data=="1" or data=="2" or data=="-1" or data=="-2":
                mutuationnum+=1
        mutuationfrenquency=float(mutuationnum/(len(datas)-1))
        if mutuationfrenquency>=0.6:
            frenquencyfile.write(datas[0]+"\n")

    file.close()
    frenquencyfile.close()
def calculate2(dir,cancer): #选择突变频率前300的基因作为候选regulator
    file=open(str(dir)+"//"+str(cancer)+"//"+str(cancer)+"_Gistic2_CopyNumber_Gistic2_all_thresholded.by_genes","r")
    frenquencyfile=open(str(dir)+"//"+str(cancer)+"//"+str(cancer)+"_frenquency.txt","w")
    file.readline()
    genenames=[]
    frenquenciesMap={}
    while True:
        str1=file.readline()
        mutuationnum=0
        if str1==None or str1=="":
            break
        datas=str1.split()
        genenames.append(datas[0])
        for data in datas:
            if data=="1" or data=="2" or data=="-1" or data=="-2":
                mutuationnum+=1
        mutuationfrenquency=float(mutuationnum/(len(datas)-1))
        frenquenciesMap[datas[0]]=mutuationfrenquency
    frenquenciesMap=sorted(frenquenciesMap.items(), key=lambda x: x[1], reverse=True)
    number=0
    print(frenquenciesMap)
    for item in frenquenciesMap:
        number+=1
        if number>300:
            break
        frenquencyfile.write(item[0] + "\n")
    file.close()
    frenquencyfile.close()

calculate("F://test//ganesh","BRCA")
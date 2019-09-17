from numpy import *;

def outputMatrixToFile(m,dir,genenames):#将矩阵m写到指定目录的方法
    a=m.tolist()
    outputfile=open(dir,"w")
    outputfile.write("\t")
    i=0
    for genename in genenames:
        outputfile.write(genename+"\t")
    outputfile.write("\n")
    for line in a:
        outputfile.write(genenames[i]+"\t")
        i+=1
        for num in line:
            if num==0 or num==1:
                outputfile.write(str(int(num)))
            else:
                outputfile.write(str(num))
            outputfile.write("\t")
        outputfile.write("\n")
    outputfile.close()

def DealCancerFile(dir,cancer): #根据目录和癌症名处理矩阵的方法
    filename = str(dir)+str(cancer)+"//cluster1.output.txt"
    file1 = open(filename, "r")
    file1.readline()
    genenames = []
    matnums = []
    finalmatrix = []
    genenum = 0
    while True:
        content = file1.readline()
        if content == None or content == "":
            break
        strs = content.split()
        genename = strs.pop(0)
        genenames.append(genename)
        nums = [int(num) for num in strs]
        matnums.append(nums)
    file1.close()
    mat1 = mat(matnums)
    finalmatrix = mat1 * mat1.T
    # 读取后四个文件，并计算其矩阵*矩阵^T
    for i in range(2, 6):
        filename =str(dir)+str(cancer)+"//cluster"+str(i)+ ".output.txt"""
        file1 = open(filename, "r")
        file1.readline()
        Map = {}
        matnums2 = []
        while True:  # 读取文件数据，并根据基因名存储到map中
            content = file1.readline()
            if content == None or content == "":
                break
            strs = content.split()
            genename = strs.pop(0)
            nums = [int(num) for num in strs]
            Map[genename] = nums
        file1.close()
        for genename in genenames:  # 根据第一个文件的基因顺序生成对应的矩阵数据
            matnums2.append(Map[genename])

        # 将矩阵相加
        mat2 = mat(matnums2)
        finalmatrix += mat2 * mat2.T
    #取均值然后保存到对应目录
    finalmatrix = finalmatrix / 5
    outputMatrixToFile(finalmatrix,str(dir)+str(cancer)+"//G.txt",genenames)

DealCancerFile("F://test//ganesh//","BRCA")






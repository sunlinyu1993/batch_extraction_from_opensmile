import os
from subprocess import call
import time

#path constants


# pathConfig = pathExecute + "config\\" + "IS09_emotion.conf"

# read cmd from windows by call function
def excuteCMD(_pathExcuteFile,_pathConfig,_pathAudio,_pathOutput):
    cmd = _pathExcuteFile + " -C "+ _pathConfig +" -I "+ _pathAudio + " -O " + _pathOutput
    call(cmd,shell=True)
# filepath='F:/DataSet/音频文件/IEMOCAP/IEMOCAPwavfile'
def feature_get(filepath,_pathExcuteFile,_pathConfig):
    dirfile=os.listdir(filepath)
    for filesone in dirfile:#traverse ten persons
        filepathone=os.path.join(filepath,filesone)
        dirfileone=os.listdir(filepathone)
        for filesc in dirfileone:#traverse emotion files
            filepathsc=os.path.join(filepathone,filesc)
            dirfiletwo=os.listdir(filepathsc)
            for fileth in dirfiletwo:# traversal wav files
                namefront=os.path.splitext(fileth)[0]
                _pathAudio=os.path.join(filepathsc, fileth)
                _pathOutput='F:/DataSet/校对过的数据集/only_hap/IEMOCAP42维特征_vector_09func/'+filesone+'/'+filesc+'/'+str(namefront)+'.txt'
                excuteCMD(_pathExcuteFile, _pathConfig, _pathAudio, _pathOutput)
#opensmile bin path
pathExecute = "F:/语音情感识别/语音特征提取工具/opensmile-2.3.0/"
pathExcuteFile = pathExecute + "bin/Win32/" + "SMILExtract_Release"
#opensmile config path
configpath='F:/语音情感识别/语音特征提取工具/opensmile-2.3.0/config/42/vector'
#audio file path
filepath='F:/DataSet/音频文件/IEMOCAP/IEMOCAPwavfilehap'

configpathfile=os.listdir(configpath)

for configpathfilepper in configpathfile:
    configpathfinall=os.path.join(configpath,configpathfilepper)
    feature_get(filepath=filepath,_pathExcuteFile=pathExcuteFile,_pathConfig=configpathfinall)





# def loopExcuteOuterLayer(_pathExcuteFile,_pathConfig,_pathAudioRoot,_pathOutputRoot):
#     flag = -1
#     for rt, dirs, files in os.walk(_pathAudioRoot):
#         if os.path.isdir(rt):
#             if flag == -1:
#                 listDirlist = dirs
#             else:
#                 _pathOutputRootSecond = os.path.join(_pathOutputRoot,listDirlist[flag])
#                 _pathAudioRootSecond = os.path.join(_pathAudioRoot,listDirlist[flag])
#                 if not os.path.exists(_pathOutputRootSecond):
#                     os.mkdir(_pathOutputRootSecond)
#                 loopExcuteInnerLayer(_pathExcuteFile,_pathConfig,_pathAudioRootSecond,_pathOutputRootSecond)
#             flag = flag + 1
#
# def loopExcuteInnerLayer(_pathExcuteFile,_pathConfig,_pathAudioRoot,_pathOutputRoot):
#     for i in os.listdir(_pathAudioRoot):
#         nameBehind =  os.path.splitext(i)[1]
#         nameFront = os.path.splitext(i)[0]
#         if nameBehind =='.wav':
#             print(i)
#             _pathOutput = os.path.join(_pathOutputRoot, nameFront+".txt")
#             _pathAudio = os.path.join(_pathAudioRoot, i)
#             excuteCMD(_pathExcuteFile,_pathConfig,_pathAudio,_pathOutput)

# if __name__ == '__main__':
#     time1 = time.time()
#     loopExcuteOuterLayer(pathExcuteFile, pathConfig, pathAudioRoot, pathOutputRoot)
#     time2 = time.time()



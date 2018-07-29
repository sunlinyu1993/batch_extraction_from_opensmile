import os
import numpy as np
import pandas as pd
from sklearn import preprocessing

path='F:\DataSet\校对过的数据集\only_hap\IEMOCAP42维特征_vector_09func'
for index, peoplefiles in enumerate(os.listdir(path)):
        emotionpath = os.path.join(path, peoplefiles)
        for emotionfiles in os.listdir(emotionpath):
            csvfilespath = os.path.join(emotionpath, emotionfiles)
            for csvfiles in os.listdir(csvfilespath):
                finallpath = os.path.join(csvfilespath, csvfiles)
                namefront = os.path.splitext(csvfiles)[0]
                x_data=[]
                x_datalist=[]
                x_datamat=[]
                cnt=1
                fa = open(finallpath)
                for line in fa:
                    if cnt==513:
                        x_data=line.split(",")
                        x_data=x_data[2:-1]

                    elif cnt<513:
                        pass

                    cnt=cnt+1


                if 'ang' in emotionfiles:

                    x_data.append(0)
                    x_data_vector=np.reshape((np.array(x_data)),[1,-1])
                    # samplenum=x_datamat.shape[0]
                    # label=np.ones((samplenum,1))*0
                    # x_datamat=np.hstack((x_datamat,label))
                elif 'hap' in emotionfiles:
                    # x_data = x_data.tolist
                    # samplenum = x_datamat.shape[0]
                    # label = np.ones((samplenum, 1)) * 1
                    # x_datamat = np.hstack((x_datamat, label))

                    x_data.append(1)
                    x_data_vector = np.reshape((np.array(x_data)), [1, -1])
                elif 'neu' in emotionfiles:
                    # x_data = x_data.tolist
                    # samplenum = x_datamat.shape[0]
                    # label = np.ones((samplenum, 1)) * 2
                    # x_datamat = np.hstack((x_datamat, label))

                    x_data.append(2)
                    x_data_vector = np.reshape((np.array(x_data)), [1, -1])
                elif 'sad' in emotionfiles:
                    # x_data = x_data.tolist
                    # samplenum = x_datamat.shape[0]
                    # label = np.ones((samplenum, 1)) * 3
                    # x_datamat = np.hstack((x_datamat, label))

                    x_data.append(3)
                    x_data_vector = np.reshape((np.array(x_data)), [1, -1])
                # x_data=np.array(x_data)
                # x_data=np.reshape(x_data,[1,-1])
                DF = pd.DataFrame(x_data_vector)
                DF.to_csv('F:\DataSet\校对过的数据集\only_hap\IEMOCAP42维特征_vector_09func_csv/' + peoplefiles + '/'+emotionfiles+'/'+namefront+'.csv',
                          header=False, index=False)

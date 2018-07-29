import os
import numpy as np
import pandas as pd
from sklearn import preprocessing



def segment_lstm(features,sequence,paddingnum):
    #lstm后边补零
    featureSegment = []
    # frameSegmentend = []
    # frameSegmentfirst=voiceindex[0]
    # for voiceframenum in range(len(voiceindex)-1):
    #     if voiceindex[voiceframenum + 1] - voiceindex[voiceframenum] > 1:
    #         frameSegmentend.append(voiceindex[voiceframenum])
    #         frameSegmentfirst.append(voiceindex[voiceframenum+1])

    features = preprocessing.scale(features)
    # featureSegment=features[voiceindex,:]
    [N, M] = np.shape(features)
    segment_features = []
    feature_mat_all = []
    utterance_features=[]
    i = 0
    #每一个segment分别补长
    if N <= sequence:
        padding = sequence - N
        padmat = np.ones((padding, M)) * paddingnum
        segment_features = np.vstack((features, padmat))
    elif N > sequence:
        while 1:
            if N - sequence * i >= sequence:
                features_mat = features[i * sequence:i * sequence + sequence, :]
                feature_mat_all.append(features_mat)
                i = i + 1
            elif N - sequence * i > 0 and N - sequence * i < sequence:
                padding = sequence - (N - sequence * i)
                padmat = np.ones((padding, M)) * paddingnum
                feature_mat = features[sequence * i:, :]
                combine_mat = np.vstack((feature_mat, padmat))
                feature_mat_all.append(combine_mat)
                i = i + 1
            elif N - sequence * i <= 0:
                break
        segment_features = np.concatenate((feature_mat_all[0:]), axis=0)
    # utterance_features.append(segment_features)
    utterance_features=np.array(segment_features)
    return utterance_features

def segment_cnn(features,sequence,paddingnum):
    #两边补0
    features = preprocessing.scale(features)
    # featureSegment = features[voiceindex, :]
    [N, M] = np.shape(features)
    segment_features = []
    feature_mat_all = []
    utterance_features = []
    i = 0
    # 每一个segment分别补长
    if N % 2 == 0:  # if N is even
        if N <= sequence:
            padding = sequence - N
            padmat = np.ones((int(padding / 2), M)) * paddingnum
            segment_features = np.vstack((padmat, features, padmat))  # CNN需要两边补零
        elif N > sequence:
            while 1:
                if N - sequence * i >= sequence:
                    features_mat = features[i * sequence:i * sequence + sequence, :]
                    feature_mat_all.append(features_mat)
                    i = i + 1
                elif N - sequence * i > 0 and N - sequence * i < sequence:
                    padding = sequence - (N - sequence * i)
                    padmat = np.ones((int(padding / 2), M)) * paddingnum
                    feature_mat =features[sequence * i:, :]
                    combine_mat = np.vstack((padmat, feature_mat, padmat))
                    feature_mat_all.append(combine_mat)
                    i = i + 1
                elif N - sequence * i <= 0:
                    break
            segment_features = np.concatenate((feature_mat_all[0:]), axis=0)
    if N % 2 == 1:  # if N is odd
        if N <= sequence:
            padding = sequence - N
            padmatone = np.ones((int(padding / 2), M)) * paddingnum
            padmattwo = np.ones((int(padding / 2) + 1, M)) * paddingnum

            segment_features = np.vstack((padmatone, features, padmattwo))  # CNN需要两边补零
        elif N > sequence:
            while 1:
                if N - sequence * i >= sequence:
                    features_mat = features[i * sequence:i * sequence + sequence, :]
                    feature_mat_all.append(features_mat)
                    i = i + 1
                elif N - sequence * i > 0 and N - sequence * i < sequence:
                    padding = sequence - (N - sequence * i)
                    padmatone = np.ones((int(padding / 2), M)) * paddingnum
                    padmattwo = np.ones((int(padding / 2) + 1, M)) * paddingnum
                    feature_mat = features[sequence * i:, :]
                    combine_mat = np.vstack((padmatone, feature_mat, padmattwo))
                    feature_mat_all.append(combine_mat)
                    i = i + 1
                elif N - sequence * i <= 0:
                    break
            segment_features = np.concatenate((feature_mat_all[0:]), axis=0)

    utterance_features = np.array(segment_features)
    return utterance_features



def voice_segment_lstm_nopad(features, sequence):
    # 语音一句话的最后的一段segment直接删去，不进行补长，要在截断之前加号类标，因为label是固定长度和原有语音帧数量对应（一句话两个类标）
    # filepath='F:/DataSet/音频文件/IEMOCAP/IEMOCAPwavfile/02M/hap/Ses02M_script01_3_F001.wav'
    # wnd=400
    # inc=160
    # T1=0.05
    # minL=10
    # pitch_vad(filepath,wnd,inc,T1,minL=10)
    [N, M] = np.shape(features)
    # features_segment = preprocessing.scale(
    #     features)  # 因为labelvoice和Unvoice在外面这里我们先加入了类标，归一化是减去类标注意减去类标(用这个函数注意和上面进行区别）
    # features_all = np.hstack((features_segment, features[:, -1]))

    i = 0
    feature_mat_all = []
    if N < sequence:
        print('error')
    elif N >= sequence:
        while 1:
            if N - sequence * i >= sequence:
                features_mat = features[i * sequence:i * sequence + sequence, :]
                feature_mat_all.append(features_mat)
                i = i + 1
            elif N - sequence * i <= 0 or (N - sequence * i < sequence and N - sequence * i > 0):
                break
    # if len(feature_mat_all)==1:
    #     segment_features=feature_mat_all
    # if len(feature_mat_all)>1:
    segment_features = np.concatenate((feature_mat_all[0:]), axis=0)
    utterance_features = np.array(segment_features)
    return utterance_features

path='F:/DataSet/校对过的数据集/only_hap/09emotion/IEMOCAP_09emo_mat_32'
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
                    if cnt>=40:
                        x_data=line.split(",")
                        x_data=x_data[1:-1]
                        x_datalist.append(x_data)
                    elif cnt<40:
                        pass

                    cnt=cnt+1
                x_datamat=np.array(x_datalist)
                # x_datamat=voice_segment_lstm_nopad(x_datamat,50)
                if 'ang' in emotionfiles:
                    # x_data=x_data.tolist
                    samplenum=x_datamat.shape[0]
                    label=np.ones((samplenum,1))*0
                    x_datamat=np.hstack((x_datamat,label))
                elif 'hap' in emotionfiles:
                    # x_data = x_data.tolist
                    samplenum = x_datamat.shape[0]
                    label = np.ones((samplenum, 1)) * 1
                    x_datamat = np.hstack((x_datamat, label))
                elif 'neu' in emotionfiles:
                    # x_data = x_data.tolist
                    samplenum = x_datamat.shape[0]
                    label = np.ones((samplenum, 1)) * 2
                    x_datamat = np.hstack((x_datamat, label))
                elif 'sad' in emotionfiles:
                    # x_data = x_data.tolist
                    samplenum = x_datamat.shape[0]
                    label = np.ones((samplenum, 1)) * 3
                    x_datamat = np.hstack((x_datamat, label))
                # x_data=np.array(x_data)
                # x_data=np.reshape(x_data,[1,-1])
                DF = pd.DataFrame(x_datamat)
                DF.to_csv('F:/DataSet/校对过的数据集/only_hap/09emotion/IEMOCAP_09emo_mat_32_csv/' + peoplefiles + '/'+emotionfiles+'/'+namefront+'.csv',
                          header=False, index=False)


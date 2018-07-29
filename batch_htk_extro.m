clear;
path='F:\DataSet\新处理的数据集\opensmile_feature\';
C=2.^(-4:4);
Kpar=2.^(-4:4);
files=dir(path);
filename={files.name};
filenum=length(filename);
csvmattalltrain=[];
csvmatalltest=[];
    for i=3:filenum
           filepath=[path,filename{i}];
           fileemotion=dir(filepath);
           fileemotionname={fileemotion.name};
           fileemotionnum=length(fileemotionname);
           for j=3:fileemotionnum
               filecsvpath=[filepath,'\',fileemotionname{j}];
               filecsv=dir(filecsvpath);
               filecsvname={filecsv.name};
               filecsvnum=length(filecsvname);
               for p=3:filecsvnum
                   name=filecsvname{p}(1:end-4);
                   filefinalpath=[filecsvpath,'\',filecsvname{p}];
                   is09vector=readhtk(filefinalpath);
                   csvwrite('F:\DataSet\新处理的数据集\opensmile_feature_htk',filename{i},'\',fileemotionname{j},'\',filecsvname{p},'\',name,'.csv')
               end
           end
    end
    
                   
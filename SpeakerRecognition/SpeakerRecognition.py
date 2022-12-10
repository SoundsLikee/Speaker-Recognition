from speechbrain.pretrained import SpeakerRecognition
import os
import sys

if len(sys.argv) <= 1:
    print("Error: No Argument")
    sys.exit()
    
src_path ="speechbrain/spkrec-ecapa-voxceleb"; #"speechbrain/spkrec-ecapa-voxceleb"
save_dir = "./pretrained_models/spkrec-ecapa-voxceleb";
verification = SpeakerRecognition.from_hparams(source=src_path, savedir=save_dir)


file1 = sys.argv[1]
path = sys.argv[2]
files = os.listdir(path)
files.sort() 

t = False
r = -100  
name = "none" 
for file_ in files:    
    print(path +file_)
    file2 = path +file_
    if file_[0] == '.':
        continue
    score, prediction = verification.verify_files(file1, file2)
    print(score)
    print(prediction)
    if prediction[0] :
        t = True
        if score[0] > r :
            r = score[0]
            name = file_.split('.')[0]
f = open('result.txt','w')

f.write(str(t)+'\n'+ name+'\n'+str(r))
print(t,name,r)

1. 먼저 환경에서 "pip install speechbrain"를 수행한다.

2. python SpeakerRecognition.py ['입력 음성파일 경로']  ['test용 음성파일의 폴더 경로']

    폴더에서 음성파일을 있어야 한다

```
python SpeakerRecognition.py '/content/sample_data/input/input1.wav' '/content/sample_data/test/'
```
3. 결과는 SpeakerRecognition.py 과 동일하는 폴더에서 result.txt파일에 있다.

    내용은 다음과 같다

```
True #입력한 음성과 저장된 음성이 같은 사람인지
test1 # 같으면 같은 사람의 이름 (test폴더 에서 저장한 파일과 동일 )
tensor(0.6251)# 정확도
```
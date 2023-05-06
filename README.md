# Safety First
> 이 프로젝트는 복원, 보완 중에 있습니다.<br> 
당시 본인이 맡은 파트였던 머신러닝 코드와 얼굴인식 관련 내용이 기록되어 있습니다.<br>
미완이었던, 데이터를 받아 핸드폰으로 푸시알림을 보내는 것을 다시 한번 진행하고 작성중입니다. <br>

+ [x] 보완 완료

## 프로젝트 소개
프로젝트 기간 : 2021.03 ~ 2021.12 <br>
홍익대학교 컴퓨터공학과 4학년 졸업 프로젝트 입니다. 3명의 팀원과 진행한 팀프로젝트 입니다. <br>

거주민이 출입하는 입구에 카메라를 설치하고, <br>
머신러닝 기반의 오브젝트 검출 알고리즘 Haar Cascade를 사용하여 카메라에 비치는 사람의 얼굴을 인식합니다.<br>
인식 후 그 사람이 위험인물인지 아닌지를 파악하여 해당 인물이 위험인물인지 아닌지 구분하여
위험인물일시 거주자의 핸드폰으로 경고 알림을 보냅니다. 

## 프로젝트 개발 동기
1인 가구나, 여성 밀집 거주지역, 낙후된 지역에서의 잦은 스토킹 피해등을 보고 프로젝트를 개발하게 되었습니다. <br>
사용자가 거주하는 단지내에 카메라를 설치한 뒤, 카메라 사람이 인식되면 인식된 사람을 구분하여 위험인물이나 수상한 인물일 경우 알림을 보낼수 있다면 그에 대비할 수 있지 않을까 하는 생각을 바탕으로 프로젝트를 기획하였습니다. <br>

## 프로젝트 상세 
1. 얼굴등록 (store_faces.py)
* 거주자 등록  <br>

본 프로젝트는 특정 단지나 아파트 거주민들을 타겟으로 설정한 프로젝트입니다. 아파트 단지에 살고 있는 거주자들의 얼굴 정보를 등록합니다. <br>
store_faces.py 를 사용하여 아파트 거주자들의 얼굴을 찍습니다. 찍은 사진은 Resident 폴더에 저장됩니다. 

* 자주 출입하는 사람 등록  <br>

해당 아파트 단지의 담당 택배기사님이나 경비아저씨의 경우, 아파트에 거주하지 않을수 있지만 거주하지 않는다고 매번 위험 알림을 보낼시 불편을 야기합니다. <br>
거주자 등록때와 마찬가지로 store_faces.py 를 사용하여 얼굴을 찍어, often 폴더에 저장합니다.

* 얼굴이 공개된 범죄자 등록  <br>

얼굴이 기록되지 않은 범죄자들이 대다수지만 흉악범등은 미디어를 통해 얼굴이 공개된 경우가 있습니다. <br>
이런 범죄자들의 얼굴사진을 인터넷에서 얻어 XMAN폴더에 저장합니다. 

2. 카메라 설치 <br>
아파트 단지 입구등 사람들이 자주 출입하는 곳에 카메라를 설치합니다.<br>
-> 본 프로젝트에서 설치 카메라는 라즈베리 카메라를 연결하여 구동하였습니다.<br>

3. 모델 학습 & 얼굴 인식 & 위험 메세지 전송 (training_recognize_fcm.py)

* 모델 학습 <br>
머신러닝 기반의 오브젝트 검출 알고리즘 Haar Cascade를 사용합니다. trains()로 등록한 얼굴사진을 학습합니다. <br>
얼굴 인식용 'haarcascade_frontalface_default.xml' 를 로딩하여 얼굴 검출에 사용합니다.

* 얼굴인식 <br>
85 보다 크면 동일 인물로 간주합니다. <br>
유사도 85 이상이며 데이터가 위험인물로 분류된 사람일 경우, 거주자로 분류된 사람일 경우 , 자주 등록된 사람으로 분류될 경우,
이렇게 3가지 경우로 나누어져 분류되고, 화면상에 그룹이 표시됩니다. <br>
3가지 그룹모두에 속하지 않은 경우 'Unknown'으로 표시됩니다. 

* 위험 메세지 전송 <br>
firebase의 FCM(Firebase Cloud Messaging)을 사용하여 핸드폰으로 메세지를 보냅니다. <br>
범죄자로 등록된 사람으로 인식된 경우 거주자의 핸드폰으로 위험(Danger!) 알림을 보냅니다. <br>
그 외 3가지 그룹모두 등록되지 않은 사람(Unknown)의 경우도 외부인이므로 경고(Warning!) 알림을 보냅니다. <br>
위의 두가지 경우에 속하는 사람이 카메라 앞에 계속 서 있을경우 알림도 계속 전송되는것을 방지하기위해 마지막으로 보낸 위험알림으로 부터 
10분이 지난경우에만 다시 위험알림을 보내도록 하였습니다. 

## 📚Stack

![badge](https://img.shields.io/badge/RaspberryPi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![badge](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![badge](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![badge](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white)
![badge](https://img.shields.io/badge/AndroidStudio-3DDC84?style=flat-square&logo=androidstudio&logoColor=white)

## Installation
> anaconda가 필요합니다. <br>
> Firebase와 Android Studio의 연동이 필요합니다.

### anaconda 설치 
참고 자료 : https://www.anaconda.com/download/

### Firebase, Android Studio 연동
참고 자료 : https://www.youtube.com/watch?v=M7z2MFoI6MQ

1. anaconda에서 필요한 패키지를 다운로드
```python
$ pip install --upgrade pip
$ pip install opencv-python
$ pip install opencv-contrib-python
$ pip install pyfcm
```

2. 본 레포지토리 클론 
```python
$ git clone https://github.com/sigma-wbi/Graduation_project.git
```

3. vscode등 작업하는 환경에서, 1단계에서 패키지를 설치한 anaconda 환경으로 인터프리터를 변경합니다.

4. 'fcm.py' 의 APIKEY, TOKEN 값을 입력합니다. 
- APIKEY 는 firebase 콘솔에서 서버키를 받아 입력합니다. 
- TOKEN 은 본 프로젝트의 FCM 폴더를 android studio 에서 실행시키면 android의 화면에 뜨도록 하였습니다. <br>
복사하여 입력합니다. 

## run the program
1. store_faces.py 실행

초기 거주자들의 데이터베이스를 위한 과정입니다. <br>
현재 카메라에 비치는 인물을 어느 그룹에 저장할지 결정한 뒤 그룹버튼을 누르면 해당인물이 faces폴더와 3개의 그룹폴더가 생성되고,<br>
설정한 그룹폴더안에 저장됩니다.

2. training_recognize_fcm.py 실행

카메라에 비치는 인물이 위험인물인지 판단합니다. <br>
위험인물일 경우 'Danger!' , 등록되지 않은 인물일경우 'Warning!'을 푸시알림으로 전송합니다.

3. 결과화면

<img width="60%" src="https://user-images.githubusercontent.com/81278907/235640308-6e78a25b-bb73-4de0-9c16-212a34708081.gif"/>

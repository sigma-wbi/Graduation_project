# Safety First
> 이 프로젝트는 복원, 보완 중에 있습니다.<br> 
현재 본인이 맡은 파트였던 머신러닝 코드와 얼굴인식 관련 내용이 기록되어 있습니다.<br>
다른 팀원들의 역할이었던 데이터를 받아 핸드폰으로 푸시알림을 보내는 것을 다시한번 진행하고 작성중입니다. <br>

+ [ ] 보완 완료

## 프로젝트 소개
홍익대학교 컴퓨터공학과 4학년 졸업 프로젝트 입니다. 3명의 팀원과 진행한 팀프로젝트 입니다. <br>

거주민이 출입하는 입구에 카메라를 설치하고 (본 프로젝트에서 설치 카메라는 라즈베리 카메라를 연결하여 구동하였습니다.)<br>
머신러닝 기반의 오브젝트 검출 알고리즘 Haar Cascade를 사용하여 카메라에 비치는 사람의 얼굴을 인식합니다.<br>
인식 후 그 사람이 위험인물인지 아닌지를 파악하여 해당 인물이 위험인물인지 아닌지 구분하여
위험인물일시 거주자의 핸드폰으로 경고 알림을 보냅니다. 

## 프로젝트 개발 동기
1인 가구나, 여성 밀집 거주지역, 낙후된 지역에서의 잦은 스토킹 피해등을 보고 프로젝트를 개발하게 되었습니다. <br>
사용자가 거주하는 단지내에 카메라를 설치한 뒤, 카메라 사람이 인식되면 인식된 사람을 구분하여 위험인물이나 수상한 인물일 경우 알림을 보낼수 있다면 그에 대비할 수 있지 않을까 하는 생각을 바탕으로 프로젝트를 기획하였습니다. <br>

## 기능 상세 

* Extract 
Dummy data를 RDS에 저장하고 이 데이터를 기반으로 생성된 Log data를 가져옴

* Transform 
Log data의 길이 및 용량을 줄이기 위해 필요없는 문자 제거 및 딕셔너리 형식 사용

* Load
S3에 적재시 gz형식으로 한번 더 압축 및 날짜와 시간별로 파티셔닝 후 저장


## 📚Stack

![badge](https://img.shields.io/badge/RaspberryPi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![badge](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![badge](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![badge](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=white)
![badge](https://img.shields.io/badge/AndroidStudio-3DDC84?style=flat-square&logo=androidstudio&logoColor=white)



## Installation
> anaconda가 필요합니다.

### anaconda 설치 
참고 자료 : https://www.anaconda.com/download/


1. anaconda에서 필요한 패키지를 다운로드
```python
$ pip install --upgrade pip
$ pip install opencv-python
$ pip install opencv-contrib-python
```

2. 본 레포지토리 클론 
```python
$ git clone https://github.com/sigma-wbi/Graduation_project.git
```

3. vscode등 작업하는 환경에서, 1단계에서 패키지를 설치한 anaconda환경으로 인터프리터를 변경합니다.


## run the program
1. traning.py 실행

초기 거주자들의 데이터베이스를 위한 과정입니다. <br>
현재 카메라에 비치는 인물을 어느 그룹에 저장할지 결정한 뒤 그룹버튼을 누르면 해당인물이 faces폴더와 3개의 그룹폴더가 생성되고,<br>
설정한 그룹폴더안에 저장됩니다.

2. training_and_recognize.py 실행

카메라에 비치는 인물이 위험인물인지 판단합니다.

3. 결과화면

<img width="80%" src="https://user-images.githubusercontent.com/81278907/235640308-6e78a25b-bb73-4de0-9c16-212a34708081.gif"/>

## Report
https://github.com/sigma-wbi/Graduation_project
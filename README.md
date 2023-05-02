# Safety First
> 이 프로젝트는 복원, 보완 중에 있습니다.<br> 
현재 본인이 맡은 파트였던 머신러닝 코드와 얼굴인식 관련 내용이 기록되어 있습니다.<br>
다른 팀원들의 역할이었던 데이터를 받아 핸드폰으로 푸시알림을 보내는 것을 다시한번 진행하고 작성중입니다. <br>

+ [ ] 보완 완료

## 프로젝트 소개
홍익대학교 컴퓨터공학과 4학년 졸업 프로젝트 입니다. 3명의 팀원과 진행한 팀프로젝트 입니다. <br>

머신러닝 기반의 오브젝트 검출 알고리즘 Haar Cascade를 사용하여 카메라에 비치는 사람의 얼굴을 인식하고,<br>
3단계에 걸쳐 그 사람이 위험인물인지 아닌지를 파악하여 해당 인물이 위험인물인지 아닌지 구분하여
위험인물일시 거주자의 핸드폰으로 경고 알림을 보냅니다. 

## 프로젝트 개발 동기
1인 가구나, 여성 밀집 거주지역, 낙후된 지역에서의 잦은 스토킹 피해등을 보고 프로젝트를 개발하게 되었습니다. <br>
사용자가 거주하는 단지내에 카메라를 설치한 뒤, 카메라 사람이 인식되면 인식된 사람을 구분하여 위험인물이나 수상한 인물일 경우 알림을 보낼수 있다면 그에 대비할 수 있지 않을까 하는 생각을 바탕으로 프로젝트를 기획하였습니다. 


## 기능 상세 

* Extract 
Dummy data를 RDS에 저장하고 이 데이터를 기반으로 생성된 Log data를 가져옴

* Transform 
Log data의 길이 및 용량을 줄이기 위해 필요없는 문자 제거 및 딕셔너리 형식 사용

* Load
S3에 적재시 gz형식으로 한번 더 압축 및 날짜와 시간별로 파티셔닝 후 저장


## 📚Stack

![badge](https://img.shields.io/badge/AmazonRDS-527FFF?style=flat-square&logo=AmazonRDS&logoColor=white)
![badge](https://img.shields.io/badge/AmazonS3-009639?style=flat-square&logo=AmazonS3&logoColor=white)
![badge](https://img.shields.io/badge/AmazonEC2-990099?style=flat-square&logo=AmazonEC2&logoColor=white)
![badge](https://img.shields.io/badge/Airflow-FF9900?style=flat-square&logo=apache-airflow&logoColor=white)



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

4. venv 폴더 아래에서 파일을 실행합니다.

## run the program
1. traning.py 실행
초기 거주자들의 데이터베이스를 위한 과정입니다. <br>
현재 카메라에 비치는 인물을 어느 그룹에 저장할지 결정한 뒤 그룹버튼을 누르면 해당인물이 faces폴더안의 그룹에 저장됩니다.

2. training_and_recognize.py 실행
카메라에 비치는 인물이 위험인물인지 판단합니다.

3. 결과화면
![image](https://user-images.githubusercontent.com/109950265/222493919-16121577-0c66-43dc-81ee-f62e1502cd67.png)



## Report
https://github.com/sigma-wbi/ETL_pipeline/tree/main/report
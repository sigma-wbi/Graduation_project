import cv2
import numpy as np
from os import listdir
from os.path import isdir, isfile, join
from fcm import sendMessage
import time

# 얼굴 인식용 haar/cascade 로딩
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# 사용자 얼굴 학습
def train(name):
    data_path = 'faces/' + name + '/'
    # 파일만 리스트로 만듬
    face_pics = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    Training_Data, Labels = [], []

    for i, files in enumerate(face_pics):
        image_path = data_path + face_pics[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # 이미지가 아니면 패스
        if images is None:
            continue
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    if len(Labels) == 0:
        print("There is no data to train.")
        return None
    Labels = np.asarray(Labels, dtype=np.int32)
    # 모델 생성
    model = cv2.face.LBPHFaceRecognizer_create()
    # 학습
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    print(name + " : Model Training Complete!!!!!")

    # 학습 모델 리턴
    return model


# 여러 사용자 학습
def trains():
    # faces 폴더의 하위 폴더를 학습
    data_path = 'faces/'
    # 폴더만 색출
    model_dirs = [f for f in listdir(data_path) if isdir(join(data_path, f))]

    # 학습 모델 저장할 딕셔너리
    models = {}
    # 각 폴더에 있는 얼굴들 학습
    for model in model_dirs:
        print('model :' + model)
        # 학습 시작
        result = train(model)
        # 학습이 안되었다면 패스
        if result is None:
            continue
        # 학습되었으면 저장
        print('model2 :' + model)
        models[model] = result

    # 학습된 모델 딕셔너리 리턴
    return models


# 얼굴 검출
def face_detector(img, size=0.5):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi  # 검출된 좌표에 사각 박스 그리고(img), 검출된 부위를 잘라(roi) 전달


# 인식 시작
def run(models):
    # 카메라 열기
    cap = cv2.VideoCapture(0)

    # 위험인물이 계속 카메라에 있을때 위험알림이 너무많이 전송되는것을 막기위해 10분당 한개로 제한함
    last_warning_time = 0
    current_time = time.time()

    while True:
        # 카메라로 부터 사진 한장 읽기
        ret, frame = cap.read()
        # 얼굴 검출 시도
        image, face = face_detector(frame)
        try:
            min_score = 999  # 가장 낮은 점수로 예측된 사람의 점수
            min_score_name = ""  # 가장 높은 점수로 예측된 사람의 이름

            # 검출된 사진을 흑백으로 변환
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # 위에서 학습한 모델로 예측시도
            for key, model in models.items():
                result = model.predict(face)
                if min_score > result[1]:
                    min_score = result[1]
                    min_score_name = key

            # min_score 신뢰도이고 0에 가까울수록 자신과 같다는 뜻이다.
            if min_score < 500:

                confidence = int(100 * (1 - (min_score) / 300))
                # 유사도 화면에 표시
                display_string = str(confidence) + '% Confidence '
            cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
            
            # 85 보다 크면 동일 인물로 간주
            if confidence > 80:
                # 유사도 85 이상이며 데이터가 위험인물로 분류된 사람일 경우
                if min_score_name == "XMAN" :
                    cv2.putText(image, "Danger!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow('Face Cropper', image)

                    # 마지막으로 보낸 위험신호에서 10분이 지났을경우만 다시 위험신호 전송
                    if current_time - last_warning_time > 600:
                        sendMessage("Danger!", "Dangerous person detected!")
                        last_warning_time = current_time

                # 유사도 85 이상이며 데이터가 위험인물이 아닌 거주자일 경우
                else :
                    cv2.putText(image, min_score_name, (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1,
                                (0, 255, 0),
                                2)
                    cv2.imshow('Face Cropper', image)

            else:
                # 85 이하
                cv2.putText(image, "Unknown", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Face Cropper', image)
                
                # 마지막으로 보낸 위험신호에서 10분이 지났을경우만 다시 위험신호 전송
                if current_time - last_warning_time > 600:
                        sendMessage("Warning!", "Unknown person detected!")
                        last_warning_time = current_time
                        
        except:
            # 얼굴 검출 안됨
            cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', image)
            pass
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    models = trains()
    run(models)
import cv2
from tkinter import *
import os

# 얼굴 저장 함수
face_dirs = 'faces/'

face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



# 얼굴 검출 함수
def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    # 얼굴이 없으면 패스
    if faces is ():
        return None
    # 얼굴이 있으면 얼굴 부위만 이미지로 만들고
    for (x, y, w, h) in faces:
        cropped_face = img[y:y + h, x:x + w]
    # 리턴!
    return cropped_face

# 추가 인물 등록시 ENTER키를 눌러서 정지
# Function to store only faces
def take_pictures(name):
    # Create a folder with that name if it doesn't exist
    if not os.path.exists(face_dirs + name):
        os.makedirs(face_dirs + name)

    # Get the count of existing files in the folder
    files = os.listdir(face_dirs + name)
    count = len(files)

    # Camera ON
    cap = cv2.VideoCapture(0)

    while True:
        # Read a picture from the camera
        ret, frame = cap.read()
        # Face detection in a photo, if a face is detected
        if face_extractor(frame) is not None:
            count += 1
            # Reduce or expand to 200 x 200 size
            face = cv2.resize(face_extractor(frame), (200, 200))
            # convert to black and white
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # save 200x200 black and white photo as faces/face name/userxx.jpg
            file_name_path = face_dirs + name + '/user' + str(count).zfill(4) + '.jpg'
            cv2.imwrite(file_name_path, face)

            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Cropper', face)
        else:
            print("Face not Found")
            pass

        # If you get all 100 face photos or press the enter key, exit
        if cv2.waitKey(1) == 13 or count == 100:
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Colleting Samples Complete!!!')




if __name__ == "__main__":
    # 사진 저장할 이름을 넣어서 함수 호출
    root = Tk()  # GUI선언
    root.title("Face Recognition")
    root.geometry("540x340")

    def btncmd():
        #take_pictures('wbi')
        print(chkclick.get())
        print(chkclick1.get())
        print(chkclick2.get())
        if chkclick.get() == 1 : # 거주민에 등록하고 싶다면
            take_pictures('Residents')
        if chkclick1.get() == 1 :  # 자주 출입하는 인물 (택배기사)
            take_pictures('often')
        if chkclick2.get() == 1 : # 위험인물에 등록하고싶다면
            take_pictures('XMAN')

        print("어느 그룹에 저장?")

    chkclick = IntVar()
    chkbox = Checkbutton(root,  text = " 거주민 ", variable=chkclick)
    chkbox.pack()

    chkclick1 = IntVar()
    chkbox1 = Checkbutton(root, text=" 자주출입하는사람 ", variable=chkclick1)
    chkbox1.pack()

    chkclick2 = IntVar()
    chkbox2 = Checkbutton(root, text=" 위험인물 ", variable=chkclick2)
    chkbox2.pack()

    btn = Button(root, text="GROUP", command=btncmd)
    btn.pack()
    root.mainloop()
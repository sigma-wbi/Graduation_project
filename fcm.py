from pyfcm import FCMNotification

# firebase에서 fcm을 사용하기 위한 서버키를 받아와서 입력
APIKEY = "Your APIKEY "
# android studio에서 device registraion token을 받아와서 입력
TOKEN = "Your TOKEN"

# FCMNotification 클래스의 인스턴스를 만들고 APIKEY를 인수로 전달
push_service = FCMNotification(APIKEY)

# 본문과 제목이라는 두 가지 인수를 사용하는 sendMessage 함수를 정의.  인수는 보내려는 알림의 본문과 제목.
def sendMessage(body, title):
    data_message = {
        "body": body,
        "title": title
    }
    # push_service 인스턴스의 notify_single_device 메서드를 호출하여 TOKEN 및 data_message를 인수로 전달.
    # 또한 message_title 및 message_body 매개변수를 각각 title 및 body 함수 인수로 설정.
    result = push_service.notify_single_device(registration_id=TOKEN, data_message=data_message, message_title=title,
                                               message_body=body)

    print(result)


#sendMessage("test message", "push message")
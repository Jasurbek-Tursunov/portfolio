from requests import get


def send_message_telegram(message):
    try:
        from frontend.models import Configuration
        conf = Configuration.get_solo()
        url = f"https://api.telegram.org/bot{conf.token}/sendMessage?chat_id={conf.chat_id}&parse_mode=HTML&text={message}"
        response = get(url)
        if response.status_code == 200:
            print(f"Success: {message}")
            return True

        else:
            print(f"Error: {response.text}")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False

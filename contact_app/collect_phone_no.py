def collect_phone_no():
    phone_no = input("type your phone number: ").strip()
    while not phone_no.isdigit() or len(phone_no) != 11 or len(phone_no) > 11:
        print('Invalid phone number entry')
        phone_no = input("type your phone number: ").strip()
    return phone_no

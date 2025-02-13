print("Улирлаа оруулна уу 1=Хавар, 2=Зун, 3=Намар, 4=Өвөл")

try:
    season = int(input())  # Хэрэглэгчээс тоо авах
    if season == 1:
        print("Хавар боллоо цэцэглэлээ.")
    elif season == 2:
        print("Зун болсон халуун боллоо.")
    elif season == 3:
        print("Намар болж навч уналаа.")
    elif season == 4:
        print("Өвөл болоод цас орлоо.")
    else:
        print("Буруу утга оруулсан байна!")
except ValueError:
    print("Тоон утга оруулна уу!")


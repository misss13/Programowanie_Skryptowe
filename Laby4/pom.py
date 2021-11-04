metody: earlierDay(), laterDay(), earlierTime() oraz laterTime():

    metody earlierDay() oraz laterDay() przesuwają zajęcia, odpowiednio, o jeden dzień do tyłu lub do przodu, pod warunkiem, że jest to możliwe, tzn. zmodyfikowany termin spełnia założenia wymienione w punkcie 2
    metody earlierTime() oraz laterTime() przesuwają zajęcia, odpowiednio, o duration minut do tyłu lub do przodu, pod warunkiem, że jest to możliwe
    Metody te zwracają true jeżeli operacja przesunięcia powiodła się, w przeciwnym przypadku zwracają false 
    Implementując powyższe metody należy przyjąć, że:

    zajęcia na studiach stacjonarnych  poniedziałku do czwartku w godzinach 8:00-20:00 oraz w piątek w godzinach 8:00 - 17:00
    zajęcia na studiach niestacjonarnych w weekendy w godzinach 8:00-20:00 oraz w piątek w godzinach 17:00 - 20:00 
                                                                                            MON=0 
                                                                                            TUE=1
                                                                                            WED=2
                                                                                            THU=3
                                                                                            FRI=4
                                                                                            SAT=5
                                                                                            SUN=6
# Der Code dient zur Steuerung eines Motorsets,
# das unter folgendem Link erhältlich ist:
# http://bit.ly/schritt-motor


# Benötigten Bibliotheken importieren
import RPi.GPIO as GPIO
import time

try:
    # GPIO einrichten
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # Pins initialisieren
    # Pins des ersten Motors
    pinsA = [11, 12, 13, 15]

    # Pins des zweiten Motors
    pinsB = [16, 18, 22, 7]

    # Pins des ersten Motores als Output festlegen
    for pin in pinsA:
        GPIO.setup(pin, GPIO.OUT, initial = False)

    # Pins des zweiten Motores als Output festlegen
    for pinB in pinsB:
        GPIO.setup(pinB, GPIO.OUT, initial = False)

    # Ansteuerungsmuster initialisieren
    pattern = []
    pattern.append([1,0,0,0])
    pattern.append([1,1,0,0])
    pattern.append([0,1,0,0])
    pattern.append([0,1,1,0])
    pattern.append([0,0,1,0])
    pattern.append([0,0,1,1])
    pattern.append([0,0,0,1])
    pattern.append([1,0,0,1])


    # Variablen auf Startwert setzen
    step = 0

    # Den Nutzer fragen, ob Motor A oder B
    print("Du kannst Motor A oder B ansteuern!")
    print("Bitte gebe, wenn du gefragt wirst, den Motor an den du bentutzen willst")

    # Solange die Antwort keine Gültige ist weiter Fragen
    while True:
        input_motor = input("Motor: ")
        input_motor = input_motor.lower()
        if(input_motor == "a" or input_motor == "b"):
            break;
    # Den Nutzer Fragen, in welche Richtung sich der Motor drehen soll
    print("Du kannst eine Richtung angeben, in der sich der Motor drehen soll")
    print("Der Motor kann sich vorwärts (v) oder rückwärts (r) drehen")

    # Solange die Antwort ungültig ist Frage wiederholen
    while True:
        input_rotation = input("Richtung (v|r): ")
        input_rotation = input_rotation.lower()
        if(input_rotation == "v" or input_rotation == "r"):
            break;

    # Dem Nutzer mitteilen, welcher Motor sich jetzt dreht
    if(input_motor == "a"):
        if(input_rotation == "v"):
            print("Der Motor A dreht sich jetzt vorwärts!")
        else:
            print("Der Motor A dreht sich jezt rückwärts!")

    if(input_motor == "b"):
        if(input_rotation == "v"):
            print("Der Motor A dreht sich jetzt vorwärts!")
        else:
            print("Der Motor A dreht sich jezt rückwärts!")

    # Den Motor drehen vorwärts drehen
    if(input_rotation == "v"):
        while True:
            if(input_motor == "a"):
                for i in range(0, len(pinsA)):
                    GPIO.output(pinsA[i], pattern[step % 8][i])

                step += 1
                time.sleep(0.001)
            else:
                for i in range(0, len(pinsB)):
                    GPIO.output(pinsB[i], pattern[step % 8][i])
                step += 1
                time.sleep(0.001)

    # Den Motor rückwärts drehen
    else:
        while True:
            if(input_motor == "a"):
                for i in range(0, len(pinsA)):
                    GPIO.output(pinsA[i], pattern[step % 8][0-i])

                step += 1
                time.sleep(0.001)
            else:
                for i in range(0, len(pinsB)):
                    GPIO.output(pinsB[i], pattern[step % 8][0-i])
                step += 1
                time.sleep(0.001)
except KeyboardInterrupt:
    for pin in pinsA:
        GPIO.output(pin, GPIO.LOW)
    for pin in pinsB:
        GPIO.output(pin, GPIO.LOW)
    print("Alle Pins aus!")
    print("Auf wiedersehen!")

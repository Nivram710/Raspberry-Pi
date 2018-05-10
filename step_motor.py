# Der Code dient zur Steuerung eines Motorsets,
# das unter folgendem Link erhältlich ist:
# http://bit.ly/schritt-motor


# Benötigten Bibliotheken importieren
import RPi.GPIO as GPIO
import _thread
import time

# Funktion, die die gekürtze Eingabe in Wörter umwandelt
def getRotation(rotation):
    
    # Wenn die ausgewählte Richtung 'v' ist
    if(rotation == "v"):
        
        # wird 'vorwärts' zurück gegeben
        return "vorwärts"
    
    # sonst
    else:
        
        # wird 'rückwärts' zurück gegeben
        return "rückwärts"

# Funktionen, die die Motor-Auswahl in "Wörter" umwandelt
def getMotor(motor):
    
    # Wenn der ausgewählte Motor 'a' ist 
    if(motor == "a"):
        
        # wird 'A' zurück gegeben
        return "A"

    # Wenn der ausgewählte Motor 'b' ist
    elif(motor == "b"):
        
        # wird 'B' zurückgegeben
        return "B"
    
    # sonst
    else:
        
        # wird 'A und B' zurückgegeben
        return "A und B"

# Funktion, die Motor A drehen lässt
def motorA(rotation, step_a):
    
    # Solange der Nutzer das Programm nicht beenden
    while True:
        
        # wird der Motor vorwärts gedreht, wenn es angegeben worden ist
        if(rotation == "v"):
            for i in range(0, len(pinsA)):
                GPIO.output(pinsA[i], pattern[step_a % 8][i])

            step_a += 1
            time.sleep(0.001)

        # Sonst Rückwärts drehen
        else:
            for i in range(0, len(pinsA)):
                 GPIO.output(pinsA[i], pattern[step_a % 8][0-i])

            step_a += 1
            time.sleep(0.001)

# Funktion, die Motor B drehen lässt
def motorB(rotation, step_b):
    
    # Solange der Nutzer das Programm nicht beenden
    while True:
        
        # wird der Motor vorwärts gedreht, wenn es angegeben worden ist
        if(rotation == "v"):
            for i in range(0, len(pinsB)):
                GPIO.output(pinsB[i], pattern[step_b % 8][i])

            step_b += 1
            time.sleep(0.001)

        # Sonst Rückwärts drehen
        else:
            for i in range(0, len(pinsB)):
                 GPIO.output(pinsB[i], pattern[step_b % 8][0-i])

            step_b += 1
            time.sleep(0.001)

try:
    # GPIO einrichten
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # Pins des Motors A festlegen 
    pinsA = [11, 12, 13, 15]

    # Pins des Motors B festlegen
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
    step_a = 0
    step_b = 0

    # Den Nutzer fragen, ob Motor A oder B
    print("Du kannst Motor A und/oder B ansteuern!")
    print("Bitte gebe, wenn du gefragt wirst, den Motor an den du bentutzen willst")
    print("Wenn du beide Motoren Steuern möchtest gebe 'c' ein")

    # Solange die Antwort keine Gültige ist
    while True:

        # Den Nutzer nach einer neuen Antwort fragen
        input_motor = input("Motor: ")

        # Alles klein schreiben, um ein Programmstandard zu haben
        input_motor = input_motor.lower()

        # Wenn eine gültige Antwort eingegeben wurde
        if(input_motor == "a" or input_motor == "b" or input_motor == "c"):
            # wird mit dem Rest des Progrannes weiter gemacht
            break

        
    # Den Nutzer Fragen, in welche Richtung sich der Motor drehen soll
    print("Du kannst eine Richtung angeben, in der sich der Motor drehen soll")
    print("Der Motor kann sich vorwärts (v) oder rückwärts (r) drehen")

    # Solange die Antwort ungültig ist Frage wiederholen
    while True:

        # Wenn nicht beide Motoren angesteuert werden,
        if (input_motor != "c"):

            #  wird nur eine Richtung abgefragt
            input_rotation = input("Richtung (v|r): ")

            # Alles klein schreiben, um ein Programmstandard zu haben
            input_rotation = input_rotation.lower()

            # Wenn eine gültige Antwort eingegeben wurde,
            if(input_rotation == "v" or input_rotation == "r"):
                # wird mit dem Rest des Programmes weiter gemacht 
                break

        # Wenn beide Motoren angesteuern werden,
        else:

            # wird erst nach der Richtung für Motor A gefragt
            input_rotation_a = input("Richtung Motor A: ")            

            # Alles klein schreiben, um ein Programmstandard zu haben
            input_rotation_a = input_rotation_a.lower()
            
            # Wenn die Antwort für Motor A gültig ist,
            if(input_rotation_a == "v" or input_rotation_a == "r"):

                # Solange die Antwort für B ungültig ist
                while True:
                    #wird nach der Richtung von B gefragt
                    input_rotation_b = input("Richtung Motor B: ")
                    input_rotation_b = input_rotation_b.lower()

                    # Wenn die Antwort für B gültig ist,
                    if(input_rotation_b == "v" or input_rotation_b == "r"):
                        #wird mit dem Rest des Programmes weiter gemacht
                        break
                break
            

    # Dem Nutzer mitteilen, welcher Motor sich jetzt dreht
    if(input_motor == "c"):
        print("Motor {} drehen sich jetzt {} / {}".format(getMotor(input_motor), getRotation(input_rotation_a), getRotation(input_rotation_b)))
    else:
        print("Motor {} dreht sich jetzt {}".format(getMotor(input_motor), getRotation(input_rotation)))

        
    # Wenn Motor A angeben wurde
    if(input_motor == "a"):
        # rufen wir die Funktion auf, die Motor A drehen lässt
        motorA(input_rotation, step_a)

    # Wenn Motor B angegeben wurde
    elif(input_motor == "b"):
        # Bis der Nutzer das Programm beendet
        while True:
            # rufen wir die Funktion auf, die Motor B drehen lässt
            motorB(input_rotation, step_b)

    # Wenn 'c' (beide Motoren) angeben wurde(n)
    else:
        # Wird ein Thread mit der Funktion Motor A in die gewünschte Richtung drehen zu lassen gestartet 
        _thread.start_new(motorA, (input_rotation_a, step_a))
        
        # die Funktion, um Motor B in die gewünschte Richtung drehen zu lassen, aufrufen
        motorB(input_rotation_b, step_b)
        

# Wenn 'Strg + C' gedrückt wird beide Motoren ausschalten
# und Nutzerbestätigung ausgeben
except KeyboardInterrupt:
    for pin in pinsA:
        GPIO.output(pin, GPIO.LOW)
    for pin in pinsB:
        GPIO.output(pin, GPIO.LOW)
    print("Alle Pins aus!")
    print("Auf wiedersehen!")
    exit()

# Leere Liste für Tupel erstellen
gueltige_tupel = []
x = 0
# Alle möglichen Kombinationen von Werten für a, b, c, d, e probieren (optimierung vorherige Varible +1 als Minimum: >59000 Versuche -> 126 Versuche)
for a in range(1, 10):
    for b in range(a+1, 10):
        for c in range(b+1, 10):
            for d in range(c+1, 10):
                for e in range(d+1, 10):
                    x+=1
                    #print(x)
                    
                    # a^e berechnen
                    links = a**e
                    
                    # (bd + 1)c berechnen
                    rechts = (b*d + 1) * c
                    
                    # Prüfen ob die Gleichung stimmt
                    if links == rechts:
                        # Tupel der Liste hinzufügen
                        gueltige_tupel.append((a, b, c, d, e))

# Gültige Tupel ausgeben
print(gueltige_tupel)
print(str(x) + " Versuche")
# def pirmais(skaitlis1, skaitlis2):
#     reiz= skaitlis1*skaitlis2
#     if reiz <=1000:
#         return reiz 
#     return skaitlis1+skaitlis2

# def otrais(gals):
#     ieprieksejais = 0
#     for esosais in range(gals+1):
#         print(f"esošais- {esosais}, ieprieksejais skaitlis-{ieprieksejais}, to summa= {esosais+ieprieksejais}")
#         ieprieksejais = esosais
#     return    
# #otrais(10)

# def tresais():
#     teksts = input("lūdzu ievadi tekstu")
#     for i in range (0,len(teksts),2):
#         print(teksts[i])
# tresais()

# def ceturtais():
#     teksts = input("lūdzu ievadi tekstu  : ")
#     skaits = int(input("Cik pirmos burtus japazaude? : ")) 
#     print(teksts[skaits:])
#     return 
# ceturtais()

def devitais(skaits):
    for cipars in range(1,skaits+1):
        for i in range(cipars):
            print(cipars, end="")
    return
devitais(9)






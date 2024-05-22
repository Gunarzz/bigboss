def ierakstit(teksts):
    fails = open ("teksts.txt", "w", encoding = "utf-8" ) # r - read; w - write; a - append
    fails.write(teksts + "\n")
    fails.close()

# ierakstit("wsg boy")

def pierakstit_klat (teksts):
    fails = open ("teksts.txt", "a", encoding = "utf-8")
    fails.write(teksts+ "\n")
    fails.close()

  #  pierakstit_klat("es esmu chill")
    
def nolasit_visu():
    fails = open("teksts.txt", "r", encoding="utf-8")
    teksts = fails.read()
    fails.close()
    return teksts

 # print(nolasit_visu())

# def dabut_rindinas():
#     fails = open ("teksts.txt", "r", encoding="utf-8")
#     rindas = fails.readlines()
#     return rindas

def dabut_rindinas():
    fails = open ("teksts.txt", "r", encoding="utf-8")
    rindas = fails.readlines()

    for i in range(len(rindas)):
        rindas[i] = rindas[i].strip()

    fails.close()
    
    return rindas 


# saraksts = dabut_rindas()
# print(saraksts)

ierakstit("toms, https://i.kym-cdn.com/entries/icons/original/000/048/633/Screenshot_2024-02-27_at_1.49.23_PM.png")
pierakstit_klat("stankevics,https://helios-i.mashable.com/imagery/articles/05VLY7Lzn0CqhARsG57bEE8/hero-image.fill.size_1248x702.v1661452017.png")
pierakstit_klat("top,https://media.ed.edmunds-media.com/mercedes-benz/gle-class/2024/oem/2024_mercedes-benz_gle-class_4dr-suv_amg-gle-53_fq_oem_1_815.jpg")
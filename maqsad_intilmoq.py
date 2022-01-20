# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 14:12:49 2021

@author: user
import.math.sin():
"""

# Assalomu alaykum bugunda boshlab haqiiqiy dasturchiday harakat qilamiz
# Insha Allah bu yilda hech qachon to'xtamaymiz.data:08.01.2022
# 1-darsimiz lugatlar bilan ishlash:
# ismlar=['Abubakr','Muhammad','Mavlon']  
# print(f"'Assalomu Alaykum'  {ismlar[0]}  'bugun dasr bormi?'")

# print("dostim" +  ' '+ ismlar[0] +' ' +  "bugun gaplasha alomizmi?")
# sonlar=[12,23,48,-5,-54]
# print(sonlar)
# sonlar[0]=21
# sonlar[2]=84
# sonlar.append(26)
# sonlar.insert(4,43)
# sonlar.pop(3)
# del sonlar[1]
# print(sonlar)
# t_shaxslar=['Imom Buxoriy','Abubakr','Umar raziyallohu anhu','Ali raziyallohu anhu']
# z_shaxslar=['bel gets','ilon mask','Abdulloh damla','muhammad S.A.V']
# print(f"men {t_shaxslar[1]} bilan gaplashishni juda xoxlayman",
#       f" va yana tushlarimda payg'ambarimiz {z_shaxslar[-1].title()} korishishbi va suhbatlashishni hohlardim  ")
# friends=[]
# friends.append('Mavlon')
# friends.append('ilsom')
# friends.append('behruz')
# friends.append('Abubakr')
# friends.append('sanjar')
# print(friends[2].title())
# friends.remove('Mavlon')
# print(friends)
# friends.remove('behruz')
# mehmonlar=[]
# friends2=friends.pop(0)
# mehmonlar.append(friends2)
# print(mehmonlar)
# bugungi birinchi dars tugadi 
 
# dars royxat darsimizni davomi 2-daes

  # 1-topshiriq
# davlatlar=['misr','madina','makka','malayziya','uzbekiston']
# print(davlatlar)
# print(len(davlatlar))
# #davlatlar.sort()
# #print(davlatlar)
# print(sorted(davlatlar))
# print(sorted(davlatlar,reverse=True))
# print(davlatlar)
# davlatlar.reverse()
# print(davlatlar)
  
 # 2-topshiriq
# sonlar=list(range(120,1200,2))
# print(sonlar)
# yigindi=sum(sonlar)
# print(yigindi)
# katta=max(sonlar)
# kichik=min(sonlar)
# print(katta-kichik)
# print(len(sonlar))
# print(sonlar[:20])
# print(sonlar[220:241])
# print(sonlar[520:])

  # 3- topshiriq
  
# toam=[]
# toam.append('mastava')
# toam.append('halim')
# toam.append('kabob')
# toam.append('osh')
# toam.append('norin')
# print(toam)
# nonushta=toam[:]
# print(nonushta) 
# nonushta.remove('halim')
# nonushta.remove('kabob')
# nonushta.remove('norin')
# nonushta.append('manti')
# nonushta.append('somsa')
# print(nonushta)
# nonushtam=tuple(nonushta)
# print(nonushtam)
# nonushtam[0]='qaymoq va non'
# print(nonushtam)

 #shu bilan royxat mavzudagi darsimiz yakunlandi
 
 #  3- dars for sikl operatori
# 1 topshiriq
# ismlar=['abdumalik','Mavlon','Alisher','Abubakr','Behruz']
# for ism in ismlar:
#     print(f"do'stim {ism.title()} sizni nohorgi oshga taklif qilaman ")
#     print("xurmat bilan Brediyevla olasi")
# print("xush kelibsiz aziz mehmonlar")
# print(f" kod {len(ism)} marta takrorlandi")#kod nechi marta takrorlangani 
#                                            # korsatadi 
                                           
 # 2- topshiriq 10 dan 100 ga bolgan  toq sonlar royxatini chiqaring 
 # har birini 3 chiqaruvchi kod yozing
# t_sonlar=[]
# for son in list(range(11,100,2)):
   
#     print(f" {son} ning kubi {son**3}")
#     t_sonlar.append(son)
# print(t_sonlar)

 # 3- topshiriq.
# kinolar=[]
# for n in range(5):
#     kinolar.append(input(f"{n+1}- yoqtirgan kinagizni kiriting:"))
# print(kinolar)
    
# if sikl operatori haqida bugungi darsimiz
  
 # 1- topshiriq
# yangi_cars=['toyota','mazda','hyundai','gm','kia']
# for  cars in yangi_cars:
#     if cars=='gm':
#         print(cars.upper())
#     else:   
#         print(cars.title())

 # 2- topshiriq: != teng emas holat uchun
# y_cars=['toyota','mazda','hyundai','gm','kia']  
# for cars in y_cars:
#     if cars !='gm':
#         print(cars.title())
#     else:
#         print(cars.upper())
# login=input("foydalanuvchini_ismi:")
# if login == 'admin':
#    print("xush kelibsiz, ",login.title())
# else:
#    print(f"xush kelibsz {login.title()}")       
 
# 3-toppshiriq
# print('ikkita son liriting')
# son1=int(input('y ='))
# son2=int(input('x ='))
# if son1==son2:
#     print('sonlar teng')
# son=int(input("istalgan sonni kiring:\n"))
# if son > 0:
#   print(f"{son**0.5}")
# else:
#   print('musbat son kiriting')
 # 4- topshiriq 
# son=int(input("son kiriting:\n"))
# if (son%2)==0:
#     print("juft son")
# else:
#    print('toq son') 

# 4- topshiriq:

# yosh=int(input("yoshigiz nechida: "))
# if (yosh<=4 or yosh>=60):
#     price=0
# elif yosh<=18:
#     price=100000    
# elif yosh>=18:
#     price=20000
# print(f"muzeyga kirish siz uchun {price}")

# 5- topshiriq:

# son1=int(input("son kiriting: "))
# son2=int(input("son kiriting: "))
# if son1==son2:
#      qiymat='teng'
# elif son1>son2:
#      qiymat='son1 katta son ikkidan '
# elif son1<son2:
#      qiymat='son1 kichik son2 dan'  
# print(f"siz kiritgan son {qiymat} ")
   
# 5- topshiriq:
# mahsulotlar=["yog'",'makaron','mosh','kartoshka','piyoz','sabzi','gosht']
# savat=[]
# savat.append(input('mahsulot kiriting: '))
# savat.append(input('mahsulot kiriting: '))
# savat.append(input('mahsulot kiriting: '))
# savat.append(input('mahsulot kiriting: '))
# savat.append(input('mahsulot kiriting: '))
# print(savat)
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f" {mahsulot} mahsulot dikonimizda bor")
#         else:
#             print(f" bizda {mahsulot}  mahsuloti yoq")
# else:
#   print("savat bo'sh")            
# print(mahsulot)

# 6- topshiriq:
# mahsulotlar=["yog'",'makaron','mosh','kartoshka','piyoz','sabzi','gosht']
# savat=[]
# for n in range(5):
#     savat.append(input(f"{n+1} - mahsulotni kiriting: "))
    
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"dokonimizda {mahsulot} bor")
#     else:
#         print(f"dokonimizda {mahsulot} yoq ")

# 7 topshriq: haqiqatdan bu misol men uchun qiyin boldi


# mahsulotlar=["yog'",'makaron','mosh','kartoshka','piyoz','sabzi','gosht']
# savat=[]
# for n in range(5):
#      savat.append(input(f"{n+1} - mahsulotni kiriting: "))
     
# bor_mahsulot=[]
# mavjud_emas=[]
# for mahsulot in savat:
#   if mahsulot in mahsulotlar:
#     bor_mahsulot.append(mahsulot)
#   else:
#       mavjud_emas.append(mahsulot)
# if  mavjud_emas:
#     print(f"dokonimizda quyidagi mahsulotlar yoq:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#    print("siz so'ragan barcha mahsulotlar dokonimizda mavjud")        
    
  # 8- misol :
# foydalanuvchilar=['alisher@12','maqsud123','rustam99','abubakr00','mirhosil55']
# login=input("login kiriting: ")
# if login in foydalanuvchilar:
#         print("login band, yangi login tanlang!")
# else:
#    print(f"xush kelibsiz {login}")

# 9- topshiriq:
# son=int(input("birorta son kiriting:"))
# for n in range(2,11):
#     if not (son%n):
#         print(f" {son} soni {n} ga qoldiqsiz bolinadi")

#  yangi dars lug'atlar bilan ishishlash:
    
# 1- topshiriq:
# otam={"ismi":'Muhammadi','yoshi':'56','kasbi':'harbiy'}
# print(otam['ismi'])
# otam["yashash_joyi"]="qumqo'rg'on"
# otam["xulqi"]='samimiy'
# print(otam)
# print(f"{otam['ismi']}, yoshi:{otam['yoshi']}")

 # 2- topshiriq:
# lugat={'use':'foydalanmoq',
#        'hope':'umid qilmoq',
#        'day':'kun',
#        'brain':'miyya'}
# soz=input("soz kiriting: ")

# if soz in lugat:
#     print(f"{lugat[soz]}")
# else:
#      print("bunday so'z mavju d=emas")
 
 # bunda get( ) funksiyadan foydalandik:
# lugat={'use':'foydalanmoq',
#        'hope':'umid qilmoq',
#        'day':'kun',
#        'brain':'miyya'}
# soz=input("soz kiriting: ")
# soz=lugat.get(soz,"bunday so'z mavjud emas")
# print(f"{soz}")
# talaba={
#      'ism':'alijon',
#      'familya':'shamsiyev',
#      'yosh':22,
#      'fakultet':'matematika',
#      'kurs':4
#      }
# for keys,vosue in talaba.items():
#     print(f"key: {keys}")
#     print(f"vosue: {vosue}")

# 1-topshiriqlar:
# lugat={
#        'hope':'umid qilmoq',
#        'mind':'qarshi emasman',
#        'egree':'qoshilaman',
#        'gun':'miltiq',
#        'show':'korsatmoq',
#        'pay':'tolamoq',
#        }
# for k,q in sorted(lugat.items()):
#     #print(f"{k.title() }: ")
#     #print(f"{q.title()}")
#     print(f"{k.title()} so'zini manosi: {q}")
    
# 2- topshiriq:
# davlatlar={
#     'rassiya':'maskva',
#     'italya':'rim',
#     'ispaniya':'madrid',
#     'uzbekiston':'toshkent',
#     'avfgo\'niston':'qabul',
#     'turkiya':'anqara'
#     }
# davlat=input("istalgan davlatni kiriting: ")
# davlat=davlatlar.get(davlat, f"kechirasiz bunday  {davlat} davlati yoq")
# print(davlat.title())

# 3- topshriq:
# menyu={
#        'kabob':'18000',
#        'norin':'20000',
#        'halim':'20000',
#        'osh':'18000',
#        'somsa':'10000',
#        'manti':'4000'
#        }
# print(" 3 ta taom kiriting")
# buyurtmalar=[]
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1} - buyurma: "))
# for buyurtma in buyurtmalar:
#      if buyurtma in menyu:
#          print(f"{buyurtma.title()} {menyu[buyurtma]} so'm")
#      else:
#         print(f"kechirasiz, bizda {buyurtma} yoq")

# men uchun har darsda bir yangilik bor bundan hursadman
 
 # nestining : lug'at ichida royxat
# olimlar0={
    
#  'olim0':{
#       'ism':'Imom Buxoriy',
#       't_joy':'Buxora shaxri',
#       'ijod':'xadisshunos',
#       'asarlar':['al- jome as sahih','al- adab']
#       },
#  'olim1':{
#       'ism':'Ibin sino',
#       't_joy':'samarqand',
#       'ijod':'tib ilmini olimi',
#       'asarlar':['tib qonunlar 4 jild','fiqhul akbar']
#       },
#  'olim2':{
#       'ism':'xasan basriy',
#       't_joy':'Buxora shaxri',
#       'ijod':'xadisshunos',
#       'asarlar':['adab','sulh']}
# }
# # olimlar=[olim0,olim1,olim2]
# # for olim in olimlar:
# #     print(f"{olim['ism']} {olim['t_joy']} {olim['ijod']} {olim['asarlar']}")
# for ism,info in olimlar0.items():
#     print(f"\n{ism.title()} :{info['ism']} ")
    
#     for asar in info['asarlar']:
#         print(asar.title(),end=' ')

 # bugungi darsimiz while sikl operatori:
# 1- topshiriq:
# print("yaxshi ko'rgan kitoblarizni kiriting:")
# savol=("kitob kiriting: ")
# savol+=("to'xtatish uchun 'stop' deb yozing ")
# qiymat=''
# kutubxona=[]
# while qiymat !='stop':
#     qiymat=input(savol)
#     if qiymat!='stop':
#         print(qiymat.title(), end='')
#         kutubxona.append(qiymat.title())
# print(kutubxona)    

# 2- topshiriq: 1- usul
# print(" muzeyga xush kelibsiz")
# savol=("yoshingizni kiriting: ")
# savol+=("toxtatish uchun 'exit' deb yozing ")
# yosh=''
# while yosh !='exit':
#     yosh=(input(savol))
#     if yosh !='exit':
#      yosh=int(yosh)
    
#      if yosh<=7:
#         narx=2000
#      elif (yosh>7 and yosh<=18):
#         narx=300
#      elif(yosh>18 and yosh<=65):
#         narx=10000
#      elif yosh>65:
#         narx='free'
    
#      print(f" agar {yosh}-yosh bolsa {narx}")       
   # 2- usul    
# savol=("yoshingizni kiriting: ")
# savol+=("toxtatish uchun 'exit' deb yozing ")
# yosh=''
# while yosh !='exit':
#     yosh=(input(savol))
#     if yosh !='exit':
#      yosh=int(yosh)
    
#      if yosh<=7:
#         narx=2000
#      elif (yosh>7 and yosh<=18):
#         narx=300
#      elif(yosh>18 and yosh<=65):
#         narx=10000
#      elif yosh>65:
#         narx='free'
#     if yosh=='exit':
#         break
  
#     print(f" agar {yosh}-yosh bolsa {narx}")  
   
  # 3- usuli
# savol=("yoshingizni kiriting: ")
# savol+=("toxtatish uchun 'exit' deb yozing ")
# ishora=True
# while ishora:
#      yosh=(input(savol))
#     #if yosh !='exit':
     
#      if yosh=='exit':
#         ishora=False
#         break
#      else:
#         yosh=float(yosh)
#         if yosh<=7:
#          narx=2000
#         elif (yosh>7 and yosh<=18):
#          narx=300
#         elif(yosh>18 and yosh<=65):
#          narx=10000
#         elif yosh>65:
#          narx='free'
#      print(f" agar {yosh}-yosh bolsa {narx}")         

 # 2- mazu while sikl haqida 
# 1- topshriq:
#buyurtmalar=[]
# n=1
# while True:
#      savol=(f"{n}-buyurtmani bering: ")
#      buyurtma=input(savol)
#      buyurtmalar.append(buyurtma)
#      javob=input("agar yana buyurtma beraszmi? (ha\yo'q)")
#      if javob=='ha':
#       n+=1
#      else:
#       break
#  #        print("xaridiz uchun raxmat!!!")

#  #       print(buyurtma)
  
#  # 2 - topshiriq
# e_bozor={}
# ishora=True
# while ishora:
#      mahsulot=input("mahsulot kiriting: ")
#      narx=input(f"{mahsulot} ni narxini kiriting: ")
#      e_bozor[mahsulot]=narx
#      javob = input("yana mahsulot olaszmi? (ha\yo'q) ")
    
#      if javob=="yo'q":
#          ishora=False
         
# #for mahsulot,narx in e_bozor.items():
# # print(f"{mahsulot} {narx} - narxda")

# if buyurtmalar:
#     for buyurtma in buyurtmalar:
#      if buyurtma in e_bozor:
#          print(f"{buyurtma} {narx}- narxda")
#     else:
#         print(f"bizda bunday {buyurtma} yoq")

 # funksiya mavzusiga keldik :
     # 1- topshiriq:
# def malumot_ber(ism,t_yil):
#     print(f"{ism.title()} {2022-t_yil}")
    
# malumot_ber("abdulaziz",1998)
 
# 2- topshiriq:
# def hisobla(son):
#     print(f" {son} ning kvadrati :{son**2} va kubi: {son**3}")
# hisobla(9)
# hisobla(18)
# hisobla(0.1)
  # 3- topshiriq:
# def hisobla(son):
#     if son%2==0:
#      print(f"{son} - juft son")
#     else:
#         print(f"{son} - toq son ")
# hisobla(6)
# hisobla(5)

 # 4 - topshiriq:
# def taqosla(min,max):
#    if min==max:
#         print(f"{min} = {max}")
    
# taqosla(34,34)
# taqosla(23,32)

# def hisobla(son):
#    for n in range(2,11):
#     if not son%n:
#          print(f"{son}  soni {n} ga qoldiqsiz bolinadi")
# hisobla(20)
# hisobla(18)
# hisobla(11)

# 2-qism funksiya :
# def malumot_toldir(ism,familya,t_yil,t_joy,e_pochta,tel_raqam):
#     nusxa={
#         'ism':ism,
#         'familya':familya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'e_pochta':e_pochta,
#         'tel_raqam':tel_raqam
#         }
  
#     return nusxa
# talaba1=malumot_toldir('alisher','berdiyev',1998,"qumqorg'on tuman",'alish123',23)
# talaba2=malumot_toldir('ali','berdiyev',1999,"qumqorg'on tuman",'alish1233',29)    
# talabalar=[talaba1,talaba2] 
# for talaba in talabalar:
#     print(f"{talaba['ism']} {talaba['familya']} {talaba['t_yil']}")
    
# def malumot_toldir(ism,familya,t_yil,t_joy,e_pochta,tel_raqam):
#     nusxa={
#         'ism':ism,
#         'familya':familya,
#         't_yil':t_yil,
#         't_joy':t_joy,
#         'e_pochta':e_pochta,
#         'tel_raqam':tel_raqam
#         }
#     return nusxa
# malumotlar=[]
# while True:
#     print("malumotlarni kiriting" ,end='')
#     ism=input("ism: ")
#     familya=input("familya: ")
#     t_yil=input("tug'ulgan yil: ")
#     t_joy=input("t_joyni kiriting: ")
#     e_pochta=input("email kiriting: ")
#     tel_raqam=input('raqam kiriting:')
#     malumotlar.append(malumot_toldir(ism,familya,t_yil,t_joy,e_pochta,tel_raqam))
#     javob=input("yana malumot qoshasizmi (ha\yoq)")
#     if javob=='yoq':
#         break
# for ism in malumotlar:
#         print(f"{ism['ism'].title()} {ism['familya'].title()} {ism['tel_raqam']}")

# def taqosla(x,y,z):
#     katta=max(x,y,z)
#     return katta
# son=taqosla(12,21,31)
# print(f"eng kattasi {son}")

# def hisobla(radius,pi=3.14):
#  aylana={
#         "radius":radius,
#         "diametr":radius*2,
#         "yuz":radius*pi*2}
#  return aylana

# aylana=hisobla(4)
# print(aylana)

# def tub_son_aniqla(min,max):
#     tub_sonlar=[]
#     for n in range(min,max+1):
#      tub=True
#      if (n==1):
#         tub=False
#      elif(n==2): 
#         tub=True
#     else:
#       for x in range(2,n):
#        if (n%x==0):
#          tub=False
#     if tub:
#         tub_sonlar.append(n)
#     return tub_sonlar
# m=tub_son_aniqla(1,21)

 # funksiuya va qator:
# 1-topshiriq:
# def kopaytr(*sonlar):
#   kopaytma=1
#   for son in sonlar:
#       kopaytma*=son
#   return kopaytma
#print(kopaytr(3,4,5))

# def malumotlar(ism,familya,**talabar):
#     talabar['ism']=ism
#     talabar['familya']=familya
#     return talabar
# talaba1=malumotlar('alisher','temirov',kurs=3)
# talaba2=malumotlar('abubakr','shavqatulayev',yonalish='matematika')
# talabalar_mal=[talaba1,talaba2]
# print(f"\n {talabalar_mal},")
  
# modullar mavzusi/:
    
# def avto_info(kampaniya,model,rangi,yili,karobka,narxi):
#     avto={
#         'kampaniya':kampaniya,
#         'model':model,
#         'rang':rangi,
#         'yil':yili,
#         'karobka':karobka,
#         'narx': narxi
#         }
#     return avto
# avtolar=[]
# while True:
#     print("malumotlarni toldiring", end='')
#     kampaniya=input('kampaniya: ')
#     model=input('modeli: ')
#     rangi=input("ranggi: ")
#     yili=input('yili: ')
#     karobka=input("karobka: ")
#     narxi=input("narxi: ")
#     avtolar.append(avto_info(kampaniya,model,rangi,yili,karobka,narxi))
#     javob=input("yana malumot qoshasizmi? (ha\yoq) ")
#     if javob=='yoq':
#      break
# for avto in avtolar:
#  if avto['narx']:
#      narxi=avto['narx']
#  else:
#    narxi='malumot yoq' 

     
#  print(f"{avto['rang']} {avto['model']} {avto['kampaniya'].upper()}, {karobka} karobpa ")
     
def malumot(ism,familya,*t_yil):   
  talaba={
      'ism':ism,
      'familya':familya,
      't_yil':t_yil}
  return talaba 
def mal_print(malumot):
    print(f"{malumot}")
 
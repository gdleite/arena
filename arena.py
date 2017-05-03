import random

def dado(n):
  n=random.randint(1,n)
  if habilidade == 'Sorte':
    n+=1
  print('Rolou um dado: ',n,'!')
  return n

def cpu_cansado():
  acoes=['Defesa']*3+['Magia']*3+['Esperar']*4
  i=acoes[random.randint(0,9)]
  return i
  
def cpu_AI():
  acoes=['Defesa']*5+['Magia']*3+['Ataque']*10+['Esperar']*2
  i=acoes[random.randint(0,19)]
  return i
  
def ataque(ação_cpu):
  if ação_cpu=='Esperar':
    hp=0
    if arma=='Machado':
      stamina_cpu=1
      stamina=0
      hp_cpu=-dado(6)
    elif arma=='Lança':
      stamina_cpu=1
      stamina=-2
      hp_cpu=-dado(9)
    else:
      stamina_cpu=1
      stamina=-1
      hp_cpu=-dado(7)
  elif ação_cpu=='Defesa':
    hp=0
    if arma=='Machado':
      stamina_cpu=1
      stamina=-1
      hp_cpu=-dado(4)
    elif arma=='Lança':
      stamina_cpu=1
      stamina=-3
      hp_cpu=-dado(6)
    else:
      stamina=-2
      stamina_cpu=1
      hp_cpu=-dado(5)
  elif ação_cpu=='Ataque':
    hp=-random.randint(1,4)
    if arma=='Machado':
      stamina_cpu=-1
      stamina=-1
      hp_cpu=-dado(5)
    elif arma=='Lança':
      stamina_cpu=-1
      stamina=-2
      hp_cpu=-dado(7)
    else:
      stamina=-1
      stamina_cpu=-1
      hp_cpu=-dado(6)
  else:
    if raca=='Mago':
      hp=-random.randint(1,5)
    else:
      hp=-random.randint(1,8)      
    if arma=='Machado':
      stamina_cpu=0
      stamina=-1
      hp_cpu=-dado(6)
    elif arma=='Lança':
      stamina_cpu=0
      stamina=-2
      hp_cpu=-dado(9)
    else:
      stamina=-1
      stamina_cpu=0
      hp_cpu=-dado(7)
      
  return hp, hp_cpu, stamina, stamina_cpu,0
  
def magia(ação_cpu):
  stamina=0
  if ação_cpu=='Esperar':
    stamina_cpu=1
    if raca=='Humano':
      hp=dado(8)
      hp_cpu=0
    elif raca=='Ogro':
      hp=0
      hp_cpu=-dado(8)
    else:
      stamina=dado(4)
      hp=0
      hp_cpu=0
  elif ação_cpu=='Defesa':
    stamina_cpu=1
    if raca=='Humano':
      hp=dado(8)
      hp_cpu=0
    elif raca=='Ogro':
      hp=0
      hp_cpu=-dado(4)
    else:
      stamina=dado(4)
      hp=0
      hp_cpu=0
  elif ação_cpu=='Ataque':
    stamina_cpu=-1
    if raca=='Humano':
      hp=dado(8)-random.randint(1,5)
      hp_cpu=0
    elif raca=='Ogro':
      hp=-random.randint(1,5)
      hp_cpu=-dado(8)
    else:
      stamina=dado(4)
      hp=-random.randint(1,5)
      hp_cpu=0
  else:
    stamina_cpu=0
    if raca=='Humano':
      hp=dado(8)-random.randint(1,8)
      hp_cpu=0
    elif raca=='Ogro':
      hp=-random.randint(1,8)
      hp_cpu=-dado(8)
    else:
      stamina=dado(4)
      hp=-random.randint(1,5)
      hp_cpu=0
    
  return hp, hp_cpu, stamina, stamina_cpu, -1
  


def personagem():
  print('MONTE SEU GUERREIRO\n')
  racas=['Ogro','Humano','Elfo']
  raca=input('Escolha sua raça: (Humano/Ogro/Elfo)')
  while raca not in racas:
    raca=input('Raça invalida, escolha: (Humano/Ogro/Elfo)')
  proeficiencias=['Machado','Espada','Lança']
  proeficiencia=input('Escolha sua arma: (Machado/Espada/Lança)')
  while proeficiencia not in proeficiencias:
    proeficiencia=input('Arma invalida, escolha: (Machado/Espada/Lança)')
  habilidades=['Magia','Sorte','Força']
  habilidade=input('Escolha sua habilidade: (Magia/Força/Sorte)')
  while habilidade not in habilidades:
    habilidade=input('Habilidade invalida, escolha: (Magia/Força/Sorte)')
  
  return raca, proeficiencia, habilidade

print('------------------------------------------------------')
print('--------------- BEM VINDO A ARENA   ----------------- ')
print('------------------------------------------------------\n')

def apresentaçao():
  if raca=='Humano':
    nomes=['Jusher Zinel','Hukhar Dunnan','Gae Stonedraft','Brangilm Voidstream','Fidgem Glutsk','Ram Grardodz','Trumem Mournpeak','Tarth Softridge','Vijejek Hukdendrild','Nothu Nikdut','Rolvonrilm Gakagaru','Jondausk Tromyerga','Liow Daim Daim','Zie Waong Waong','Feantildel Zuldemu','Ridrol Gonornu']
  elif raca == 'Ogro':
    nomes=['Progdush','Erork','Pogdish','Erirag','Vrunak','Krirbag','Raadush','Piol','Gridush','Raol','Kigdish','Ponk','Pagor','Gruunak','Guuk','Gadish','Vigar','Grur','Bogash','Grugash','Boshnak','Vrag','Vrishnak']
  else:
    nomes=['Revgalad','Neurdur','Arpantien','Eihasyonion','Dramollien','Eglerion','Saelion','Hothien','Daugion','Airathil']
  i=random.randint(0,len(nomes))
  
  print('\n"...Os portões se abrem revelando o sol que queima seus olhos e a platéia aplaude em chamas a sua chegada. Seu Nome é {}, o {}.'.format(nomes[i],raca))
  if habilidade=='Força':
    sumario1='Sua infância foi repleta de bons momentos, sua família, por ter raízes no exercito da cidade, era conhecida por todos ali. Você treinava diariamente na esperança de se equivaler a seu irmão que fora para a capital defender o reino da invasão de um reino inimigo."'
  elif habilidade=='Magia':
    sumario1='Como todo bom aprendiz de feiticeiro, você passou a infância enfiado nos livros e assim conseguiu o dominio dos elementos que lhe garantem proteção."'
  else:
    sumario1='Correndo de guardas, roubando bolsos e dormindo em becos assim pode se resumir a sua juventude orfã na capital. A maioria dos garotos com que você convivia ja foram mandados para a prisão, mas você peculiarmente tem o dom de sempre estar um passo a frente da polícia."'
  print(sumario1)
  #fazer resto da historia#
  print('')
  
def combate():
  turno=0
  stamina=2
  stamina_cpu=1
  hp=30
  hpcpu=30
  if raca=='Mago':
    mana=3
  else:
    mana=1
  ações=['A','M','D','E','a','m','d','e']
  while hpcpu >= 0 and hp >= 0:
    ação=input('(A)TACAR, (M)AGIA, (E)SPERAR ou (D)EFESA?')
    while ação not in ações:
      ação=input('(A)TACAR, (M)AGIA, (E)SPERAR ou (D)EFESA?')
    while stamina <=0 and (ação=='A' or ação=='a'):
      ação=input('Não tem energia suficiente para atacar, (D)EFESA, (E)SPERAR ou (M)AGIA?') 
    if stamina_cpu <= 0:
      ação_cpu=cpu_cansado()
    else:
      ação_cpu=cpu_AI()
      
    if ação=='A' or ação=='a':
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=ataque(ação_cpu)
    elif ação=='M' or ação=='m':
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=magia(ação_cpu)
      
    hp+=hpchange
    stamina+=stachange
    hpcpu+=hp_cpuchange
    stamina_cpu+=sta_cpuchange
    mana+=mana_change
         
raca,arma,habilidade=personagem()
apresentaçao()
combate()

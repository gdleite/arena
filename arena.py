import random

def dado(n):
  n=random.randint(1,n)
  if habilidade == 'Sorte':
    n+=1
  return n

def esquiva():
  chance=['1']*9+['0']
  i=chance[random.randint(0,9)]
  return i

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
      stamina_cpu=0
      stamina=-1
      hp_cpu=-dado(3)
    elif arma=='Lança':
      stamina_cpu=0
      stamina=-3
      hp_cpu=-dado(5)
    else:
      stamina=-2
      stamina_cpu=0
      hp_cpu=-dado(4)
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
    if habilidade=='Magia':
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

def espera(ação_cpu):
  if ação_cpu=='Ataque':
    stamina_cpu=-1
    hp=-dado(7)
  elif ação_cpu=='Defesa':
    stamina_cpu=0
    hp=0
  elif ação_cpu=='Esperar':
    stamina_cpu=1
    hp=0
  else:
    stamina_cpu=0
    if habilidade=='Magia':
      hp=-dado(5)
    else:
      hp=-dado(8)
  return hp ,0, 1, stamina_cpu, 0

def defesa(ação_cpu):

  if ação_cpu=='Esperar':
    stamina_cpu=0
    hp=0
  elif ação_cpu=='Defesa':
    stamina_cpu=0
    hp=0
  elif ação_cpu=='Ataque':
    stamina_cpu=-2
    hp=-dado(4)
  else:
    stamina_cpu=0
    hp=-dado(4)
    
  return hp, 0, 0, stamina_cpu,0

def ataquevs(ação2):
  mana2=0
  if ação2=='E' or ação2=='e':
    hp1=0
    stamina2=1
    if arma1=='Machado':
      stamina1=0
      hp2=-dado(6)
    elif arma1=='Lança':
      stamina1=-2
      hp2=-dado(9)
    else:
      stamina1=-1
      hp2=-dado(7)

  elif ação2=='D' or ação2=='d':
    hp1=0
    stamina2=0
    if arma1=='Machado':
      stamina1=-1
      hp2=-dado(3)
    elif arma1=='Lança':
      stamina1=-3
      hp2=-dado(5)
    else:
      stamina1=-2
      hp2=-dado(4)

  elif ação2=='A' or ação2=='a':
    if arma1=='Machado':
      stamina1=-1
      hp2=-dado(5)
    elif arma1=='Lança':
      stamina1=-2
      hp2=-dado(7)
    else:
      stamina1=-1
      hp2=-dado(6)

    if arma2=='Machado':
      stamina2=-1
      hp1=-dado(5)
    elif arma1=='Lança':
      stamina2=-2
      hp1=-dado(7)
    else:
      stamina2=-1
      hp1=-dado(6)

  else:
    hp2=0
    stamina2=0
    mana2=-1
    hp1=0
    if raca2=='Humano':
      hp2=dado(8)
    elif raca2=='Ogro':
      if habilidade1=='Magia':
        hp1=-dado(6)
      else:
        hp1=-dado(8)
    else:
      stamina2=dado(5)

    if arma1=='Machado':
      stamina1=-1
      hp2-=dado(6)
    elif arma1=='Lança':
      stamina1=-2
      hp2-=dado(9)
    else:
      stamina1=-1
      hp2-=dado(7)
  return hp1, hp2, stamina1, stamina2, 0, mana2

def esperavs(ação2):
  hp2=0
  if ação2=='E' or ação2=='e':
    hp1=0
    stamina2=1
    mana2=0

  elif ação2=='D' or ação2=='d':
    hp1=0
    stamina2=0
    mana2=0

  elif ação2=='A' or ação2=='a':
    mana2=0
    if arma2=='Machado':
      stamina2=0
      hp1=-dado(6)
    elif arma2=='Lança':
      stamina2=-2
      hp1=-dado(9)
    else:
      stamina2=-1
      hp1=-dado(7)

  else:
    stamina2=0
    mana2=-1
    hp1=0
    if raca2=='Humano':
      hp2=dado(8)
    elif raca2=='Ogro':
      if habilidade1=='Magia':
        hp1=-dado(6)
      else:
        hp1=-dado(8)
    else:
      stamina2=dado(5)

  return hp1, hp2, 1, stamina2, 0, mana2

def defesavs(ação2):

  if ação2=='E' or ação2=='e':
    hp1=0
    stamina2=1
    mana2=0

  elif ação2=='D' or ação2=='d':
    hp1=0
    stamina2=0
    mana2=0

  elif ação2=='A' or ação2=='a':
    mana2=0
    if arma2=='Machado':
      stamina2=-1
      hp1=-dado(3)
    elif arma2=='Lança':
      stamina2=-3
      hp1=-dado(5)
    else:
      stamina2=-1
      hp1=-dado(4)

  else:
    hp2=0
    stamina2=0
    mana2=-1
    hp1=0
    if raca2=='Humano':
      hp2=dado(8)
    elif raca2=='Ogro':
      if habilidade1=='Magia':
        hp1=-dado(4)
      else:
        hp1=-dado(6)
    else:
      stamina2=dado(5)

  return hp1, 0, 0, stamina2, 0, mana2

def magiavs(ação2):
  mana2=0
  stamina1=0
  stamina2=0
  if ação2=='E' or ação2=='e':
    hp2=0
    hp1=0
    stamina2=1
    if raca1=='Humano':
      hp1=dado(8)
    elif raca1=='Ogro':
      if habilidade2=='Magia':
        hp2=-dado(6)
      else:
        hp2=-dado(8)
    else:
      stamina1=dado(5)

  elif ação2=='D' or ação2=='d':
    hp2=0
    hp1=0
    stamina2=0
    if raca1=='Humano':
      hp1=dado(8)
    elif raca1=='Ogro':
      if habilidade2=='Magia':
        hp2=-dado(6)
      else:
        hp2=-dado(8)
    else:
      stamina1=dado(5)

  elif ação2=='A' or ação2=='a':
    hp2=0
    stamina1=0
    hp1=0
    if raca1=='Humano':
      hp1=dado(8)
    elif raca1=='Ogro':
      if habilidade2=='Magia':
        hp2=-dado(6)
      else:
        hp2=-dado(8)
    else:
      stamina1=dado(5)

    if arma2=='Machado':
      stamina2=-1
      hp1-=dado(6)
    elif arma2=='Lança':
      stamina2=-2
      hp1-=dado(9)
    else:
      stamina2=-1
      hp1-=dado(7)

  else:
    mana2=-1
    hp1=0
    hp2=0
    stamina2=0
    stamina1=0
    if raca1=='Humano':
      hp1=dado(8)
    elif raca1=='Ogro':
      if habilidade2=='Magia':
        hp2-=dado(6)
      else:
        hp2-=dado(8)
    else:
      stamina1=dado(5)

    if raca2=='Humano':
      hp2+=dado(8)
    elif raca2=='Ogro':
      if habilidade2=='Magia':
        hp2-=dado(6)
      else:
        hp2-=dado(8)
    else:
      stamina2=dado(5)

  return hp1, hp2, stamina1, stamina2, -1, mana2
  
def personagem():
  racas=['Ogro','Humano','Elfo']
  raca=input('Escolha sua Raça:\n -Humano \n -Ogro \n -Elfo\n')
  while raca not in racas:
    raca=input('Raça invalida, escolha:\n -Humano \n -Ogro \n -Elfo\n')
  proeficiencias=['Machado','Espada','Lança']
  proeficiencia=input('Escolha sua arma: \n -Machado \n -Espada \n -Lança\n')
  while proeficiencia not in proeficiencias:
    proeficiencia=input('Arma invalida, escolha: \n -Machado \n -Espada \n -Lança\n')
  habilidades=['Magia','Sorte','Força']
  habilidade=input('Escolha sua habilidade: \n -Magia \n -Força \n -Sorte\n')
  while habilidade not in habilidades:
    habilidade=input('Habilidade invalida, \n -Magia \n -Força \n -Sorte\n')
  
  return raca, proeficiencia, habilidade

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
    sumario1='Sua infância foi repleta de bons momentos, sua família, por ter raízes no exercito da cidade, era conhecida por todos ali. Você treinava diariamente na esperança de se equivaler a seu irmão que fora para a capital defender o reino da invasão de um reino inimigo."\n'
  elif habilidade=='Magia':
    sumario1='Como todo bom aprendiz de feiticeiro, você passou a infância enfiado nos livros e assim conseguiu o dominio dos elementos que lhe garantem proteção."\n'
  else:
    sumario1='Correndo de guardas, roubando bolsos e dormindo em becos assim pode se resumir a sua juventude orfã na capital. A maioria dos garotos com que você convivia ja foram mandados para a prisão, mas você peculiarmente tem o dom de sempre estar um passo a frente da polícia."\n'
  print(sumario1)
  
  print('"Porém tudo isso mudou quando recebeu a oferta de um grupo de criminosos, não ladrões comuns, mas sim o Grupo ''Serpente'' que é conhecido na região por sua atividade agiota em troca de duelos na Arena local, e em prol da saúde de sua mãe em estado doente você se sentiu obrigado a aceitar a proposta."\n')

def combate1():
  turno=1
  stamina=2
  stamina_cpu=1
  if habilidade=="Força":
    hp=36
  else:
    hp=30
  hp_new=hp
  hpcpu=30
  hpcpu_new=hpcpu
  if habilidade=='Magia':
    mana=3
  else: 
    mana=1
  ações=['A','M','D','E','a','m','d','e']
  print('Seu inimigo se aproxima, ')
  while hpcpu_new >= 0 and hpcpu_new >= 0:
    if stamina <=0:
      print('Você aparenta estar esgotado...')
    else:
      if stamina < 2 and arma=='Lança':
        print('Você sente o peso da sua lança e percebe que não está 100% recuperado...')
      elif arma=='Machado':
        print('Você consegue segurar firmemente seu machado para o proximo ataque!')
      elif arma=='Espada':
        print('Com sua espada empunhada você se sente pronto para o proximo ataque!')
      elif stamina >=2:
        print('Você segura sua Lança com confiança e está pronto para o proximo golpe!')
    ação=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while ação not in ações:
      ação=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while stamina <=0 and (ação=='A' or ação=='a'):
      ação=input('Não tem energia suficiente para atacar, (D)EFESA, (E)SPERAR ou (M)AGIA?\n')
    while mana <= 0 and (ação=='M' or ação=='m'):
      ação=input('Não tem mana suficiente para usar magia, (D)EFESA, (E)SPERAR ou (A)TACAR?\n') 
    if stamina_cpu <= 0:
      ação_cpu=cpu_cansado()
    else:
      ação_cpu=cpu_AI()
      
    if ação=='A' or ação=='a':
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=ataque(ação_cpu)
    elif ação=='M' or ação=='m':
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=magia(ação_cpu)
    elif ação=='E' or ação=='e':
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=espera(ação_cpu)
    else:
      hpchange,hp_cpuchange,stachange,sta_cpuchange,mana_change=defesa(ação_cpu)
      
    hp_new+=hpchange
    stamina+=stachange
    hpcpu_new+=hp_cpuchange
    stamina_cpu+=sta_cpuchange
    mana+=mana_change
    print('-----------------------------')
    print('TURNO: {}\n'.format(turno))
    print('O Inimigo utilizou:', ação_cpu)
    if hpchange<0:
      print('O inimigo realiza: {} de dano'.format(abs(hpchange)))
    if hpchange>0:
      print('Você cura: {} de dano'.format(abs(hpchange)))
    if hp_cpuchange<0:
      print('Você realiza: {} de dano'.format(abs(hp_cpuchange)))
    print('Seu HP:',hp,"/",hp_new)
    print('HP do inimigo:', hpcpu,"/",hpcpu_new)
    turno+=1

  if hp_new <= 0:
    print('Você morreu, sua jornada acaba aqui')
    return
  elif hpcpu_new<=0:
    print('Você venceu')

def vsmode():
  esquiva1='1'
  esquiva2='1'
  turno=1
  stamina1=2
  stamina2=2
  if habilidade1=="Força":
    hp1=36
  else:
    hp1=30
  if habilidade2=="Força":
    hp2=36
  else:
    hp2=30
  hp_new1=hp1
  hp_new2=hp2
  if habilidade1=='Magia':
    mana1=3
  else: 
    mana1=1
  if habilidade2=='Magia':
    mana2=3
  else: 
    mana2=1
  ações=['A','M','D','E','a','m','d','e']
  print('Seu inimigo se aproxima\n')
  while hp_new1 >= 0 and hp_new2 >= 0:
    print(nome1,'decida seu proximo movimento')
    if stamina1 <=0:
      print('Você aparenta estar esgotado...')
    else:
      if stamina1 < 2 and arma1=='Lança':
        print('Você sente o peso da sua lança e percebe que não está 100% recuperado...')
      elif arma1=='Machado':
        print('Você consegue segurar firmemente seu machado para o proximo ataque!')
      elif arma1=='Espada':
        print('Com sua espada empunhada você se sente pronto para o proximo ataque!')
      elif stamina1 >=2:
        print('Você segura sua Lança com confiança e está pronto para o proximo golpe!')
    ação1=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while ação1 not in ações:
      ação1=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while stamina1 <=0 and (ação1=='A' or ação1=='a'):
      ação1=input('Não tem energia suficiente para atacar, (D)EFESA, (E)SPERAR ou (M)AGIA?\n')
    while mana1 <= 0 and (ação1=='M' or ação1=='m'):
      ação1=input('Não tem mana suficiente para usar magia, (D)EFESA, (E)SPERAR ou (A)TACAR?\n')

    print(nome2,'decida seu proximo movimento')
    if stamina2 <=0:
      print('Você aparenta estar esgotado...')
    else:
      if stamina2 < 2 and arma2=='Lança':
        print('Você sente o peso da sua lança e percebe que não está 100% recuperado...')
      elif arma2=='Machado':
        print('Você consegue segurar firmemente seu machado para o proximo ataque!')
      elif arma2=='Espada':
        print('Com sua espada empunhada você se sente pronto para o proximo ataque!')
      elif stamina2 >=2:
        print('Você segura sua Lança com confiança e está pronto para o proximo golpe!')
    ação2=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while ação2 not in ações:
      ação2=input('\n*************\n >(A)TACAR\n >(M)AGIA\n >(E)SPERAR\n >(D)EFESA\n*************\n')
    while stamina2 <=0 and (ação2=='A' or ação2=='a'):
      ação2=input('Não tem energia suficiente para atacar, (D)EFESA, (E)SPERAR ou (M)AGIA?\n')
    while mana2 <= 0 and (ação2=='M' or ação2=='m'):
      ação2=input('Não tem mana suficiente para usar magia, (D)EFESA, (E)SPERAR ou (A)TACAR?\n')
      
    if ação1=='A' or ação1=='a':
      hpchange1,hpchange2,stachange1,stachange2,manachange1,manachange2=ataquevs(ação2)
    elif ação1=='M' or ação1=='m':
      hpchange1,hpchange2,stachange1,stachange2,manachange1,manachange2=magiavs(ação2)
    elif ação1=='E' or ação1=='e':
      hpchange1,hpchange2,stachange1,stachange2,manachange1,manachange2=esperavs(ação2)
    else:
      hpchange1,hpchange2,stachange1,stachange2,manachange1,manachange2=defesavs(ação2)

    if (ação2 =='A' or ação2 == 'a') and habilidade1=='Sorte':
      esquiva1=esquiva()
      if esquiva1=='0':
        hpchange1=0

    if (ação1 =='A' or ação1 == 'a') and habilidade2=='Sorte':
      esquiva2=esquiva()
      if esquiva2=='0':
        hpchange1=0

      
    hp_new1+=hpchange1
    hp_new2+=hpchange2
    stamina1+=stachange1
    stamina2+=stachange2
    mana1+=manachange1
    mana2+=manachange2
    print('-----------------------------')
    print('TURNO: {}\n'.format(turno))
    
    if esquiva1=='0':
      print(nome1,'Se utilizou de sua sorte para esquivar-se de um golpe')
    if esquiva2=='0':
      print(nome2,'Se utilizou de sua sorte para esquivar-se de um golpe')

    if hpchange2<0:
      print(nome1,' realiza: {} de dano'.format(abs(hpchange2)))
    if hpchange1<0:
      print(nome2,' realiza: {} de dano'.format(abs(hpchange1)))
    if hpchange1>0:
      print(nome1,' cura: {} de dano'.format(hpchange1))
    if hpchange2>0:
      print(nome2,' cura: {} de dano'.format(hpchange2))

    print('HP de',nome1,":",hp1,"/",hp_new1)
    print('HP de',nome2,":",hp2,"/",hp_new2)
    print()
    turno+=1

  if hp_new1 <= 0 and hp_new2 <=0:
    print('Com a morte dos dois combatentes, a luta terminou em empate')
    return
  elif hp_new2 <=0:
    print(nome1,'Venceu a luta!\n')
  else:
    print(nome2,'Venceu a luta!\n')


start=0
while start != 1 or start !=2:
  print('------------------------------------------------------')
  print('--------------- BEM VINDO A ARENA   ----------------- ')
  print('------------------------------------------------------\n')
  start=int(input("Você deseja jogar o modo história ou contra outro jogador?\n1-Historia \n2-Versus\n"))
  if start==1:
    print('MONTE SEU GUERREIRO:\n')
    raca,arma,habilidade=personagem()
    apresentaçao()
    combate1()

  if start==2:
    habilidade=''
    nome1=input('PLAYER 1 DIGITE SEU NOME: ')
    nome2=input('PLAYER 2 DIGITE SEU NOME: ')
    print('----------------------------------')
    print('PLAYER 1 MONTE SEU GUERREIRO\n')
    raca1,arma1,habilidade1=personagem()
    print('PLAYER 2 MONTE SEU GUERREIRO\n')
    raca2,arma2,habilidade2=personagem()
    vsmode()
  else:
    ("Comando invalido, digite 1 ou 2")
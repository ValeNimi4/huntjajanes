#! /usr/bin/python3
def v2lju():
    global STOPP
    STOPP = True
    sys.exit()
def rp(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
STOPP = False
manguinfo = """
Hunt ja jänes
Oled jänes. Põgene hundi eest ja ära nälga jää!
Nooleklahvidega või WASD liigub
Veebileht: valeNimi4.github.io/huntjajanes
Vajuta alustamiseks nooleklahvi "alla", arvutis saab ka vajutades nupule ALUSTA.
Porgand annab energiat 10 sekundiks ja raha 3€
p on porgandi, jk jänese kiiruse ja hk hundikiiruse lühend.
Iga 60 sekundi tagant käib hunt vargil
Vajuta P/Esc et minna poodi
Hunt saab iga 60s tagant kiiruse võrdseks s ja varastab
(c) valeNimi4 (github.com/ValeNimi4) Litsents: GPL v3"""
pygame.init()
ekraan = pygame.display.set_mode((400,400), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption("Hunt ja jänes")
kell = pygame.time.Clock()
pygame.mixer.music.load(rp("hunt_ja_janes.mp3"))
pygame.mixer.music.play(-1)
janku_vasakule = pygame.image.load(rp("janes_ainult_vasakule.png"))
janku_paremale = pygame.image.load(rp("janes_ainult_paremale.png"))
hundi_pilt = pygame.image.load(rp("hunt.png"))
porgandipilt = pygame.image.load(rp("porgand.png"))
porgand = porgandipilt.get_rect()
KIRI = pygame.image.load(rp("janes.png"))
font = pygame.font.Font(None, 25)
raha_heli = pygame.mixer.Sound(rp("raha.mp3"))
manglabi = pygame.mixer.Sound(rp("manglabi.mp3"))
heli = pygame.mixer.Sound(rp("porgand.mp3"))
taust = pygame.image.load(rp("taust.png"))
janku_pilt = janku_vasakule
janku_rect = janku_pilt.get_rect()
# algus- ja sihtpunkt
hunt = pygame.math.Vector2(0, 0)
janku_rect.x, janku_rect.y = [375, 375]
porgand.x, porgand.y = [randint(0,348),randint(0,380)]
aken = pygame_gui.UIManager((400,400))
nupp_start = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((0,25), (400,50)),
    text='!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ALUSTA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!',
    manager=aken
)
nupp_info = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0,0), (400,25)), text="Info (nool üles)", manager=aken)
m2nguinfo = pygame_gui.elements.UITextBox(
    html_text=manguinfo.replace("\n", "<br>"),
    relative_rect=pygame.Rect((0,25), (400,400)),
    manager=aken
)
pood = pygame_gui.elements.UITextBox(
    html_text="POOD",
    relative_rect=pygame.Rect((0,0), (400,400)),
    manager=aken
)
pood.hide()
pygame.mouse.set_visible(False)
kiirus = 2
suund = "vasakule"
poevalikud = ["leht", "kapsas", "kiirus"]
running = True
aeg = 0
raha = 6
kaader = 0
jkiirus = 4
algus = True
pime = 0
ntinfot = False
m2nguinfo.hide()
pygame.display.set_icon(janku_pilt)
kursor = 0
while algus:
    dt = kell.tick(60) / 1000
    for e in pygame.event.get():
        aken.process_events(e)
        if e.type == pygame.QUIT:
            pygame.quit()
            v2lju()
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN:
            algus = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                if ntinfot:
                    m2nguinfo.hide()
                    ntinfot = False
                else:
                    ntinfot = True
                    m2nguinfo.show()
        elif e.type == pygame.MOUSEMOTION:
            kursor += 1
        elif e.type == pygame_gui.UI_BUTTON_PRESSED:
            if e.ui_element == nupp_start:
                algus = False
            elif e.ui_element == nupp_info:
                if ntinfot:
                    m2nguinfo.hide()
                    ntinfot = False
                else:
                    ntinfot = True
                    m2nguinfo.show()
    ekraan.fill((0,255,0))
    ekraan.blit(taust, [0,0])
    ekraan.blit(KIRI, [0,250])
    aken.update(dt)
    aken.draw_ui(ekraan)
    if kursor > 50:
        ekraan.blit(porgandipilt, pygame.mouse.get_pos())
    pygame.display.flip()
nupp_start.hide()
nupp_info.hide()
m2nguinfo.hide()
m2ng = True
viimati_saadud = -1
eelminekiirendus = 0
pime = False
kapsapea = False
kolmkummend = 6
while m2ng:
    dt = kell.tick(60) / 1000
    if viimati_saadud == 10:
        break
    elif viimati_saadud > 6:
        hoiatus = "NÄLG "
    else:
        hoiatus = ""
    kaader += 1
    if kaader == 60:
        kaader = 1
        aeg += 1
        viimati_saadud += 1
        if pime:
            pime -= 1
    for e in pygame.event.get():
        valik = None
        if e.type == pygame.QUIT:
            pygame.quit()
            v2lju()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                suund = "paremale"
                janku_pilt = janku_paremale
            elif e.key == pygame.K_LEFT:
                suund = "vasakule"
                janku_pilt = janku_vasakule
            elif e.key == pygame.K_DOWN:
                suund = "alla"
            elif e.key == pygame.K_UP:
                suund = "üles"
            elif e.key == pygame.K_d:
                suund = "paremale"
                janku_pilt = janku_paremale
            elif e.key == pygame.K_a:
                suund = "vasakule"
                janku_pilt = janku_vasakule
            elif e.key == pygame.K_s:
                suund = "alla"
            elif e.key == pygame.K_w:
                suund = "üles"
            elif e.key in [pygame.K_ESCAPE, pygame.K_p]:
                paus = True
                teade = ""
                hoiatus = "POOD "
                valiknr = 0
                pood.show()
                while paus:
                    dt = kell.tick(60) / 1000
                    for e in pygame.event.get():
                        valik = None
                        aken.process_events(e)
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            v2lju()
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_UP:
                                if valiknr > 0:
                                    valiknr -= 1
                                else:
                                    valiknr = len(poevalikud) - 1
                            elif e.key == pygame.K_DOWN:
                                if valiknr < len(poevalikud) - 1:
                                    valiknr += 1
                                else:
                                    valiknr = 0
                            elif e.key == pygame.K_RIGHT:
                                valik = poevalikud[valiknr]
                            elif e.key in [pygame.K_ESCAPE, pygame.K_LEFT, pygame.K_p]:
                                valik = "jätka"
                        aken.process_events(e)
                        if valik:
                            if valik == "kiirus":
                                if raha > 50:
                                    raha -= 51
                                    jkiirus += 1
                                    teade = 'Ostetud "+1 kiirust"'
                                    raha_heli.play()
                                else:
                                    teade = "Pole piisavalt raha"
                            elif valik == "kapsas":
                                if raha > 14:
                                    raha -= 15
                                    kolmkummend += 6
                                    teade = 'Ostetud "kapsapea"'
                                    raha_heli.play()
                                else:
                                    teade = "Pole piisavalt raha"
                            elif valik == "leht":
                                if raha > 2:
                                    raha -= 3
                                    viimati_saadud = -1
                                    teade = 'Ostetud "leht"'
                                    raha_heli.play()
                                else:
                                    teade = "Pole piisavalt raha"
                            if valik == "jätka":
                                paus = False
                    ekraan.fill((0,255,0))
                    poekiri = f"""{hoiatus}{aeg}s {raha}€={int(raha / 3)}p HK: {kiirus} JK {jkiirus} {kolmkummend}€/30s<br>
Sinu valik: {poevalikud[valiknr]}<br>Ostmine = paremale, valimine=üles/alla, jätka = vasakule<br><a href="kiirus">+1 kiirust 51€</a><br><a href="leht">leht, annab energiat 10 sekundiks 3€</a><br><a href="kapsas">kapsapea, tõstab 30s tasu 6€ võrra 15€</a><br><b>{teade}</b>"""
                    pood.set_text(poekiri)
                    aken.update(dt)
                    aken.draw_ui(ekraan)
                    pygame.display.flip()
    if suund == "paremale" and janku_rect.x < 375:
        janku_rect.x += jkiirus
    elif suund == "vasakule" and janku_rect.x > 0:
        janku_rect.x -= jkiirus
    elif suund == "alla" and janku_rect.y < 375:
        janku_rect.y += jkiirus
    elif suund == "üles" and janku_rect.y > 0:
        janku_rect.y -= jkiirus
    janku = pygame.math.Vector2(janku_rect.x, janku_rect.y)
    # liikumine vektoriga
    kurss = janku - hunt
    kurss = kurss.normalize() * kiirus
    hunt += kurss
    if janku_rect.colliderect(pygame.Rect(int(hunt.x), int(hunt.y), 50, 25)):
        hoiatus = "HUNT "
        break
    if porgand.colliderect(janku_rect):
        heli.play()
        raha += 3
        viimati_saadud = -1
        porgand.x, porgand.y = [randint(0,348),randint(0,380)]
    if aeg != eelminekiirendus and aeg % 60 == 0:
        eelminekiirendus = aeg
        raha = 0
        kiirus = jkiirus - 1
        raha += kolmkummend
    if not pime and aeg != 0 and aeg % 20 == 0:
        pime = 10
    if aeg != eelminekiirendus and aeg % 30 == 0:
        eelminekiirendus = aeg
        raha += kolmkummend
    kiri = f"{hoiatus}{aeg}s {raha}€={int(raha / 3)}p HK: {kiirus} JK. {jkiirus} {kolmkummend}€/30s"
    if pime:
        ekraan.fill((0,0,0))
        ekraan.blit(font.render(kiri, True, "white"), [0,0])
    else:
        ekraan.fill((0, 255, 0))
        ekraan.blit(taust, [0,0])
        ekraan.blit(font.render(kiri, True, "black"), [0,0])
    ekraan.blit(hundi_pilt, [int(hunt.x), int(hunt.y)])
    ekraan.blit(janku_pilt, janku_rect)
    ekraan.blit(porgandipilt, porgand)
    pygame.display.flip()
pygame.mixer.music.stop()
manglabi.play(-1)
ntlabi = True
while ntlabi:
    dt = kell.tick(1) / 1000
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            v2lju()
        elif e.type == pygame.KEYDOWN:
            ntlabi = False
    ekraan.fill((0,255,0))
    pood.show()
    pood.set_text(f"Surid :(<br>Põhjus: {hoiatus}<br>{aeg}s {raha}€={int(raha / 3)}p<br>hundikiirus: {kiirus} jänesekiirus {jkiirus}<br>Vajuta ükskõik mida jätkamiseks...")
    aken.update(dt)
    aken.draw_ui(ekraan)
    pygame.display.flip()
pygame.quit()
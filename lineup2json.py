import json
import re
import unicodedata

text = """
Gorki List Main Stage
Šajzerbiterlemon 20:00
Viagra Boys 21:00
Opening Ceremony 22:45
The Prodigy 23:20
Chase & Status DJ Set 01:05
Gardna 02:40
Charlie Tee 03:45
mts Dance Arena
Vylana 21:30
Miju 22:30
Lanna 23:30
Tijana T 00:30
Amelie Lens 02:00
Nina Kraviz 04:00
Indira Paganotto 06:00
Visa Fusion Stage
TBK 19:30
Badfocus 20:35
Freekind. 21:50
Ploho 23:10
Rudeboy plays Urban Dance Squad ft. DJ Dna 00:40
Pero Defformero 02:00
Mortal Kombat 03:30
Explosive Stage
Dead Dog Summer 20:00
3AM 20:55
Urban Instinkt 22:00
Ignite 23:00
Night Fever 00:20
Wolfbrigade 01:30
Polywhy 02:45
Hak Attak 03:35
NSNS Refreshed by Heineken Silver
Rade Badjin 22:00
DJ Brka & Runy 00:00
Ben Ufo 02:00
Avalon Emerson 04:00
Krystal Klear 06:00
Gang Beats
Gang Beats Mixtape 20:00
Keyri DJ Set 21:00
2soma 22:30
Av47 23:00
Kultura DJ Set 23:30
FTP 23:50
Gerum 00:30
Kultura DJ Set 01:00
Bore Balboa 01:20
Grše 02:10
30Zona 03:00
Faberge x Kza 03:45
Gang Beats Mixtape 04:30
X-Bass Pit
Souldrive 22:00
DSPT 23:30
C:Critz 00:30
Charlie Tee 01:30
Monrroe & Bo Jah MC 02:30
Statik 04:00
Wenti Wadada Positive Vibrations Reggae
Reggae Intro 20:00
ShowMe Selecta 21:30
Ital Vision 23:00
Salmanovicc 00:30
Bush Mad Squad 02:00
Gigatron Selecta 03:30
Gaia Trance Stage
DJ Andjela 21:00
DJ Solar Kid 23:00
DJ Pura 01:00
DJ Manda 02:45
DJ Albert 04:30
Latino Stage by IDEA
DJ Ice 20:00
Orient Express 22:00
Allegro 22:45
DJ Sinny 23:20
Latin Fitness Power 23:40
Brazil Sambalkinhas 00:10
DJ Rey 01:00
DJ`s b2b 03:00
Urban Bug Stage
Marina Mimoza b2b Pink Palindrome 19:00
Teachr b2b Wortexx 20:00
Vladimir Tucakov b2b Bokun 21:00
Denni b2b Victoria 22:00
Slobodan Jevremović b2b Carlo Gotovac 23:00
Dimitri J b2b Un Padre 00:00
Perfect Pitch DJs 01:00
Zarez b2b Vladislav Rashkov 02:00
Vanja Bursać b2b Vojkan Bećir b2b Alek Bošković 03:00
Novak b2b Fakir 04:00
Una Nikolić b2b Despić 05:00
Sho b2b Jovana Takač 06:00
Mancha b2b Mark Panic 07:00
Radio AS FM Stage
Stanik b2b Fantomska Napast / Klostridijum 20:00
Meli 22:00
Morning Indian 23:00
Groover 00:30
Peryz & Daave 02:00
Spear 03:30
Lena Glish 05:00
Official Afterparty
G76 07:00
Mihigh 10:00
Pachamama Powered by ROSA
Sarasvati Druna Bend 20:00
DJ Đorđe Bastovanović 21:15
Dub Duba 23:00
Nektarije 01:00
Together. X House by IQOS
JO:LE 21:00
Ned O'Neal 22:00
Deaf In Mini 23:00
Nitefreak 00:30
Mark Funk b2b Danny Cruz 02:30
Coketails Zone
Mix 21:00
Luton b2b Šćepine Vragolije 22:00
Gorki List Main Stage
Ground Zero vs War Engine 20:15
Jenner 21:30
Epica 23:00
Skrillex 01:00
LF System 02:45
Burak Yeter 04:00
mts Dance Arena
Cosmic G 21:00
Kristijan Molnar 22:30
Space Motion 00:30
Eric Prydz 02:00
Camelphat 04:00
Coeus 06:00
Human Rias 07:00
Visa Fusion Stage
Petar Z 19:30
Sicksoul 20:40
Dina Jashari & Drugari 21:50
Dzipsii 23:00
Zoe Kida 00:10
Kendi 01:25
Crni Cerak & Lacku 02:40
Sunshine 03:45
Explosive Stage
Affliction 19:30
Larska 20:30
Sur Austru 21:35
Mirror 22:35
Hyperborea 00:00
Midnight 01:00
Nervochaos 02:20
Violentor 03:20
NSNS Refreshed by Heineken Silver
Danilo Kas b2b Sergej Krstić 22:00
Luton b2b Šćepine Vragolije 00:00
Desiree 02:00
Shimza 04:00
Carlita 06:00
Gang Beats
Gang Beats Mixtape 20:00
Sarchy DJ Set 21:15
Ena x Rouzi 22:15
Zevin 23:00
Jymenik x Mlada Beba 23:35
TTM 00:00
Fam DJ Set 00:40
Tam 01:00
Spejs Noksi & Kene Beri 01:45
Ružno Pače 02:30
Fam DJ Set 03:10
Yung Bude 03:30
Dino Blunt 04:00
Gang Beats Mixtape 04:40
X-Bass Pit
Slink 22:00
Leol Drop Sensei 23:30
Missin 00:30
Youphoria 01:30
Tendo 03:00
Buzzin 04:00
Wenti Wadada Positive Vibrations Reggae
Little Shuja 20:00
Herbal Queen 22:00
Jahmessenjah Sound System 23:30
RootsInSession 01:00
AKKA 03:00
Gaia Trance Stage
DJ Vlada 21:00
Ectima live 00:00
Zyce live 01:00
Flegma live 02:00
DJ Hruscsov 03:00
Latino Stage by IDEA
DJ Sinny 20:00
Zero Witches 22:00
DJ Tete 22:20
Surma & Latino Fitness Power 22:50
Pablo & Mauri 00:00
Casanova 01:00
Gatto & Mad Piano 02:00
Tito 03:20
Urban Bug Stage
Harry Qarter b2b Machiavelli 19:00
Vlado Božović b2b Mr. Mips 20:00
Zira b2b Gostoja 21:00
Wocky b2b Svemirski Mjau 22:00
The + b2b Mina Poznanović 23:00
Dakman b2b Dakissa 00:00
Kristijan Šajković b2b Janko 01:00
Layzie b2b Techa 02:00
Undoo b2b Cosmic G 03:00
Luton b2b Šćepine Vragolije b2b Danilo Kas 04:00
Bo-Ian b2b Chv 05:00
Neutron b2b Vanja Babić 06:00
Knower b2b Stenik 07:00
Radio AS FM Stage
Milo / Znaš Vanju?! 20:00
Marcuss 22:00
Groover 23:00
Lena Glish 00:30
Dale 02:00
Jjoy 03:30
Ra5tik 05:00
Official Afterparty
Nick Morgan 07:00
Coeus 09:00
Inner Sense 11:00
Pachamama Powered by ROSA
Hearts Liberated 20:00
Vylana 21:15
Tebra 22:30
Klo Klo 00:15
It's a Global Thing ft. Black City Boys 01:15
Together. X House by IQOS
Mr. Fanatik 21:00
Lisa 22:00
Ogyy 23:00
Karyen De Soul 00:00
Fabrizio Marra 02:00
Coketails Zone
Mix 21:00
DJ Eye, Rescobar, Vaso 22:00
Gorki List Main Stage
Kejt 19:30
Sajsi MC 20:25
Mimi Mercedez 21:15
Senidah 22:15
Sofi Tukker 23:30
Claptone 01:00
Alesso 02:30
Lady Lee / iLee 04:35
mts Dance Arena
IDQ 21:00
Mene 22:00
Layla Benitez 23:30
Gioli & Assia live 01:00
Vintage Culture 02:30
Hot Since 82 04:00
Marko Nastić 06:00
Visa Fusion Stage
Jolly Little Bunch 19:30
Manna 20:30
Spasibo 21:35
Nikola Vranjković 22:40
Bojana Vunturišević 00:00
Porto Morto 01:15
Hiljson Mandela 02:45
Z++ 03:45
Explosive Stage
Svlak 20:00
Fiskalni racun 20:45
Mige i Vršnjaci 21:40
The Bar Stool Preachers 22:35
Cockney Rejects 23:40
Daikaiju 01:00
Punkreas 02:00
V Okovih 03:00
NSNS Refreshed by Heineken Silver
Jovana Takač 22:00
Vahicabi 23:30
Cici 01:00
Partiboi69 03:00
X-Coast 05:00
Partiboi69 b2b X-Coast 07:00
Gang Beats
Gang Beats Mixtape 20:00
Thicc Boi DJ Set 21:00
Matej Foltz & Young Dadi 22:00
Zee 22:20
RNB Confusion w/ DJ Turk & Zembo Latifa 22:40
2xŠihta 23:10
Podočnjaci 23:50
Big Drip DJ Set 00:30
Bejbi Motorola & Thea 00:50
Macha Ravel 01:30
Big Drip DJ Set 02:10
Ognjen 02:30
Bekfleš 03:20
Gang Beats Mixtape 04:00
X-Bass Pit
Quantrussyan 22:00
Indukt 23:30
Shizzla 00:30
Jade 01:30
Drop Sensei 03:00
Rebar 04:00
Wenti Wadada Positive Vibrations Reggae
Mizizi Selectah 20:00
DJ Elioh 21:15
Del Arno Band 22:30
Hornsman Coyote DJ set 23:45
DJ/MC Killo Killo 01:00
Deadly Hunta 02:00
RootsInSession 03:00
Gaia Trance Stage
DJ Cheda 21:00
Species Live 00:00
DJ Aquapipe 02:00
DJ Dapeace 04:00
Latino Stage by IDEA
DJ Rey 20:00
Brazil Sambalkinjas 21:00
Zero Witches 22:00
Allegro 22:30
DJ Beathoven 23:00
Sosabi 00:00
Tito 01:15
Surma 01:25
DJ Sesha 03:00
Urban Bug Stage
Papachek b2b Pao Pausto 19:00
Stamina b2b Teodora Jarić 20:00
Perfect Pitch DJs 21:00
Hudi b2b Sicillio 22:00
Nemansky b2b Theanilo 23:00
Techni b2b Yugen 00:00
Una Andrea b2b Anyushka 01:00
Rudhaman b2b Milanko Trifunčević 02:00
Denis Dražić b2b Spicy Flamingo 03:00
Nadezda Dimitrijević b2b Vuk Smiljanić 04:00
Filthy Kid b2b Miloš Vujović 05:00
Inner Sense 06:00
Migazz b2b Novak 07:00
Radio AS FM Stage
Moises / Coa 20:00
Ivan Pobor 22:00
The Vibe Radio Show DJ’s 23:00
Supertons 01:30
Macro 03:00
Peryz & Daave 04:30
Official Afterparty
Calussa 07:00
Space Motion 09:00
iLEE 11:00
Cuneyt Cilingiroglu 12:00
Un Padre b2b Dimitri J 13:00
Pachamama Powered by ROSA
Julija Kastaluči 20:00
Laura Escude 21:30
Deep Steady 23:00
Shi Cu 00:30
Lo Fi Falafel 01:30
Together. X House by IQOS
Mr. Fanatik 21:00
Luka Čikić 22:00
IDQ DJ Set 23:30
Caiiro 01:00
BDM DJ Set 03:00
Coketails Zone
Mix 21:00
Marko Milosavljević, Zarez Dunga, Bucotzar 22:00
Awavemess DJ Set 03:00
Gorki List Main Stage
Thicc Boi 19:00
Micka Lifa 20:00
Tam 20:15
Macha Ravel 20:40
Fox & Surreal 21:00
Aigel 21:30
Njezz 22:05
Blackout30 Showcase: Onyx x Prti Bee Gee x Bolesna Braca x Smoke Mardeljano & Ajs Nigrutin x Bege Fank + Phat Phillie 22:25
Wu Tang Clan 00:00
Dimitri Vegas & Like Mike 02:00
Mahmut Orhan 03:30
mts Dance Arena
Goran Starčević 21:00
Gheist live 22:30
8kays 23:30
Ben Böhmer live 01:00
Agents Of Time live 02:30
Mind Against 04:00
Keinemusik 06:00
Visa Fusion Stage
Short Reports 19:30
K not K 20:35
The Toasters 21:50
Dry Cleaning 23:20
Atheist Rap 00:50
Smoke Mardeljano & Ajs Nigrutin 02:30
Prti Be Gee 03:50
Explosive Stage
Claymorean 19:30
Dead Joker 20:30
Sarcasm 21:30
Bombarder 22:40
Exciter 23:50
Massacre 01:10
Flesh 02:30
Armada 03:30
NSNS Refreshed by Heineken Silver
Asarri 22:00
Katalina b2b Muhi 00:00
Koboyo b2b Raven 02:00
Patrick Mason 04:00
Anetha 06:00
Gang Beats
Gang Beats Mixtape 20:00
Fich DJ Set 21:30
Viking Krew 22:30
Bulch 23:00
Keyri DJ Set 23:30
Micka Lifa x Rodjeni 01:15
Cunami Flo 02:00
Bolesna Braća 02:30
Bigru & Paja Kratak 03:15
Fox & Surreal 04:00
Purprose DJ Set 04:45
X-Bass Pit
Dozet & Lysergic 22:00
Kritik 23:30
Drumsta 00:30
State Of Mind 01:30
Bane 03:00
Vetas & Zooter 04:00
Wenti Wadada Positive Vibrations Reggae
Butchaa 20:00
Old Youth Selecta 21:15
DJ STK 22:30
Tommy T. 00:00
Deadly Hunta 01:15
King Calypso 02:00
Wenti Wadada closing party 03:30
Gaia Trance Stage
DJ Stole 21:00
DJ Zarma 00:00
Imaginarium live 02:00
DJ Mozza 04:00
Latino Stage by IDEA
DJ Beathoven 20:00
Latin Fitness Power 21:00
DJ Arceo 22:00
Pablo & Mauri 22:30
Orient Express 23:15
DJ Rey 00:00
Allegro 00:25
Salsa Y Punto 01:30
DJ`s b2b Tete vs Casanova 02:45
Urban Bug Stage
Zagi b2b Dimic 19:00
Deeman b2b Stiv 20:00
Ogun b2b Burakcan 21:00
Pinda b2b Darko Stanimirović b2b Emica 22:00
Mekhu b2b Machado b2b Aljoša 23:00
Hobin Rude b2b Igor D. 00:00
Rade Badjin b2b Poliformat 01:00
Luka Jukić b2b Miloš Drvenica 02:00
Antrax b2b Sofija 03:00
Mark Andersson B2b Novak Vuković 04:00
Essio b2b Aleksssa 05:00
Paragon b2b Impedance 06:00
Goran Kan b2b Lesya 07:00
Radio AS FM Stage
3.Sexty / Musse 20:00
Alex 22:00
Macro 23:00
Morning Indian 00:30
Ra5tik 02:00
Vanjanja 03:30
Pacho & Pepo 05:00
Official Afterparty
Goran Starčević 08:00
Special Guest 10:00
Pachamama Powered by ROSA
Conscious Dance with Nataša Stojkić 20:00
DJ Kalje Vest 22:15
The Durians 00:00
DJ/MC Killo Killo 01:00
Sounds of Zez 02:00
Together. X House by IQOS
Atsou 22:00
Le Croque 23:30
Awen live 01:00
Liva K 02:30
Coketails Zone
Mix 21:00
Iron & Chvare 22:00
"""

# Split the text into lines
lines = text.strip().split('\n')

# Create an empty list to store the stages and artists
concert_list = []

# Iterate over the lines and create dictionaries for each stage and artist

r = re.compile(r"\b\d{2}:\d{2}\b")

current_stage = None
for line in lines:
    if line.strip():
        time = r.findall(line)
        if len(time) == 0:
            current_stage = line.strip()
        else:
            artist = r.split(line)[0]
            normalized_artist = unicodedata.normalize('NFKD', artist).encode('ASCII', 'ignore').decode('utf-8')
            concert_list.append({"stage": current_stage, "artist": normalized_artist, "time": time[0]})

# Convert the list to JSON
json_data = json.dumps(concert_list, indent=2)

with open('lineup.json', 'w+', encoding='utf-8') as file:
    file.writelines(json_data)


from pprint import pprint

vk = {"KONKURENTSIVÕIMELINE MAJANDUSKESKKOND": [1,None],
"EELARVE": [2,1],
"MAKSUNDUS": [3,1],
"TÖÖTURG": [4,1],
"ETTEVÕTLIKKUSE EDENDAMINE": [5,1],
"TARISTU": [6,1],
"RIIGIMAJANDUS": [7,1],
"ÕIGUSKAITSE": [8,1],
"EKSPORDI ERGUTAMINE": [9,1],
"FINANTSKESKKOND": [10,1],

"PERESÕBRALIK RIIK": [11,None],

"HARITUD EESTI": [12,None],

"AKTIIVNE TÖÖTURUPOLIITIKA. SOTSIAALNE TURVALISUS": [13,None],

"TERVE EESTI": [14,None],

"ENERGIAJULGEOLEK": [15,None],

"TRANSPORT": [16,None],

"E-RIIGIST I-RIIGIKS": [17,None],

"TURVALINE EESTI": [18,None],
"ÕIGUSKORD": [19,18],
"ÕIGUSKAITSE": [20,18],

"KULTUURIPOLIITIKA": [21,None],

"SPORT JA KEHAKULTUUR": [22,None],

"EESTI KEEL JA MEEL": [23,None],

"LÕIMUMINE": [24,None],

"ILUS JA PUHAS EESTI": [25,None],

"MAAELU EDENDAMINE": [26,None],

"VÄLISPOLIITIKA": [27,None],

"RIIGIKAITSE- JA JULGEOLEKUPOLIITIKA": [28,None],

"KODANIKE RIIK": [29,None],
"PÕHISEADUS JA DEMOKRAATIA": [33,29],
"KODANIKUÜHENDUSED": [30,29],
"RIIGIHALDUS": [31,29],
"KOHALIK HALDUS": [32,29],
}

i=1

l = {}

txt = """KONKURENTSIVÕIMELINE MAJANDUSKESKKOND
Valitsusliidu majanduspoliitika eesmärk on Eesti inimeste elatustaseme tõus. Selle eelduseks on stabiilne majanduskasv ja konkurentsivõimeline majandusstruktuur – just neist sõltuvad uued töökohad, pensionitõus, teenused lastega peredele, turvalisus ja heal tasemel haridus. Eesti majanduskasvu võtmeks on edenemine ülemaailmses väärtusahelas – Eestis tehtu ja loodu peab muutuma oluliselt väärtuslikumaks ja konkurentsivõimelisemaks. Töö tootlikkus ja hind peab kasvama – vaid sellisel juhul saavad kasvada ettevõtlustulu ja palgad. Prioriteetseks on just inimeste sissetulekute kasv, mis pikemas perspektiivis tagab ka avalike teenuste osutamiseks vajalike vahendite piisavuse.
Riik panustab majanduskasvu atraktiivse ja usaldusväärse keskkonna loomisega: hariduse, teaduse ja kultuuri arendamisega, tööturupoliitika, taristu-, IT-, energia- ja transpordipoliitika, õiguspoliitika ja majandusdiplomaatiaga. Kõiki riigi ja kohalike omavalitsuste poolt ettevõetavaid samme, mis mõjutavad majanduskeskkonda, tuleb hinnata nende mõju alusel Eesti rahvusvahelisele konkurentsivõimele.
Riigi suur vastutus, mis võimaldab seda keskkonda rahastada, on elujõuline riigieelarve, stabiilne maksusüsteem, võimalikult madal ning majanduslikult mõistlikult jaotuv maksukoormus. Tuleb luua olukord, kus halbadele aegadele majanduses ei pea reageerima ühegi maksu tõstmisega.
Maksukoormuse alandamine ning teised konkurentsivõimet tõstvad meetmed peavad sõltuma eelarve struktuurse ülejäägi suurusest.
Valitsusliit viib läbi struktuurseid reforme ja poliitikaid, mis lähtuvad järgmistest põhimõtetest:
EELARVE
1. Eesti kui investeeringute ja uute töökohtade sihtmaa rahandusliku usaldusväärsuse süvendamine:
viime valitsussektori hiljemalt aastaks 2014 struktuursesse eelarve ülejääki ning hoiame seejärel ülejääki kõigil kasvuaastatel;
kasvatame reserve, mis lubavad võimalikud langusaastad valutult üle elada ka tulevikus;
lisame eelarve baasseadusesse valitsussektori eelarve tasakaalu nõude;
valitsussektori rahavoo ja võlakohustuste tõhusamaks juhtimiseks koondame järk-järgult valitsussektorisse kuuluvate juriidiliste isikute (v.a. kohalike omavalitsuste) vahendite arveldamise ja nende haldamise riigikassasse.
MAKSUNDUS
2. Lihtsa ja ühetaolise maksukeskkonna säilitamine:
jätkame lihtsa ja ettevõtlikkust soodustava ühetaolise üksikisiku tulumaksuga ning välistame astmelise tulumaksusüsteemi kehtestamise;
säilitame tulumaksuvabastuse ettevõttesse tagasi investeeritud kasumilt;
järgime põhimõtet, et sotsiaalvajadusi rahastatakse kogutud maksudest, mitte maksude kogumatajätmisest. Reformime erimärgistatud kütuse maksuerisuste süsteemi, pakkudes teatud valdkondades asemele otsetoetusi. Langetame 1. jaanuarist 2012 tulumaksusoodustuse ülempiiri 1920 euroni;
kaalume alkoholiaktsiisi kohaldamist ka kosmeetikatoodetes sisalduvale alkoholile.
3. Maksukoormuse vähendamine, sealjuures langetades ennekõike tööjõu makse kõrge tootlikkusega töökohtade tekkeks:
alates 2013 vähendame töötuskindlustusmakse määra;
kehtestame 1. jaanuarist 2014 sotsiaalmaksu (v.a. ravikindlustuse osa) lae: töötasu osalt, mis ületab 4000 eurot kuus ei maksta sotsiaalmaksu;
vähendame 1. jaanuarist 2015 tulumaksumäära 20%ni;
ei käsitle kulutusi tööga seotud tasemekoolituselt erisoodustusena;
koduomanike maksukoormuse vähendamiseks kaotame alates 1. jaanuarist 2013 maamaksu kodu alusele maale tiheasustusega kuni 1500m2 ja hajaasustusega piirkonnas kuni 2 ha ulatuses.
TÖÖTURG
4. Tööturu turvalise paindlikkuse suurendamine:
viime läbi eri- ja sooduspensionide reformi. Loome tööõnnetus- ja kutsehaiguskindlustussüsteemi, mis motiveerib töötajaid hoolima oma tervisest ja tööandjaid pakkuma oma töötajaile tervislikku töökeskkonda;
toetame tootlikkuse suurendamisele suunatud töötajate ümber- ja täiendõpet, ergutame ülikoole ja ettevõtjaid osalema senisest jõulisemalt täiendkoolituse turul, et viia elukestvas õppes osalemine Põhjamaade tasemele;
aktiivsete tööturumeetmete abil toetame puuetega inimeste algatusi luua koostöös ettevõtetega uusi töökohti;
analüüsime Töölepingu seaduse senist mõju eesmärgiga suurendada tööturu turvalist paindlikkust.
5. Investeeringuid ning rahvusvahelist äri ligitõmbava sotsiaalse keskkonna arendamine:
rakendame haridusprogrammi Põhjamaade tasemel kvaliteetse hariduse andmiseks, muuhulgas edendame Euroopa koole välisspetsialistide laste jaoks ja rahvusvahelist bakalaureuseõpet;
jätkame Eesti kujundamist turvalise ja perekeskse elukeskkonnaga riigiks;
edendame Eesti ühiskonna üldist avatust ja sallivust;
jätkame atraktiivse kultuurikeskkonna loomist Eestimaa erinevates piirkondades, mis aitab arendada turismivaldkonda;
Eesti majanduse konkurentsivõime tõstmiseks loome soodsa keskkonna välistudengite ja tippspetsialistide Eestisse tulekuks. See aitab Eestisse luua teadus- ja kompetentsikeskusi ning tagada ettevõtetele kõrgema kvaliteediga tööjõudu;
oleme vastu väheste oskustega võõrtööjõu massilisele sissetoomisele.
ETTEVÕTLIKKUSE EDENDAMINE
6. Turutõkete kõrvaldamine ja ausa konkurentsi tagamine:
võitlus kartellide ja monopolidega, kes takistavad konkurentide turulepääsu ja vähendavad sellega majanduse tõhusust ning tõstavad tarbijahindu, on riiklik prioriteet.
7. Bürokraatia ja aruandluse vähendamine:
vähendame bürokraatiat ja aruandlust, sealhulgas võimaldame alla 100 000 euro suuruse aastakäibega väikeettevõtetele mugava raamatupidamise äriregistri keskkonnas. Laiendame ettevõtjaportaali, lisades sinna mugava võimaluse käibemaksukohusluse ja kaubamärgi registreerimiseks;
lihtsustame äriühingute ümberkujundamise ja lõpetamisega seotud reegleid, et soodustada ettevõtlusaktiivsust ja juhtimisoskuste taaskasutamist;
viime läbi auditi Euroopa direktiividest tuleneva halduskoormuse minimeerimiseks Eesti seadusandluses.
8. Ettevõtluse õpe ja suurem väärtustamine:
väärtustame ettevõtjat ühiskonnas kui uue rikkuse loojat;
algatame üliõpilastele suunatud programmi „Hakka ettevõtjaks!";
viime ettevõtlusõppe põhihariduse õppekavasse ning tagame 2013. aastaks kõigile mittemajanduseriala tudengitele oma õppekava raames ettevõtlusõppe.
TARISTU
9. Energiajulgeoleku tagamine odavaima võimaliku hinnaga tarbijaile ja keskkonnale:
tagame ettevõtetele ja tarbijatele odavaima võimaliku hinnaga elektrivarustuse, mitmekesistades ja hajutades energiatootmist, ergutades rohkem kasutama kodumaiseid taastuvaid energiaallikaid ning vähendades sõltuvust julgeolekuriske sisaldavast energia sisseostmisest kolmandatest riikidest.
10. Eksporti ja ettevõtlust takistavate transpordi pudelikaelte kaotamine:
arendame lennuühendusi eesmärgiga, et Tallinnast saab kõigisse suurematesse Euroopa ärikeskustesse lennata põhimõttel „hommikul sinna, õhtul tagasi";
koostöös Poola, Läti, Leedu ja Euroopa Komisjoniga peame vajalikuks koostada ühiskava Baltimaade paremaks ja kiiremaks ühendamiseks Lääne-Euroopaga maismaad pidi (Via Baltica, Rail Baltica, Tallinn-Varssavi raudteeühendus jm.) ning analüüsime Tallinn-Peterburi reisirongiliini taasavamise otstarbekust.
11. Mugava äritegemise taristu edendamine:
liidestame riiklikud põhiregistrid (maakataster ja kinnistusraamat). Arendame registrite ristkasutust eesmärgiga viia andmete esitamisega seotud koormus ettevõtja jaoks võimalikult väikeseks;
katame Eesti ülikiire internetiühendusega; e-teenuste ja kogu IT sektori potentsiaali edasiarendamiseks ning ettevõtlusvõimaluste parandamiseks regioonides on oluline kaasaegse info- ja kommunikatsioonitehnoloogia taristu väljaarendamine;
oleme eestvedajaks Euroopa digiteenuste ühisturu väljaarendamisel, ennekõike digitaalse isikutuvastamise rahvusvahelise süsteemi rajamisel.
12. Teadmuspõhist loomemajandust toetava taristu edendamine:
jätkame investeeringuid riigi ja juhtivate kõrgkoolide osalusel loodud teadusparkide taristu arendamisse, et viia kokku innovatsioon ja ettevõtted;
toetame kunstide rolli suurenemist ettevõtluse mitmekesistamisel, sealhulgas disaini suuremat rakendamist tootearenduses. Muudame EASi toetusmeetmeid loomemajanduse eripäradele vastavaks;
loome tingimused rahvusvaheliselt tunnustatud tippspetsialistide palkamiseks strateegilistele erialadele Eesti ülikoolides;
kaasajastame intellektuaalse omandi õiguse.
RIIGIMAJANDUS
13. Võitlus reguleeritud hindadest tuleneva hinnatõusuga:
loome konkurentsi gaasi pakkumises, et vähendada sõltuvust Vene gaasist ning suruda alla gaasi ja toasooja hind Eesti ettevõtjatele ja tarbijatele;
vähendame taastuvenergia toetusi, kahjustamata investeerimiskeskkonda ja riigi poolt endale seatud keskkonnaeesmärkide saavutamist.
14. Riigivara tootlikkuse suurendamine:
viime avaliku sektori jaoks mittevajaliku vara tsiviilkäibesse. Kaalume kapitalituru normaalseks toimimiseks valitud riigiettevõtete osaluse noteerimist börsil. Lõpetame maa- ja omandireformi;
koondame alustava ettevõtluse riiklikud tugimeetmed ühtsesse, lihtsasse ja paindlikku programmi;
soodustamaks suuremahulisi investeeringuid, peame vajalikuks pikendada riigi poolt väljastatavate ressursilubade (vee erikasutusluba jne) kehtivuse tähtaegu.
ÕIGUSKAITSE
16. Õigusriigi ja õigussüsteemi toimivuse ning ärikeskkonna parandamine:
lähtume mistahes ärikeskkonna muudatuste kavandamisel õiguskindluse ning vastava valdkonna ettevõtluse esindajate kaasamise põhimõttest;
arendame kohtusüsteemi sihiga muuta õigusemõistmine kodanikele kiiremaks ja odavamaks:
kohtasjade menetlus ei tohi üheski kohtuastmes üldreeglina kesta üle 100 päeva. Loome uusi võimalusi kohtule alternatiivsete menetluste rakendamiseks. Kohtuotsuse täitmine peab olema tagatud;
täiustame maksejõuetusõigust ja täitemenetlust;
lihtsustame ja muudame läbipaistvamaks detailplaneeringute menetlemise ja ehitusloa saamise, sealhulgas vähendame bürokraatiat kodu remontimise ja soojustamise kavandamisel;
vaatame üle ärikeeldude kohaldamise regulatsiooni, eesmärgiga kõrvaldada turult ebaausad ettevõtjad;
korruptsiooni ennetamiseks ja tõkestamiseks kasutame kõiki sotsiaalseid, õiguslikke ja poliitilisi abinõusid;
vaatame kriitilise pilguga üle riigilõivud;
rakendame täiendavaid abinõusid võitluses maksupettuste ja maksudest kõrvalehiilimisega;
kaitsmaks paremini tarbijate huve muudame konkurentsiregulatsiooni tõhusamaks ja selgemaks. Suurendame Konkurentsiameti õigusi sekkuda olukordadesse, kus ettevõtted kuritarvitavad turupositsiooni või on vaba konkurents muul moel riivatud;
algatame EASis projekti, et teha äritegevuseks tarvilik seadusandlus inglise keeles kättesaadavaks.
EKSPORDI ERGUTAMINE
17. Ettevõtlustoetuste kasuteguri ning laenude ja garantiide osa suurendamine ekspordi
toetamisel:
maksumaksja rahast makstavatest ettevõtlustoetustest on kasu vaid siis, kui need parandavad Eesti majandusstruktuuri, mistõttu tuleb Arengufondi, EASi, Kredexi ja PRIA kaudu makstavate toetuste maht ja teravik suunata ennekõike alustavate ja eksportivate ettevõtete toetuseks;
innovaatiliste ja ambitsioonikate ettevõtete sünniks käivitame programmi Start-up Eesti;
riigieelarve vahendite piiratuse juures peame õigeks järk-järgult liikuda toetustelt laenude ja tagatiste kasutamisele ning keskenduda koostööd ja tootearendust ergutavatele meetmetele;
Eesti ettevõtete rahvusvahelistumise ergutamiseks analüüsime omakapitali (private equity) kättesaadavust ning vajadusel arendame edasi Sihtasutus Kredexi tooteportfelli ületamaks omakapitali pakkumisel esinevaid turutõrkeid.
18. Investeeringute ligimeelitamine ja Eesti ettevõtluskeskkonna jõulisem tutvustamine
välisturgudel:
seame eesmärgiks muuta Eesti rahvusvaheliste äride peakorteriks, regionaalseks meditsiini-, küberkaitse- ja messikeskuseks, tunnustatud loomemajanduse ja disainimaaks;
kaalume õigusliku raamistiku loomist pikaajaliste partnerluslepingute sõlmimiseks riigi ja Eestisse suuremahulisi välisinvesteeringuid toovate ettevõtete vahel;
aktiviseerime välisteenistuse toetust Eesti ettevõtetele välisturgudele sisenemisel ja tegutsemisel;
algatame eraldi programmi Aasia kapitali ja turistide meelitamiseks Eestisse.
FINANTSKESKKOND
19. Finantskeskkonna turvalisuse suurendamine:
ausa konkurentsi kindlustamiseks tugevdame järelevalvet panganduse ning pensionifondide tegevuse üle;
lihtsustame reegleid, et sisuliselt käivituks börs alternatiivse heade äriideede rahastamise allikana ka väike- ja keskmise suurusega ettevõtetele. Eesti elanikest peab saama omanikuühiskond ka ettevõtete omanikeks olemise kaudu.
20. Kindlustusturu edasiarendmine:
tegutseme sihiga laiendada kindlustustegevust oluliselt enam ka tervisest ning ajutisest või alalisest töövõimetusest ja maksejõuetusest tulenevatele riskidele.
PERESÕBRALIK RIIK
Valitsusliidu pere- ja rahvastikupoliitika eesmärk on luua Eestist peresõbralik riik, kus inimesed soovivad hea meelega lapsi saada ja kasvatada ning väärikalt vananeda, mis kindlustaks, et Eesti rahvast saab kasvav rahvas. Valitsusliit soovib, et Eestis sünniks lapsi veelgi rohkem. Eesti olgu parim paik elamiseks. Valitsusliit peab hooliva ja peresõbraliku ühiskonna kujundamist parimaks viisiks, mis soodustab võõrsil töötavate ja elavate Eesti juurtega haritud inimeste kodumaale naasmist. Perekeskse hea ja turvalise elukeskkonna loomiseks peab Valitsusliit oluliseks läbi viia poliitikat ja struktuurseid reforme, mis lähtuvad järgmistest põhimõtetest:
1. Toetava keskkonna edasiarendamine sündivuse suurenemiseks:
tagame vanemahüvitise süsteemi jätkumise – vanemahüvitis on üles ehitatud pere- ja tööelu ühitamise ja tasakaalu põhimõttel, mille muutmine ühes või teises suunas viib sündide vältimiseni ja emade olukorra halvenemiseni tööturul;
toetame raseduskriisi aegset nõustamist, eesmärgiga vähendada abortide arvu;
kehtestame 1. jaanuarist 2013 vanemapensioni – maksame 01.01.2013 ja hiljem sündinud lapse ühele vanemale lapse kasvatamise eest 4% riigi keskmiselt sotsiaalmaksuga maksustatavalt töötasult vanema II pensionisambasse kuni lapse 3-aastaseks saamiseni (välja arvatud vanema tööl käimise aeg). Tagamaks põlvkondade vaheline solidaarsus, maksame 01.01.1991-31.12.2012 sündinud lapse ühele vanemale pensionilisa kahe aastahinde väärtuses. 1. jaanuarist 2015 maksame enne 01.01.2013 sündinud lapse ühele vanemale täiendavat pensionilisa ühe aastahinde väärtuses.
2. Kindlustunde tagamine peredele lapse kasvatamiseks ka pärast vanemahüvitise perioodi lõppemist:
peretoetuste maksmisel peab edaspidi kehtima põhimõte, et toetatakse rohkem neid, kes reaalselt rohkem abi vajavad ja kel on rohkem lapsi;
perede aitamisel eelistame mõistlikku tasakaalustatud süsteemi teenuste pakkumise, universaaltoetuste ja otseste rahaliste toetuste vahel;
jätkame lasterikaste perede kodutoetuse programmi, majanduslike võimaluste tekkimisel kehtestame tugisüsteemi lasterikastele peredele ja üksikvanematele;
peame õigeks, et ühe pere lastel on õigus käia samas lasteaias;
koondame omavalitsuste infokeskkonnad ühtsesse lapsehoiu infosüsteemi, et lapsevanematel oleks mugav ja lihtne leida sobiv lastehoiuvõimalus;
jätkame koolilõuna riiklikku toetamist põhikoolis, väärtustame tervislikku ja värsket, kohapeal kohalikust toorainest valmistatud toitu.
4. Pere- ja tööelu ühitamise võimaluste edasiarendamine:
jätkame lapsehoiuvõimaluste paindlikumaks muutmist, et aidata vanemad kiiremini tagasi tööturule ja seeläbi suurendada perede sissetulekuid;
arendame lastehoiuteenuse kõrval ka teisi peredele suunatud teenuseid ning väärtustame peresõbralikkust ühiskonnas tervikuna. Peresõbralike ettevõtete riiklikuks tunnustamiseks kehtestame peresõbraliku ettevõtte tunnistuse – nii teab iga lapsevanem töökohta valides, kus tema väärtust hinnatakse ja vajadusi mõistetakse;
taastame isapuhkuse.
5. Huvihariduse edendamine: noorte huvitegevuses osalemise suurendamiseks ja riskikäitumise vähendamiseks kehtestame 1. jaanuarist 2014 ringiraha.
6. Kodussünnitamise täpsem seadustamine: oleme seisukohal, et pere soovi korral ja vastunäidustuste puudumisel võib naine valida sünnitamiseks ämmaemanda või naistearsti juuresolekul ka oma kodu või muu sünnitamiseks sobiva paiga.
7. Tugi lastetutele peredele, kes soovivad lapsi:
toetame lastetusravi, et tagada võrdne võimalus lapse saamiseks ka neile, kellel meditsiinilise sekkumiseta see võimalus puuduks;
vähendame lapsedamisega seotud bürokraatiat, et üha enam asenduskodudes elavaid lapsi jõuaksid senisest kiiremini sobivatesse peredesse.
8. Laste õiguste tõhus kaitsmine:
laste õiguste ja ka kohustuste paremaks reguleerimiseks kehtestame ja rakendame tänapäevase lastekaitseseaduse;
abi osutamise tõhustamiseks lapsele ja perele pöörame tähelepanu varajase märkamisele ja sekkumisele;
peame oluliseks peredele pakutavate sotsiaalteenuste kvaliteedi tõusu.
9. Vanemahariduse ja perenõustamise kättesaadavuse parandamine:
soovime ühiskonnas rohkem väärtustada paremate peresuhete kujunemist, sest noorte eluhoiakute areng, sealhulgas ennasthävitava riskikäitumise vältimine on otseses seoses peresuhete püsivuse ja kvaliteediga;
soovime tõhusama nõustamise teel ennetada paarissuhete (nii abieluliste kui vabakooseluliste) purunemist ja toetada senisest enam vanemaharidust;
kooliprogramm peab senisest suuremat tähelepanu pöörama pereväärtustele ja riskikäitumise vältimisele. Toetame seksuaaltervise ning vanemluse alast haridust põhikoolis ja gümnaasiumiastmes.
HARITUD EESTI
Eesti püsimise võti on haritud rahva käes, seetõttu on haridusvaldkond eelseisvate aastate prioriteet. Tahame viia Eesti hariduse Põhjamaade tipptasemele – meie eesmärk on haritud rahvas ja edukas Eesti.
Hea haridus tähendab inimese jaoks suuremat palka, paremat kaitset töötuse vastu ja suuremat pensioni tulevikus. Võimalus saada maailmatasemel haridust annab peredele suurema kindlustunde laste saamisel. Parem haridus tagab tervislikuma ja õnnelikuma elu. Valitsusliit soovib ehitada jõukat Eestit, mis on Läänemere regioonis hästi lõimitud, kõrgtehnoloogiale tuginev ning ekspordile orienteeruv suurte investeeringute sihtriik. Sellise Eestini jõudmiseks on möödapääsmatu jätkata haridussüsteemi ümberkorraldustega.
Valitsusliit näeb Eesti tuleviku võtit heas ja kättesaadavas hariduses.
Et pakkuda rahvale parimat, seame hariduskorralduses ja õppesisus järgmised sihid:
1. Igale lapsele lastehoiuteenuse ja kvaliteetse alushariduse omandamise võimalus:
seame eesmärgiks, et alushariduse omandaks koolieelsetes lasteasutustes ja koolide ettevalmistusklassides vähemalt 95% lastest. Jätkame lasteaiakohtade loomist ja lasteasutuste energiasäästlikkuse parandamist Euroopa Liidu struktuurifondide KOIT kava ning Kyoto saastekvootide müügist laekuvate vahendite toel. Vähendades erinevusi kooliminejate ettevalmistuses väldime hilisemat haridustee katkemist;
alus- ja põhihariduses peab keskenduma õppimisoskuse, iseseisva mõtlemise, loovuse ja õpijulguse kujundamisele. Õppe ja kasvatusalal on oluline väärtustel põhinev tegevus;
lapsekeskse lastehoiuteenuse rakendamiseks seame pikaajaliseks sihiks õpetajate (sh eripedagoogide) arvu suurendamise lasteaialapse kohta.
2. Kaasaegsem ja kvaliteetsem üldharidus:
rakendame uue õppekava, mis vähendab õpilaste õppekoormust põhikoolis ja annab neile selle kõrval rohkem võimalusi loominguliseks tegevuseks. Peame väärtuskasvatust koolielu lahutamatuks osaks;
kindlustame õpilastele koolides parimad tingimused arenemiseks. Peame oluliseks õppekeskkonna parandamist loodusainetes, matemaatikas, tehnoloogia- ja teadusõppes;
õppetöö mitmekesistamiseks ja haridusele parema ligipääsu tagamiseks, võtame kasutusele seda lihtsustavaid uusi tehnoloogiaid. Laiendame e-õppe võimalusi, et kergendada koolikotti ja vanemate osalust õpiprotsessis. Loome e-gümnaasiumi, kuhu koondame akadeemilise õppevara ja kust nii koolid kui õpilased saavad kursusi alla laadida;
soodustame lastevanemate suuremat osalust õppeprotsessis ning võimaldame koolide juures selleks vajalikku ettevalmistust;
viime miinimumini varase koolist väljalangevuse, ajutised kõrvalejääjad toome kooli tagasi;
soosime vabahariduslikku tegevust ja alternatiivpedagoogikate kasutamist, kui see annab osale õpilastest võimaluse õppida just neile sobivas keskkonnas.
3. Õpetajakutse väärtustamine, et õpetajateks saaksid parimad:
toimiva kutsevaliku ja korraliku, harjutuskoolidele tugineva õpetajakoolituse abil ülikoolides, saavutame, et õpetajaamet oleks ihaldusväärne meie parimatele ülikoolilõpetajatele;
jätkame 12 782 eurose õpetaja lähtetoetuse maksmist noortele alustavatele õpetajatele;
pakume õpetajakutse valikut aktiivselt juba alates gümnaasiumist, lähtudes „Noored kooli!" ja teiste sarnaste projektide kogemusest. Tagame õpetajatele kõrgetasemelise baas- ja täiendkoolituse. Õppekava kvaliteedi tagamiseks sätestame, et haridus- ja teadusministeerium saab õiguse välis- ja sisehindamise tulemuse alusel hinnata koolijuhtide pädevust.
4. Mõistliku koolivõrgu kujundamine:
keskendumine hariduse sisule ning omandivormide vabadus ja võrdsus on eelduseks Eestile sobivaima haridusvõrgu kujunemisel. Tagame õpilastele ka edaspidi võrdse juurdepääsu kvaliteetsele kooliharidusele;
toetame maakonnagümnaasiumide väljaarendamist kõigis maakonnakeskustes nn puhta gümnaasiumina, vajadusel riigigümnaasiumina;
pakume rahvusvahelistele tippspetsialistidele võimalust panna oma lapsed Euroopa Kooli ning saada rahvusvahelist bakalaureuseõpet Inglise Kolledžis ja Miina Härma Gümnaasiumis.
5. Vähemusrahvustest õpilaste edukas lõimimine kvaliteetset haridust andvasse haridussüsteemi, eesti keele õpe kõigile:
kindlustame tasemel eesti keele õppe muukeelsetes lasteaedades, põhikoolides ja kutsekoolides. Selleks laiendame keelekümblusprogrammi kasutamist;
viime lõpule vene gümnaasiumide ülemineku eesti õppekeelele. Aitame omavalitsustel moodustada tugevaid vene õpilaskonnaga, kuid hea eestikeelse õppega nn vene lütseume;
laiendame Ida-Virumaal eesti keeles õpetavatele õpetajatele 30% lisatasu maksmist;
pakume jätkuvalt tasuta eesti keele õppimise võimalusi;
laiendame eesti keele õppimise võimalusi teiste riikide haridusasutustes;
kindlustame vähemuskeelsetes põhikoolides kõrgel tasemel eesti keele, kultuuri, ajaloo ja ühiskonnaõpetuse õpetamise.
6. Kutseõppe kui haridusvaliku taseme ja populaarsuse tõstmine:
ehitame kaasaegsel tasemel välja kõigi kutsekoolide õppekompleksid ja ühiselamud;
Kutsekoolidest peavad saama kohalikud kompetentsikeskused, millel on laiem roll kogu piirkonna arendamisel;
loome kutsekoolides võimaluse täiendavaks õpilaste vastuvõtuks;
soodustame üld- ja kutsehariduslike õppeasutuste koostööd ning enesetäiendusvõimalusi kutsehariduse läbinutele, kes soovivad jätkata haridusteed kõrgkoolis. Selleks võimaldame kutsekooli õpilastel omandada soovi korral üldaineid gümnaasiumi omadega sarnases mahus;
kutsekoolilõpetaja peab kooli lõpuks suutma omandada tööandjaid rahuldava kutsekvalifikatsiooni.
7. Elukestvas õppes osalemise suurendamine:
seame elukestva õppe projektide rahastamise Euroopa Sotsiaalfondi vahendite kasutamise prioriteediks. Lisaks sellele peame oluliseks noorsootööprojektide rahastamist. Haridussüsteemi tagasipöördumine ei ole ühelegi inimesele takistatud või ülemäära keeruliseks muudetud;
elukestvas õppes osalevate täiskasvanute osakaalu suurendamiseks ühiskonnas tänaselt 12%-lt 20% tasemele ei käsitle kulutusi tööga seotud tasemekoolituselt erisoodustusena;
vanemate sissemaksed oma lapse haridusfondi või -kindlustusse saab jätkuvalt maha arvata isiku maksustatavast aastatulust.
8. Tasuta ja tipptasemel kõrgharidus:
seame kvaliteedi kõrghariduskorralduse läbivaks eesmärgiks. Soovime, et kõrghariduse kvaliteet oleks ühiskonna üldise tähelepanu ja avaliku debati keskmes, muuhulgas toimiks teadusuuringute kaudu Eesti haridusseisu järjepidev seire;
loome võimaluse saada tasuta kõrgharidust Eestis kõigile võimekatele noortele. Selleks võtame 2011. aastal vastu seaduse, millega suurendame aastatel 2012-2014 avalik-õiguslikele ülikoolidele või rakenduskõrgkoolidele riiklikku tellimust 40 % võrra, tagades sellega õppemaksuta õppe kuni 12 500 sisseastumistingimused täitvale üliõpilasele eestikeelsetel õppekavadel ühe erialadiplomi omandamiseks nominaalaja jooksul. Õppetöö kvaliteedi tõstmiseks muudame riikliku koolitustellimuse jaotust;
käivitame 1. jaanuarist 2015 vajaduspõhise õppetoetuste süsteemi ja tõstame õppeedukust arvestavaid riiklike stipendiume;
seisame selle eest, et kõrghariduse struktuuriuuenduseks saaks muuhulgas kasutada ka 2014. aastal algava Euroopa struktuurifondide uue rahastamisperioodi vahendeid;
loome magistrandidele suurema võimaluse panna kokku isikupärane õpingukava erinevate ülikoolide parimaist kursusist. Doktorandid hakkavad nooremteaduritena saama palka, mis on suurem seni makstud stipendiumist;
säilitame riiklikud toetused väikestele humanitaarteaduslikele erialadele ülikoolides. Arvestame humanitaarteaduste, sealhulgas ka rahvusteaduste erilaadsusega.
9. Kasvab ühiskonna panustamine teadus- ja arendustegevusse ning rahvusvahelisse teaduskoostöösse:
seame sihiks jõuda teadus- ja arendustegevuse rahastamisel 3%-ni SKTst, sealhulgas erasektori osaluseni vähemalt 2/3 ulatuses sellest. Jätkame teaduse populariseerimist;
muudame teaduse rahastamise süsteemi selgemaks, st säilitame teadusasutuste baasfinantseerimise ja loome projektitoetuste jagamiseks kahe asutuse asemel Eesti Teadusagentuuri. Kehtestame teaduse rahastamisel teadlaste karjäärimudeli. Isikukeskne teaduse rahastamise süsteem on asendunud konkurentsikesksega – teadusasutuste rahastamine sõltub teadustulemustest, mitte olemasolevate teadlaste arvust. Soodustame igakülgselt Eesti teadlaste osalemist rahvusvaheliste teaduskeskuste töös, samuti ülikoolide, riigi ja erasektori koostööd ning ettevõtjate keskendumist tootearendusele;
jätkame teaduse ja kõrghariduse taristu välja arendamist.
AKTIIVNE TÖÖTURUPOLIITIKA. SOTSIAALNE TURVALISUS
Valitsusliidu tööturu- ja sotsiaalpoliitika eesmärk on inimeste sissetulekute, elukvaliteedi ning sotsiaalse turvalisuse kasv. Väärtustame riigi hea majandusarenguga kaasnevaid kõrgemaid sissetulekuid, tegelikele vajadustele vastavaid inimväärseid toetusi ja väärikat vananemist.
Selleks, et jätkuks inimeste sissetulekute kasv, paraneks elukvaliteet ja sotsiaalne turvalisus, viib Valitsusliit ellu poliitikaid ja struktuurseid reforme, mis lähtuvad järgmistest põhimõtetest:
1. Stabiilne pensionitõus:
pensionitõusu eelduseks on aruka ja konservatiivse majandus- ja rahanduspoliitika jätkamine, mis kindlustab majanduskasvu ning uued töökohad;
väärtustame sotsiaalselt aktiivset elu, mis tagab pensionile jäädes suuremad sissetulekud ning loob kõigile võimaluse töötada nii kaua kui ise soovitakse.
2. Põhitähelepanu noorte ning pikka aega tööturult eemal olnute tööpuuduse vähendamisele:
inimeste parim võimalus tööturul edukas olla seisneb heas hariduses. Seetõttu pöörame enim tähelepanu inimeste hariduse ja kutseoskuste tõstmisele, mis võimaldavad neil tööturul taotleda paremaid tingimusi ja palka;
jätkame TULE ja KUTSE programmidega, et haridustee kõrg- või kutsehariduses katkestanud saaksid tööturult tagasi pöörduda hariduse omandamise juurde;
jätkame ja arendame tööturu olukorrast sõltuvalt aktiivseid tööturumeetmeid, muuhulgas palgatoetust, tööpraktikat, ettevõtluse alustamise toetust, erialase ettevalmistuseta inimeste koolitamist jmt;
parandame töötukassa võimet aidata inimesi uue töökoha leidmisel, pakkudes kiiremat teenust, tänapäevaseid IT-võimalusi ning personaalsemat lähenemist;
toetame pikka aega lastega kodus olnud emade tööturule tagasipöördumist;
tagame noortele karjääriõppe –ja nõustamise üldharidus- , kutse- ja kõrghariduse tasemel;
Ida-Virumaa pikaajalise töötuse leevendamiseks pakume EAS-i kaudu individuaalseid suuremahuliste tööstusinvesteeringute toetamise pakette, mis aitaksid luua uusi töökohti regioonis.
3. Elukestva õppe ja töötute ümberõppe vahendite suurendamine:
tõstame elukestvasõppes osalemist 20%ni ning ümberõppes osalevate madalama haridusega isikute arvu;
jätkame riigi toel kutseõppe programmi 16-29 aastastele põhiharidusega või põhihariduseta töötutele. Toetame Euroopa Sotsiaalfondi pilootprojekti ülemaalist rakendamist, et anda täiskasvanutele tööalast koolitust kutseõppeasutustes.
4. Puuetega inimeste elukvaliteedi parandamine:
hindame kodanikuühiskonna väärtust ja peame vajalikuks puuetega inimeste esindusorganisatsioonide suuremat kaasamist riiklikku otsustusprotsessi;
parandame puuete määramise süsteemi korraldust ning vähendame rehabilitatsiooniga seonduvat bürokraatiat;
algatame puuetega inimeste tööhõive programme. Viime läbi Töötukassa tööturumeetmete revisjoni, et need soodustaksid puudega inimese töösuhet ja oleksid paindlikud. Kaardistame puude liikide kaupa valdkonnad, kuidas laiemalt rakendada ja koolitada inimesi;
seame eesmärgiks ratifitseerida ÜRO Puuetega Inimeste Konventsioon.
5. Investeeringute suurendamine hoolekandeasutustesse: riigi poolt hallatavate erihooldeasutuste ja asenduskodude renoveerimesel lähtume põhimõttest, et ehitatakse tänapäevased peremaja tüüpi külad, kus abivajajatele saab pakkuda parimat hoolitsust.
6. Igale vajajale võimalikult võrdväärse abi tagamine: kehtestame riiklikult loetelu minimaalselt vajalikest sotsiaalteenustest ja nende kvaliteedinõuded (standardi), mida iga omavalitsus peab inimestele pakkuma.
7. Võimaluste loomine paindlikumaks ja kvaliteetsemaks elukorralduseks pensionipõlves:
edendame koduhooldust ja telemeditsiini ning loome täiendavaid võimalusi eakate kvaliteetseks päevahoiuks.
TERVE EESTI
Valitsusliidu tervishoiupoliitika eesmärk on Eesti inimeste pikem ja tervem elu ning kvaliteetne arstiabi terviseprobleemide korral. Valitsusliidu silmis on eluea üldisest pikkusest veelgi olulisem just tervena elatud aastate arv, mis on viimase viie aastaga kasvanud rohkem kui viie aasta võrra.
Nüüdismeditsiin suudab pakkuda kvaliteetset abi, kui inimene seda vajab, aga inimestel endil on võimalus väga palju teha oma tervise säilimise või parandamise eesmärgil. Tervislik toitumine ja piisav kehaline aktiivsus on hea tervise alused.
Eestis pakutav tervishoiuteenus on Euroopa võrdluses heal tasemel, kuid sellele vaatamata soovib Valitsusliit astuda samme arstiabi veelgi paremaks muutmiseks.
Valitsusliidu nägemuses on parem rahvatervis ja tervishoid saavutatav, kui viia ellu järgmistest põhimõtetest lähtuvad poliitikad ja struktuursed reformid:
1. Inimeste eeskujuliku tervisekäitumise toetamine:
edendame tervislikke eluviise, kaasajastame Rahvatervise seaduse. Tunnustame riiklikult terviseedendajaid;
suurendame korrapäraste tervisekontrollide mahtu nii lastele kui täiskasvanutele, samuti erinevate tervisejälgimis- ja sõelumisprogrammide läbiviimist;
Eesti tippkokki kaasates julgustame Eesti inimesi juba lasteaiast ja koolist alates tervislikult toituma, kasutama toidu valmistamisel kodumaiseid ja mahetoidu tooraineid ning tõstma üldist toitumiskultuuri;
seame eesmärgiks vähendada vigastussurmade hulka vähemalt Euroopa keskmise tasemeni, rakendades pidevat erinevate valdkondade vigastussurmade ennetamise poliitikat.
2. Igaüks peab saama valida talle sobivaima tervishoiuteenuse:
toetame patsientide vaba liikumist, võtame initsiatiivi regionaalses koostöös vaba liikumise rakendamisel ning arendame Eesti patsientide vaba liikumist toetavate infosüsteeme;
selleks, et avardada Eesti-siseselt patsientide valikuvõimalusi raviteenuste saamiseks peame õigeks ravi pakkuvate teenuseosutajate paljusust ja raviks ettenähtud rahaliste vahendite suuremat sidumist patsientidega;
tervishoiuteenuse tagamiseks kõikjal Eestis loome erasektoriga koostöös asendusperearstide süsteemi, mis tagaks perearsti olemasolu igale elanikule ka siis, kui oma perearst puhkab või tekib muu ettenägematu takistus teenuse osutamiseks raskesti ligipääsetavates paikades.
3. Ravimid on odavamad ja paremini kättesaadavad:
arendame koostööd nii Euroopa Liidu kui muude riikidega, et tagada suurem ravimite valik Eestis;
tugevdame riigi võimet pidada läbirääkimisi ravimite hinna kujundamisel ja järelevalve teostamisel;
kaasajastame ravimipoliitika. Ravimite kättesaadavuse parandamiseks ja omaosaluse vähendamiseks analüüsime kehtivaid piiranguid. Kaalume apteegibussi teenuse sisseseadmist ning digiretsepti süsteemi loodud eelduste ärakasutamiseks seadustame ravimite ostmise võimaluse traditsioonilise apteegi osana toimiva e-apteegi kaudu.
4. Tervishoiu rahastamise mitmekesistamine ja tõstmine rahakasutuse parema sihituse teel:
analüüsime ja kaalume tänase süsteemi muutmist selliselt, et inimeste ravikindlustuseks mõeldud raha läheks valdavalt raviteenuste rahastamiseks;
toetame tervishoiu rahastamise mitmekesistamist, suurendades võimalusi vabatahtlikuks tervisekindlustuseks;
toetame perearstitöö kvaliteedi parandamisele suunatud lisatasusüsteemi rakendamist võimaldamaks perearstidel palgata lisaõde, et muuta tõhusamaks perearstide tegevus haiguste ennetamisel ja krooniliste haigete jälgimisel.
5. Arstiabi korralduse ajakohastamine:
uuendame nii riikliku südamestrateegia kui ka vähistrateegia, sealhulgas rajame võrgustikupõhise vähiravisüsteemi;
anname perearstidele suuremad võimalused inimeste tervisliku käitumise suunamisel, suurendame noorte arstide riiklikku tellimust ning parandame arstiabi kvaliteeti;
toetamaks maakonnakeskuste haiglatesse noorte arstide tööleasumist, maksame noorele arstile esimese residentuuri lõpetamise järgselt tööle asumisel kohalikku või üldhaiglasse 15000 euro suurust lähtetoetust;
rajame Tallinnas laste vaimse tervise keskuse.
6. Eakatele suunatud teenuste arendamine: tagame eakatele paremad hooldusravi ja koduõenduse võimalused. Demograafilisest seisundist tulenevalt eelistame rahastada hooldusravi ennaktempos ning rajame igasse maakonda kaasaegsed hooldusravikeskused.
7. Patsientide teadlikkuse tõstmine:
peame õigeks, et patsiendiga seotud ravijuhu maksumus oleks patsiendile nähtav riigiportaali kaudu;
suurendame patsienditeadlikkuse tõstmisega (nagu näiteks koopia- ja originaalravimite võrdlemine) seotud programmide mahtu;
peame vajalikuks kiirelt rakendada terviseteadlikkuse õpe uue riikliku õppekava mahus. Esmaabi ja elustamise põhiteadmised peavad olema selgeks saanud juba põhikoolis.
8. Tõhus võitlus ühiskonda hävitavate nakkushaiguste, alkoholismi, tubaka ja narkomaaniaga:
pöörame eelkõige tähelepanu noorte riskiteadlikkuse tõstmisele;
HIV-nakkusega võitlemisel on riigi prioriteet uute nakatunute arvu vähendamine, pöörates erilist tähelepanu noorte ennetusmeetmetele;
narkomaanidega tegelemisel kasutame lisaks olemasolevatele ravimeetoditele senisest enam personaalsemat lähenemist ja vajadusel narkomaania võõrutusravi alternatiivseid meetodeid;
alkoholi ja tubaka tarvitamise vähendamiseks vaatame üle riikliku alkoholi- ja tubakapoliitika ja karmistame karistusi nende alaealistele kättesaadavaks tegemise eest. Arendame välja alkoholi liigtarvitamise varajase avastamise ja nõustamise süsteemi, et ennetada kroonilise alkoholisõltuvuse väljakujunemist ja tagada ravi ning rehabiitatsiooniteenused motiveeritud alkoholist loobujatele.
9. Kõikide saarteelanike kindlustamine kvaliteetse arstiabiga: lisaks perearstiteenuse tagamisele kindlustab riik kõikide kõrgema tähtsusega väljakutsete puhul saartele helikopteriteenuse olemasolu.
10. Tervishoiuteenuste ekspordi ja meditsiiniuuenduste edendamine:
peame vajalikuks Eesti meditsiini- ja infokommunikatsioonitehnoloogia oskusteabe tugevamat ühendamist riigi ja juhtivate ülikoolide poolt loodud teadusparkides, mis aitab viia Eesti meditsiiniinnovatsiooni uuele tasemele. Riik saab seda toetada investeeringutega teadusparkide taristusse ning EASi toel Eesti meditsiiniuuenduste rahvusvahelist turundustegevust koordineerides.
ENERGIAJULGEOLEK
Valitsusliidu energiapoliitika eesmärk on Eesti energiajulgeoleku kindlustamine odavaima võimaliku hinnaga Eesti tarbijatele ja keskkonnale. Kindel, taskukohane ja puhas energiavarustus tugevdab Eesti ettevõtete konkurentsivõimet ning loob eeldused suuremaks majanduskasvuks ja uute töökohtade tekkeks. Energia säästmine ja tõhusam kasutamine on olulised vahendid energiajulgeoleku saavutamisel odavaima võimaliku hinnaga.
Valitsusliit näeb energeetikat Eesti arengu ühe võtmevaldkonnana mitte üksnes julgeoleku, vaid ka Eesti ekspordivõime kasvatamise seisukohalt. Energiast ja meie unikaalsest tehnoloogilisest oskusteabest energiatootmise vallas peab saama oluline Eesti ekspordiartikkel, majanduse, töökohtade ja sissetulekute kasvu allikas.
Nende eesmärkide saavutamiseks soovib Valitsusliit läbi viia poliitikat ja struktuurseid reforme, mis lähtuvad järgmistest põhimõtetest:
1. Energiasõltumatuse hoidmine ka pärast 2016. aastat:
Eesti peab jõuliselt jätkama energiaallikate portfelli mitmekesistamist ning säilitama energiasõltumatuse tänasel määral ka pärast 2016 aastat, st et ülekaalukas osa Eestis tarbitavast energiast toodetakse kodumaistest energiaallikatest või Eestis;
valmistame ette tuumaenergia kasutuselevõtu eelduseks oleva seadusandluse ning viime läbi erapooletud tasuvusuuringud ja keskkonnamõju hinnangud Eesti oma tuumajaama rajamise otstarbekuse hindamiseks. Tuumatehnoloogia, mida Eesti riik lubab oma territooriumil kasutada, peab olema kaasaegne ja turvaline. Seetõttu lähtuma Euroopa Komisjoni soovitusest ja lubame üksnes kolmanda või sellest kõrgema põlvkonna tuumareaktori kasutamist. Eesti võimalik tuumaenergia programm peab sisaldama kohalike spetsialistide väljaõpet ning tagama maksimaalse ohutuse ja ausad turutingimused. Eesti võimalikus tuumajaamas saavad soodsate ja stabiilsete elektrihindade tagamiseks ning töökohtade loomiseks võimaluse osaluse omandamiseks ka Eesti tööstuslikud elektritarbijad;
näeme perspektiivi kodumaiste vedelkütuste tööstusel vähendamaks sõltuvust vedelkütuse impordist.
2. Rahvuslikku julgeolekut suurendavate ühenduste ja taristute rajamine:
Eesti energiajulgeoleku suurendamiseks liidame Eesti elektrivõrgud Kesk-Euroopa sünkroonalaga;
arendame edasi ühendusi Põhjamaade ja Lätiga, esmajärjekorras ehitame valmis Estlink 2;
Eesti gaasivarustuskindluse suurendamiseks ja konkurentsi tekitamiseks gaasiturul viime läbi gaasivõrgu omandilise lahutamise;
Soome ja Balti riikide turgude sidumiseks üheks atraktiivseks gaasituruks käsitleme prioriteetse ülepiirilise energeetika taristuprojektina BalticConnectori ehitamise ettevalmistamist, milleks taotleme kaasrahastamist Euroopa Liidu uuest eelarveperspektiivist. Jätkame tööd LNG terminali Eestisse rajamise ettevalmistamiseks;
Eesti osaleb aktiivselt Balti energiaturu integratsiooniplaani (Baltic Energy Market Interconnection Plan) väljatöötamisel ja elluviimisel ning suurendab energiakoostööd Põhjamaadega;
muudame seadusandlust, et kiirendada suurte taristuprojektide puhul maakasutuse lubade menetlemist.
3. Selgete elektrikaubanduse reeglite kehtestamine Euroopa Liidus kolmandate riikidega:
seisame kolmandatest riikidest pärineva elektrienergia importimisel Euroopa Liidu ühtsete reeglite kehtestamise eest, ennekõike keskkonnanõuete ja ausa hinnakonkurentsi osas.
4. Kütte- ja elektriarveid vähendavate programmide rakendamine:
jätkame energiasäästuprogramme, sealhulgas kortermajade soojustamise programmi (võimalusel rakendades neid ka väikeelamutele), mille tulemusel Eesti inimesed ja ettevõtted saavad oluliselt vähendada oma kütte- ja elektriarveid ning elada keskkonnasõbralikumat elu. Suuname CO2 kvootidest riigile laekuva tulu energiasäästu investeeringuteks;
riik peab näitama eeskuju, rajades uued avaliku sektori hooned energiasäästlikena;
töötame välja meetmed, et rajatavad hooned vastaks parematele energiastandarditele.
5. Kodumaiste väiksema keskkonnamõjuga energiaallikate eelistamine majanduse konkurentsivõimet kahjustamata:
peame oluliseks suurendada Eesti energiatootmise ja -tarbimise portfellis kodumaiste taastuvate energiaallikate ning vähendada suure süsinikujäljega energiaallikate osakaalu;
räägime läbi tootjatega taastuvenergia toetuste määra vähendamiseks olemasolevate projektide osas, pidades silmas õiguskindluse põhimõtet, Eesti energiapoliitika eesmärke ning võimalikult väikest mõju tarbija rahakotile. Vaatame üle taastuvenergia toetuste määra uutele projektidele, diferentseerime need energiaallikate lõikes ning seame sõltuvusse elektri turuhinnast;
transpordist lähtuva saaste vähendamiseks soodustame mittefossiilsete kütuste kasutamist ning lokaalse saaste piiramiseks loome vastavate Euroopa Liidu standardite kehtestamisel elektriautode laadimiskohad suuremates Eesti keskustes;
soojusenergia tootmisel eelistame tõhusat koostootmist;
Eesti peab aktiivselt osalema Euroopa Liidu süsinikpoliitika kujundmisel ja rohesertifikaatide turul. Energiasertifikaatide turu käivitumine võimaldab Eestil jätkata energiaportfelli mitmekesistamist taastuvenergia allikatega, kahjustamata samas Eesti tarbijate rahakotti ja ettevõtete konkurentsivõimet.
6. Julgeoleku tagamiseks vajalike energiatootmisvõimsuste rajamine odavaima võimaliku hinnaga tarbijale ja keskkonnale:
energiatootmisvõimsuste kavandamisel eelistame energiaallikate mitmekesisust ja pikaajalist konkurentsivõimet, sealhulgas Euroopa keskkonnapoliitika valguses.
7. Põlevkivist Eesti jaoks saadava väärtuse oluline kasvatamine:
eelistame meie olulisima maavara suuremat väärindamist, sealhulgas põlevkiviõlitööstuse arendamist ning Eesti unikaalsete põlevkivialaste tehnoloogiliste teadmiste ja oskuste eksporti;
kaalume põlevkiviõli tootmisel põlevkivi riigitulu (royalty) põhimõtte rakendamise otstarbekust. Põlevkivi riigitulu suurus sõltub nafta maailmaturuhinnast ning arvestab tootjaettevõtte pikaajalisi äririske.
8. Energiatõhususe suurendamine läbi teadamispõhise energeetika ja targa elektrienergiakasutuse (nutivõrgu) edendamise:
peame oluliseks teadmispõhise majanduse edendamist energeetikas, tehnoloogiliste lahenduste arendamist ja oskusteabe eksporti (nt põlevkivienergeetikas). Jätkame energiatehnoloogia programmi;
väärtustame intelligentsete elektrisüsteemide arendamist, mille tulemusel suureneb elektrienergia varustuskindlus ja elektrienergia kasutuse efektiivsus ning väheneb keskkonna saastamine.
TRANSPORT
Valitsusliidu transpordipoliitika eesmärk on kindlustada inimeste ja kaupade vaba, mugav, kiire ja taskukohane liikumine Eestis ning Eesti ja muu maailma vahel. Hästi korraldatud transport parandab inimeste heaolu ja tõstab majanduse võistlusvõimet. Inimeste vaba liikumine pole mõeldav ilma transpordivõrgustike ja -vahenditeta. Teede ja tänavate võrk, nende kvaliteet ja korrashoid on Eesti-sisese liikluse jaoks võtmetähtsusega. Eesti inimeste vaba liikumise kindlustamisel ja majanduskasvu soodustava transpordipoliitika
rakendamisel lähtub Valitsusliit järgmistest põhimõtetest:
1. Põhjamaade tasemel teedevõrgu väljaehitamine:
kehtestame teedeehitusnõuded, mis kindlustavad meie teed kasutusmugavuselt ja vastupidavuselt Põhjamaade tasemel teekattega. Ajakohastame talviseid teehoiunõudeid ja tõstame teehoolde võimekust erioludes;
jätkame riigi kruusateede katmist tolmuvaba kattega, kasutades Põhjamaade tehnoloogiaid. Koostame ja rakendame riikliku programmi "Eesti teed tolmuvabaks aastaks 2030";
jätkame Tallinna ja Tartu ringtee, Tallinn-Tartu maantee neljarealiseks ehitamist, Saaremaa püsiühenduse ja Via Baltica rajamist ning Tallinn-Narva maantee rekonstrueerimist;
jätkame riigimaanteede hooldamist ja remonti pikaajalise riikliku teedehoiukava alusel.
2. Ühtse ja kasutajale mugava elektroonilise piletisüsteemi loomine: Eesti rakendab liikluse korraldamisel kõiki moodsaid infotehnoloogilisi vahendeid. Loome reisijatele mugava võimaluse teabe saamiseks ja piletite ostmiseks mistahes Eesti piires liikuvale ühistranspordivahendile ühest kesksest veebikeskkonnast.
3. Ühistranspordi arendamise kõrval jääb Eestis liiklemisel väga oluliseks maanteetransport:
Eesti hõreda asustuse ja traditsioonide tõttu jääb Eesti perede peamiseks liikumisviisiks maanteetransport. Sõiduautosid ei maksustata;
tõstmaks maanteetranspordi tõhusust kaubaveol peame oluliseks koostada uuringutele tuginev kava selleks, et vähendada Eesti põhilistel kaubaveotrassidel veokite massipiirangut.
4. Kõrvuti autoliikluse parandamisega teeb Eesti valitsus kõik selleks, et vähendada autode kasutamise sundi:
arendame kvaliteetset ühiskondlikku transporti nii maal kui linnas, et oleks tagatud piisav ühendus kõigi Eesti paikadega ning bussi- ja rongitranspordi parem haakuvus;
tõstame reisirongiliikluse tihedust, et maksimaalselt ära kasutada kiiremate rongide võimalusi;
mõjutame linna- ja elamuehitust selliselt, et vahemaad töö- ja elukohtade, kaupluste ja elukohtade, koolide ja lasteasutuse ning elukohtade vahel väheneksid;
osaleme Euroopa Liidu programmi „Tark linn/Smart City" loomisel. Valime linna, kus pilootprojektina toetame linnaplaneerimise põhimõtete juurutamist, mis vähendavad sunnitud liiklemise vajadust ja pakutakse elukohti, mille suhtes töökohad, teenindusasutused, lasteasutused on paigutatud võimalikult mugavalt. Ühtlasi on "Tark linn" ka energia kokkuhoiu ja keskkonnahoiu programm.
5. Liiklusohutuse suurendamine:
Eesti valitsus koostab Eesti rahvuslikku liiklusohutusprogrammi aastateks 2015-2025, et viia liiklusohutus Eestis Põhjamaade tasemele;
varustame põhimagistraalid vajalike barjääride, peale- ja mahasõitudega, et need oleksid läbitavad ühtlase kiirusega ning jätkame põhimagistraalide ohtlike lõikude ja ristmike valgustamist;
jalakäijate ja jalgratturite ohutuse suurendamiseks jätkame kergliiklusteede arendamist;
liiklusohutuse suurendamiseks on oluline roll liikluskasvatusel, teehoiul ja järelevalvel;
sujuva ja turvalise liiklemise kindlustamiseks rakendame aktiivselt EL Intelligentse Transpordisüsteemi (ITS) projekti tulemusi, muuhulgas infotehnoloogilisi ja sotsiaalmeedia lahendusi kodanike ohutuse ja liiklusmugavuse parandamiseks.
6. Eesti lennuühenduste oluline parandamine:
Eesti lennunduspoliitika lähim suur eesmärk on võimalus lennata Tallinnast kõigisse olulisematesse Euroopa ärikeskustesse ja tagasi ühe päeva jooksul;
Eesti kui sihtkoha reklaamimisel ühendame EASi, Tallinna Lennujaama ja lennukompaniide jõud. Pikaajalisemaks eesmärgiks on muuta Tallinna lennujaam Põhja-Euroopa Aasia-suunaliste lendude keskuseks;
Eesti osaleb aktiivselt Euroopa Ühtse Taeva projektis.
7. Kaubandussuhete arendamine meritsi ja maismaal:
mereriigina peab Eesti ära kasutama Tallinna Sadama eelised regioonis. Kavandame jäämurdevõimekuse suurendamist Euroopa Liidu uue eelarveperioodi vahendite toetusel. Meretranspordi, -turismi ja -hariduse edendamiseks kiidame Riigikogus heaks Eesti Merenduspoliitika. Laevade Eesti lipu alla registreerimine peab olema mugav, kiire ja vähese bürokraatiaga;
tõstatame Venemaa-poolsed piiriületusprobleemid Venemaaga peetavatel kõnelustel ja EL sellesisulistel foorumitel. Niisamuti peame oluliseks saavutada kokkulepe Venemaaga veokvootide suurendamiseks maismaatranspordis.
8. Kaasaegse maismaaühenduse rajamine Eesti ja Lääne-Euroopa vahel:
seame sihiks, et aastal 2014 saab uute rongidega Tallinnast Tartusse sõita alla kahe tunniga ning tiheneb sõidugraafik;
koostöös Poola, Läti, Leedu ja Euroopa Komisjoniga peame vajalikuks koostada ühiskava Baltimaade paremaks ja kiiremaks ühendamiseks Lääne-Euroopaga maismaad pidi (Via Baltica, Rail Baltica, sealhulgas Tallinn-Varssavi raudteeühendus jm.);
analüüsime Tallinn-Peterburi reisirongiliini taasavamise otstarbekust.
9. Eesti-sisese veeliikluse edendamine ja väikesadamate arendamine:
konkurentsi tagamiseks praamide üleveoliinidel käsitleme Virtsu-Kuivastu ja Rohuküla-Heltermaa liine eraldiseisvatena. Kavandame riikliku tellimusena Rohuküla-Heltermaa liinile sobivate laevade soetamist Euroopa Liidu uue eelarveperioodi vahendite toel. Ehitame valmis laevad ühenduse pidamiseks Kihnu, Ruhnu, Abruka, Vormsi ja Prangliga;
siseturismi elavdamiseks ja uute töökohtade loomiseks investeerime EL vahendeid väikesadamate arendamiseks;
kaalume ajaloolise siseveetee Peipsist Pärnu jõele taastamist ning EL koostööprogrammi abiga arendame Peipsi veeturismi võimalusi nii Soome kui Venemaa suunas.
10. Läänemere laevaliikluse turvalisuse suurendamine:
Jätkame aktiivset koostööd Helcom`iga (Helsinki Commission) Läänemere laevaliikluse turvalisemaks muutmiseks ja Läänemere reostatuse vähendamiseks.
E-RIIGIST I-RIIGIKS
Valitsusliidu infoühiskonna poliitika eesmärk on pakkuda Eesti inimestele nende aega ja mugavust väärtustavat ning turvalist elu- ja töökeskkonda moodsate tehnoloogiavahenditega. Infoühiskonna keskmes peab olema i-nimene, mitte e-lektron. Tehnoloogia arendamine ei ole eesmärk omaette – riigi eesmärgiks on pakkuda inimestele paremaid teenuseid, kasutades selleks parimat võimalikku tehnoloogiat.
Eesmärgi saavutamiseks viib Valitsusliit ellu poliitikat ja struktuurseid reforme, mis lähtuvad järgmistest põhimõtetest:
1. Infoühiskond ülikiire interneti kujul mõistliku hinnaga igasse kodusse ja ettevõttesse:
internet on oluline osa kaasaegse ühiskonna taristust. Toetame uue põlvkonna fiiberoptilistel kaablitel põhineva ülikiire lairibaühenduse väljaehitamist kõikide Eesti maapiirkondadeni.
2. Riigi ühtne, lihtne ja sõbralik kodanike poole pööratud nägu internetis ja e-teenustes:
muudame e-teenused mugavateks ja inimsõbralikeks i-teenusteks, kujundades eesti.ee kodanikele käepäraseks ja ligitõmbavaks võrgu kaudu pakutavate avalike teenuste väravaks, võimaldamaks arukat ja otstarbekohast dialoogi riigi ja kodanike vahel;
loome e-Eesti versiooni nutitelefonidele ning tagame seeläbi mugavaima e-teenuste kättesaadavuse;
ID-kaart ja mobiilID peavad tagama turvalise ligipääsu igale Eestis pakutavale teenusele;
ministeeriumid saavad ühtse ülesehitusega veebilehed.
3. Emakeele ja rahvuskultuuri hoidmine, tutvustamine ja arendamine ka e-keskkonnas:
täiustame keelenõustamise ja keeleuuenduste e-keskkonda, jätkame tõlkesõnaraamatute digitaliseerimist koostöös Google`iga ja peame oluliseks jätkata emakeelsete programmide, häältuvastustarkvara ja muu keeletehnoloogia loomist;
arendame kultuurisuhtlusportaale ja jätkame rahvuskultuuri digitaliseerimist.
4. Turvalisem, säästlikum, mugavam, kiirem, läbipaistvam ja piirkonniti kättesaadavam avalik teenus:
teabeedastuse uute tehnoloogiate abil saame reformida avaliku halduse ja muuta riik kodanike ja ettevõtjate jaoks veelgi tõhusamaks;
arendame edasi ettevõtja-, maksuameti- ja ühistranspordiportaali, e-asjaajamist ning earhiveerimist;
kodanikele parima teenuse pakkumiseks viib riik avalikud e-teenused mobiilidesse ja kasutab digiTV aina laienevaid võimalusi;
koostöös erasektoriga arendame Eesti digikaardi mitmekülgseks avalikuks teenuseks, mille kaudu saab tulevikus muuhulgas toimuma ka liikluse reguleerimine;
nimetame riigikantselei juures ametisse riigi IT-poliitikat koordineeriva ametiisiku, koondame avalikku teenistust ja selle tugifunktsioone puudutava otsustamise rahandusministeeriumi.
5. Üksikisiku privaatsuse tagamine:
tagame e-teenuste turvalisuse ja isikuandmete kaitse. Oluline osa on selles teadlikkuse arendamisel infoühiskonna võimalustest ja ohtudest. Peame vajalikuks õpetada internetiturvalisuse ABCd ja internetiliikluse eeskirju algkoolist peale;
viime läbi lapsevanemate teadlikkuse tõstmise kampaaniaid ning propageerime turvavara kasutamist;
Eesti peab võtma aktiivse eestvedaja rolli rahvusvahelise õiguse arendamises, et tagada isikuõigused ja infovabadus internetikasutuses.
6. eÕpetuse edendamine:
laiendame e-kooli võimalusi, et kergendada koolikotti ja hõlbustada vanemate osalust õpiprotsessis;
loome e-gümnaasiumi, kuhu on koondatud akadeemiline õppevara ja kust nii koolid kui õpilased saavad kursusi alla laadida;
samm-sammult rakendame moodsat infotehnoloogiat õppevahendeina, et õppimine oleks rõõmus ja põnev ka tulevikus.
7. eDemokraatia arendamine kaasamise ja läbipaistvuse suurendamiseks:
e-kodanik on e-ametniku ja e-poliitiku kiireks ja tegusaks partneriks;
nutitelefoniga on võimalik valida juba 2013. aasta kohalikel valimistel.
8. Riigi e-varade andmine kodanike ja ettevõtete teenistusse:
teeme riigi ruumiandmed töödeldaval kujul avalikuks - see annab kodanikele ja ettevõtetele võimaluse ise luua riigi andmete põhjal otstarbekaid teenuseid;
läbipaistvuse ja kaasatuse suurendamiseks ning erasektori ergutamiseks uute rakenduste loomisele muudame avalikud ehk riigi ja kohalike omavalitsuste andmed masinloetavaks (machine-readable public data);
seame sihiks, et era- ja avaliku sektori koostöös loodud andmekogud oleksid ettevõtetele ja eraisikutele arendamiseks kättesaadavad.
9. Eestist maailma juhtiva E-ID ja küberjulgeoleku lahenduste tootja kujundamine:
oleme eestvedajaks Euroopa digiteenuste ühisturu väljaarendamisel, ennekõike digitaalse isikutuvastamise rahvusvahelise süsteemi rajamisel ning küberjulgeoleku edendamisel;
btöötame välja õigusliku lahenduse riigi IKT teenuste ekspordi toetamiseks, et Eesti ettevõtjad saaksid ka riigi ja Euroopa Liidu tellimusel loodud IKT lahendusi turustada;
jätkame IT-ekspordiklastri tööd;
muudame IT-hariduse riiklikuks prioriteediks, suurendame riiklikku vastuvõttu IT-teenuste loomise ja arendamisega seotud erialadel ülikoolides ning IT erialade pearaha;
ühendame Eesti infotehnoloogilise kompetentsi ja lõimime selle loomemajandusega;
käivitame Tartu Ülikooli ja Tallinna Tehnikaülikooli koostöös IT-akadeemia ning muudame Eesti Infotehnoloogia Sihtasutuse IT koolituse koordinatsioonikeskuseks;
rakendame maakondades programmeerimise huviringid ja viime programmeerimise valikainena gümnaasiumidesse.
10. i-Eesti isikupärase näo ja positiivse rahvusvahelise maine loomine internetimaailmas:
paneme vastutuse Eesti riigi kuvandi loomise, arendamise ja hoidmise eest veebikeskkonnas ühele konkreetsele ministeeriumile;
Eesti peab saama interneti-alase õigusloome eeskujuks maailmas.
TURVALINE EESTI
Valitsusliidu sisejulgeoleku- ja turvalisuspoliitika eesmärk on inimelude, inimeste tervise ja vara edukas kaitsmine ning Eesti põhiseadusliku korra, sisemise rahu ja stabiilsuse kindlustamine. Riik peab suutma tagada inimeste turvatunde parimal moel, et see annaks igaühele kindluse ennast arendades, lapsi kasvatades ja majanduslikku edu taotledes. põhiseaduslike õiguste kaitse, võimude omavaheline tasakaal ning kontrollitavus ja jõustruktuuride vastavus kodanikuühiskonna nõuetele on põhimõtted, millest me lähtume. Näeme Eesti riigikorralduse ja õiguskorra arengut eelkõige stabiilse ja paindliku täiustumisena, mitte põhjaliku ümberkorraldamisena. Dünaamilise reageerimise kõrval tehnoloogia arengule ja väliskeskkonna muutustele, tuleb väärtustena au sisse tõsta ka institutsionaalne stabiilsus ja õigusrahu ning -selgus.
Nende eesmärkide saavutamiseks soovib Valitsusliit läbi viia poliitikat ja struktuurseid reforme, mis lähtuvad järgmistest põhimõtetest:
ÕIGUSKORD
1. Turvalisus algab elukeskkonnast ja ühiskondlikest hoiakutest:
kodanike turvatunne võrsub heast majanduslikust ja sotsiaalsest keskkonnast, saab tuge eeskujulikult arendatud avalikust taristust ja arukast elukeskkonna planeerimisest, toetub õigeaegsele ja piisavale informeeritusele ning kodanike endi hoiakutele ja osalusele. Toetame linnaplaneerimise ja arhitektuursete lahenduste kasutamist turvalise elukeskkonna kujundamisel;
ühiste väärtuste kinnistumine ühiskonnas ja nende järgimine hoiavad ära paljud riskid, kuriteod ja õnnetused ning muudavad turvalisuse tagamise sihipärasemaks ja rahva ootustele vastavaks. Turvaline on ühiskond, kus õiguskaitseorganitel on vähe põhjusi sekkuda, kuid kui see on vajalik, siis toimub see tõhusalt ja kiiresti;
suuname kuriteoennetuse eelkõige noortele, toetades neile mõeldud kuriteoennetusprojekte ning hoolitsedes, et ka piisava vanemliku hoolitsuseta noortel oleks sisukat tegevust;
peame oluliseks liiklusturvalisuse jätkuvat suurendamist ja liiklusjärelevalvet. Jätkame kiiruskaamerate paigaldamist maanteede riskikohtadesse ja suurendame läbi selle liiklusturvalisust suurematel maanteedel;
seame sihiks ohvriabi tugivõrgustiku laiendamist üle kogu Eesti.
2. Isikute põhiõiguste kaitsmine:
turvalisus peab teenima kodanike heaolu. Kogukonna, piirkonna, rahvuse, riigi suveräänsusel on mõtet vaid siis, kui see põhineb inimese vabadusel – tema põhiõiguste ja privaatsuse kaitstusel;
kanname hoolt selle eest, et politsei kutsealane haridus ja väljaõpe oleksid suunatud seaduse ja avaliku korra tagamisele minimaalse jõu rakendamisega ning et järgitaks eelkõige demokraatlikke ja eetilisi väärtusi ning inimõigusi;
panustame isikuandmete kaitse ja üksikisiku privaatautonoomia tagamisse. Tugevdame Andmekaitse Inspektsiooni võimekust ja juriidilist positsiooni üksikisikute õiguste kaitsel;
kodanike riigis ei tohi kodanik oma riiki karta. Teostame karistusõiguse läbiva analüüsi ja ühtlustame karistuspoliitika. Võimaldame süütegude heastamist mitmesuguste alternatiivsete karistusvormide (ühiskondlikult kasulik töö jmt) kaudu;
muudame süütegude menetlemise kiiremaks ja arusaadavamaks ning karistuste vaidlustamise lihtsamaks;
seame sihiks valmis ehitada uus Tallinna vangla, millega viime lõpuni vanglate kaasajastamise. Suurendame vangide tööhõivet;
tagame tõhusa, seadustes kirjeldatud järelevalve jõuametkondade üle;
kindlustame, et seadusega oleks sätestatud mõistlikud kriteeriumid ja aeg salastatud materjalide avalikustamiseks, kanname hoolt, et salajaste vahendite suhtes saaks rakendada eriauditeid;
rakendame organiseeritud ja majanduskuritegudes ning korruptsioonis süüdimõistetute suhtes senisest enam vara konfiskeerimist, andes eriasjade prokuröridele ja politseinikele võimaluse spetsialiseeruda kriminaaltulu jälitamisele.
3. Kodanikuühiskonna ja riigi koostöö süvendamine turvalisuse tagamisel:
arendame riigi ja kogukondade omavahelist vabatahtlikku head koostööd;
edendame naabrivalvet;
avaliku korra mõiste, samuti avaliku korra kaitse peab olema ühtsetel alustel mõõdetav ning hinnatav kogu riigis. Rakendame Korrakaitse seaduse;
tagame korrakaitseüksuste suurema nähtavuse ja jõudmise abivajajani, koolitades ja kaasates iseseisva pädevusega abipolitseinike. Toetame abipolitseinike tegevust;
toetame vabatahtlike päästjate tegevust.
4. Õigusruumi selguse ja arusaadavuse suurendamine:
jätkame Eesti õigussüsteemi korrastamist selles suurema kooskõla ja lihtsuse saavutamiseks ning ülereguleerimise vältimiseks;
jätkame era- ja avaliku õiguse kodifitseerimist valdkondades, kus see on otstarbekas ja vajalik – et kodanik leiaks kogu valdkonna seadused ühest tekstist ning saaks üheselt aru oma õigustest ja kohustustest. Lisaks töös olevale keskkonnaseadustikule võtame vastu valdkonnaseadusi koondava ehitus- ja planeerimisseadustiku;
arendame eesti õiguskeelt.
ÕIGUSKAITSE
5. Korrakaitse nähtavuse, reageerimise kiiruse ja tõhususe tõstmine:
kuritegevuse vastase võitluse prioriteedid lähtuvad ohuhinnangutest. Iga-aastased prioriteedid otsustatakse justiits- ja siseministri poolt järgmiseks eelarveaastaks;
kuritegevuse kiiremaks tõkestamiseks ja päästeteenuse parema kättesaadavuse tagamiseks jätkame investeerimist pääste-, politsei-, piirivalve- ja ekspertiisiasutuste tehnikasse;
tihendame rahvusvahelist õiguskaitsealast koostööd;
kindlustame kõrgema tähtsusega väljakutsete puhul helikopteriteenuse olemasolu;
parandame korrakaitsjate väljaõpet ning kaalume uue Sisekaitseakadeemia rajamist Ida-Virumaale.
6. Õiguskaitse rakendumise kiiruse ja vältimatuse tagamine:
kohtumenetluse pikkus ei tohi reeglina ületada 100 päeva ühes kohtuastmes, selleks sätestame mõistlike menetlustähtaegade järgimise üle selgema järelevalve ja vastutuse;
arendame edasi riigi õigusabi süsteemi ja eelarvevõimaluste tekkel laiendame tasuta õigusabi kättesaadavust abivajajatele;
peame vajalikuks tugeva ühendhäirekeskuse loomist ning ühele hädaabinumbrile üleminekut 112.
7. Võitlus vägivallaga lähisuhetes ja koolis:
jätkame võitlust lähisuhete vägivalla, sealhulgas koolivägivalla vähendamiseks ja tõkestamiseks;
eelarvevõimaluste piires suurendame turvalisusteenuseid osutavate kodanikeühenduste, muuhulgas naiste varjupaikade rahastamist.
8. Korruptsiooni ennetamine ja tõkestamine:
KAPO uurimisõigus peab laienema kõigile korruptsioonijuhtumitele, mis ohustavad Eesti Vabariigi julgeolekut;
võtame vastu uue korruptsioonivastase seaduse, mis muu hulgas täpsustab ametiisikute mõistet ja muudab majandushuvide deklareerimise sisuliseks ja elektrooniliseks;
uuendame aastast 2013 korruptsioonivastast strateegiat „Aus riik". Uus strateegia näeb ette täiendavaid meetmed korruptsiooni ennetamiseks ja keskendub veelgi enam korruptsiooni tõkestamisele erasektoris ja kohalikes omavalitsustes.
9. Kodanike ja ettevõtete turvalisuse tagamine küberruumis:
töötame välja küberruumi korrakaitseks vajalikud regulatsioonid, täiendame seadusandlust ja käivitame küberruumi kuriteoennetava tegevuse, sealhulgas koolituse;
täiustame küberkaitse strateegiat, jätkame selle elluviimist ning tugevdame sel eesmärgil koostööd eraettevõtete ja riigi vahel.
10. Julgeolekuasutuste ajakohastamine ja julgeolekustrateegia pikaajaline planeerimine:
tõhustame luure- ja vastuluuresektori korraldust tervikuna ning planeerime selle arengut pikemalt;
koostame pikaajalise julgeolekustrateegia valdkondade kaupa, mis sätestab selged julgeolekualased riiklikud eesmärgid ja ootused;
korrastame eri jõuametkondade töötajate sotsiaalse kohtlemise.
11. Rahvusvahelise turvalisuskoostöö edendamine:
tõhustame korrakaitselist tegevust piiriülese kuritegevuse tõkestamiseks. Kindlustame parema koostöö lähinaabrite politsei, tolli ja piirivalvega narko- ja inimkaubandusevastases tegevuses;
toetame karistuspoliitika-alase seadusandluse ühtlustamist oma naaberriikidega Euroopa Liidus;
arendame koostööd võimalike merereostuse ja suurõnnetuste ühiseks likvideerimiseks Läänemeres ning ühiseks terrorismivastaseks tegevuseks.
KULTUURIPOLIITIKA
Valitsusliidu kultuuripoliitika eesmärk on tagada eesti rahvuse, keele ja kultuuri kestmine läbi aegade. Selleks arendame kultuuripoliitikat, mis kujundab kultuuri loojale ja tarbijale vaba ja loomingulise keskkonna ning aitab seeläbi kaasa rahva ja riigi püsimisele. Olemasoleva ja toimiva kultuuriraamistiku hoidmine, traditsioonide ja pärandi säilitamine, uue ja avarama pilguga tulevikku vaatamine ning töö noortega on järgnevate aastate kultuuripoliitika olulisemad suunad. Globaliseerumine avaldab survet kõigile rahvuskultuuridele, eesti kultuuri missioon on rahvusvahelise massikultuuri tasakaalustamine hea ja eestimaisega. Valitsusliit seisab võrdsete võimaluste loomise eest ning tunnustab kõiki Eestis toimivaid kultuuriloojaid ja -vahendajaid, sealhulgas omandi- ja organisatsioonilisest vormist sõltumata.
Professionaalse- ja harrastuskultuuri elujõulisuse tagamiseks kogu Eestis lähtub Valitsusliit järgmistest põhimõtetest:
1. Riigitoetuste suunamine ennekõike professionaalseks loometegevuseks:
Kultuurkapitali aluspõhimõtteid ei muudeta. Eelarvevõimaluste tekkel suurendame professionaalse loomingu ergutamiseks mõeldud toetusi;
võtame suuna sellele, et riigiasutuste tegelikud väljaminekud oleksid finantseeritud riigieelarvest ja Kultuurkapitali vahendid läheksid ennekõike loovisikutele ja erakollektiividele projekti- ja loomingutoetusteks;
analüüsime võimalust toetada jätkuvaid kultuuriprojekte pikemaajalise toetuskava alusel;
kaalume võimalust muuta loovisikute seadust selleks, et lahendada vabakutselistele tunnustatud loovisikutele ravikindlustusega seotud probleem.
2. Kultuurile mõeldud rahaeraldiste, sealhulgas Euroopa Liidu toetuste suurendamine:
seisame selle eest, et EL järgmise finantsperspektiivi rahastamiskavades ja piiriülese koostöö programmides oleks kultuurivaldkonnal ja loomemajandusel senisest suurem osakaal.
3. Kaasamine, koostöö väärtustamine loome- ja erialaliitude ning valdkondlike keskustega:
riik peab eriala- ja loomeliite olulisteks partneriteks kultuuripoliitika kujundamisel, loome toimivad koostöövormid valdkondade esindajate kaasamiseks. Väärtustame valdkondlike keskuste panust Eesti kultuuri arendamisse;
jätkame kultuuripreemiate, sealhulgas elutöö preemiate maksmist vähemalt senises mahus.
4. Kultuuri kättesaadavuse parandamine:
edendame filmivaldkonna arengut, sealhulgas kodumaist filmilevikut ning Eesti filmitootmise tehnilist võimekust;
parandame professionaalse kunsti (kino, teater, kujutav kunst jms) kättesaadavust väikelinnades ja asulates;
loome Eesti Filmi Sihtasutuse juurde eraldi programmi laste ja noorte mängufilmide tegemiseks. Toetame Eesti animafilmi;
teeme veebis rohkem ja paremini kättesaadavaks kultuuriajakirju;
toetame veebipõhist raamatukogude infosüsteemi arendustegevusi ning tehnoloogilise võimaluste laiendamist nägemispuudega inimestele;
jätkame laulu- ja tantsupeoliikumise rahastamist pidudevahelisel ajal.
5. Eesti rahvale oluliste kultuuriehitiste püstitamine:
ehitame valmis Eesti Rahva Muuseumi ja Tallinna Muusikakeskkooli uued hooned;
jätkame ettevalmistusi Rahvusooper Estoniale uue maja ehitamiseks;
jätkame pühakodade, mõisakoolide ja looduslike pühapaikade programmi rahastamist, sealhulgas Euroopa Liidu vahenditest ning kohalike omavalitsuste kultuuri- ja spordiobjektide investeeringutoetusi;
tagame, et kõik riigi poolt algatatud suurprojektide (sealhulgas kommunismiohvrite memoriaali) arhitektuurikonkursid viiakse läbi koostöös valdkondlike loomeliitudega.
6. Kultuuriekspordi edendamine ja Eesti tutvustamine maailmas kultuuri varal:
loome kultuuriekspordi edendamiseks EASi ekspordi arendamise toetuste kõrvale kultuuriekspordi toetusmeetme, et valdkonnaspetsiifikat arvesse võttes toetada loomemajanduses tegutsejate võimalusi välisturgudel läbilöömiseks;
toetame valdkondlike arenduskeskuste tegevust, sh muusika, disaini, arhitektuuri ja filmi valdkonnas, eesmärgiga soodustada neis valdkondades ettevõtlust, kasvatada ekspordipotentsiaali, luua toimivad klastreid ja soodustada koostööd loomeettevõtete ja teiste majandusharude vahel;
kasutame kultuuriekspordi edendamisel aktiivselt Eesti diplomaatilist võimekust ning teeme koostööd teiste EL riikide välisteenistustega. Seame eesmärgiks muuta Eesti tunnustatud loomemajanduse- ja disainimaaks.
7. Kultuurihariduse suurem sidumine üldharidusega:
 1. jaanuarist 2014 kehtestame kuni 130 euro suuruse iga-aastase pearaha igale kooliealisele (6-19 aastasele) lapsele, mida saab kasutada huvialaringis osalemise eest tasumiseks;
jätkame koolide varustamist muusikariistadega;
tähtsustame muuseumit kui õpikeskkonda.
8. Eestimaa kultuurilise palge mitmekesistamine:
jätkame temaatiliselt eristuvate maakonnamuuseumide arendamist (sh muinsuskaitsealase tegevuse lisamist), et neist kujuneksid olulised maakondlikud külastus- ja teaduskeskused;
jätkame setu, Kihnu, saarte, Vana-Võru, Peipsiääre, Rannarootsi ja mulgi programme;
toetame rahvusvähemuste kultuurikollektiivide osavõttu suurematest Eesti kultuuriüritustest ja kultuurikollektiivide esinemist teistes Eesti regioonides;
aitame rahastada rahvusvähemuste kultuuri ja pühapäevakoole;
toetame hõimurahvaste koostööd.
9. Muinsuste ja kultuuripärandi tutvustamine, kaitsmine ning hoidmine:
vältimaks muinsuskaitse all olevate objektide pöördumatut hävimist, viime läbi nende inventeerimise ning vaatame üle kaitse alla võtmise kriteeriumid;
jätkame kultuuripärandi digitaliseerimist Eesti mäluasutustes. Muuhulgas muudame Eesti kultuuripärandi portaali ühtseks infoväravaks, mis võimaldab otsinguid erinevatesse süsteemidesse (muuseumid, raamatukogud, rahvusringhäälingu arhiivid, kultuuripärandi riiklik register);
täiustame muuseumide infosüsteemi (MuIS), et lähitulevikus oleksid kõik riigimuuseumide kogud veebipõhised;
seome olemasolevad infosüsteemid Euroopa digitaalraamatukoguga Europeana, et meie väärtuslik kultuuripärand oleks kättesaadav kõikidele eurooplastele.
10. Autoriõiguste ja intellektuaalse omandi kaitsmine:
tagame intellektuaalse omandi igakülgse kaitse, viies seadusandluse vastavusse digiajastu nõuetega. Kaasajastame Autoriõiguse seaduse ning reguleerime puudulikult kaitstud valdkonnad;
võitleme tõhusalt piraatlusega ja koolitame õiguskaitseorganeid, et nad oskaksid uues digitaalses maailmas võidelda intellektuaalse omandiõiguse rikkumiste ja kuritarvitustega.
11. Loomemajanduse käsitlemine osana Eesti uuest majandusest:
aitame kaasa kunstiinimeste ja ettevõtjate kokkuviimisele, majandus- ja kunstidistsipliine ühendavate õppekavade tekkele, loomelinnakute toetamisele ja kultuurimänedžeride koolitamisele;
toetame loomemajandust soosiva keskkonna väljaarendamist, muuhulgas investeeringuid loomelinnakutesse. Kaalume kultuuriministeeriumi loomemajanduse programmi suurendamist;
peame oluliseks ettevõtlusõppe võimaluste laiendamist kultuurieriala üliõpilastele.
SPORT JA KEHAKULTUUR
Valitsusliidu spordipoliitika eesmärk on elujõuline Eesti rahvas, tema õnnelik ja täisväärtuslik elu. Valitsusliit peab oluliseks liikumisharrastuse juurutamist juba imikueast ning lastesporti kui vahendit noorte eemalehoidmiseks alkoholi, tubaka ja narkootikumide tarbimisest. Liikumisharrastuste harjumuse tekitamine loob eeldused pikaks ja täisväärtuslikuks eluks väärikamas eas. Oluline on luua kõigile võimalused mitmekülgseks sportlikuks tegevuseks terve elu vältel, tagades tugeva ja laiahaardelise aluse meie tulevastele tippsportlastele ja olümpiavõitjatele.
Selle eesmärgi saavutamiseks viib Valitsusliit ellu poliitikaid, mis lähtuvad järgmistest põhimõtetest:
1. Liikumisharrastuse edendamine:
seame eesmärgiks, et aastaks 2014 on korrapärase liikumisharrastusega hõlmatud 35% asemel 45% elanikkonnast;
koostöös kohalike omavalitsustega aitame luua uusi kodulähedasi tervisespordiparke, kergliiklusteid, jooksu-, suusa-, ratta- ja matkaradasid ning soodustame harrastusspordi looduslike võimaluste väljaarendamist;
loome sportimisvõimalusi erivajadustega inimestele ja toetame nende sportlikku tegevust.
2. Noorte sportimisharjumuste toetamine:
 1. jaanuarist 2014 kehtestame lapse kohta kuni 130 euro suuruse aastase huviringiraha, mida saab muuhulgas kasutada noortespordi finantseerimiseks, luues sellega lapsevanemale valikuvabaduse oma lapse sportliku arengu kavandamiseks;
pidades tähtsaks koolisporti, parandame sportimistingimusi koolides ning jätkame ujumise algõppe programmi toetamist;
väärtustame enam saavutusspordiga tegelevaid noori ning nende treenereid. Kaalume 50/50 süsteemi kasutuselevõtmist, mille puhul toetab riik poole summa ulatuses noortespordi III, IV ja V kutsekvalifikatsiooniga treenerite tasustamist;
laiendame noorsportlaste tervisekontrolli süsteemi.
3. Spordi rahastamise korrastamine:
kujundame spordi rahastamise selgemad alused ja korrastame maksuregulatsioone sportimise soodustamiseks;
loome Euroopa Liidu järgmise finantsperspektiivi struktuurivahenditest programmi üleeestilise sporditaristu arendamiseks;
tunnustame tugevaid, hea juhtimisega spordiorganisatsioone.
4. Treener-pedagoogi elukutse väärtustamine:
väärtustame treenerikutset ja kvalifikatsiooni ning pöörame enam tähelepanu treenerite täiendkoolitusele;
treenerkonnale järelkasvu ettevalmistamisel tuleb treenerite koolitamine muuta spordikesksemaks, suurendada praktikaõppe osakaalu ja oma ala spetsialistide kaasamist õppejõududena;
loome akadeemilises treeneriõppes õppijaile võimaluse taotleda Kultuurkapitali kehakultuuri ja spordi sihtkapitali stipendiumeid.
5. Tippspordi tugistruktuuride arendamine:
toetame ratsionaalsemat ja elanikkonnas toimuvaid muudatusi arvestavat spordirajatiste kavandamist ning rajamist. Tippspordirajatiste planeerimisel ja ehitamisel võtame arvesse riiklikke prioriteete ning Eesti Spordiregistri andmebaasi. Arendame välja üleriigilised ja regionaalsed tippspordikeskused;
toetame tippsportlasi ning tagame neile konkurentsivõimelised treenimistingimused ja võimalused osalemiseks tiitlivõistlustel;
jätkame rahvusvaheliste tiitlivõistluste Eestis korraldamise toetamist.
EESTI KEEL JA MEEL
Valitsusliidu keelepoliitika eesmärk on tagada eesti keele kestmine ja areng kõigis eluvaldkondades läbi aegade. Eesti keel on eesti rahvusliku identsuse nurgakivi ning riigikeelena Eesti omariikluse olulisemaid tunnuseid.
Tähtis pole üksnes hoida eesti keele tänast kasutusala, vaid seda sihikindlalt laiendada tulevikutehnoloogiatele ning uutele teadus- ja kultuurivaldkondadele. Veelgi järjekindlamaks peab muutuma keeleõppevõimaluste loomine muude emakeeltega Eesti elanikele. Tõhusalt tuleb toetada eesti keele õpet kodumaast eemal viibivaile eestlastele ja kõigile huvilistele. Valitsusliit on veendunud eesti keele suutlikkuses pidada sammu maailma muutumisega ja seab oma eesmärgiks selleks vajalike tegevuste sihipärase toetamise.
Nende eesmärkide saavutamiseks peab Valitsusliit vältimatuks riigi ja kogu ühiskonna järjekindlat panustamist eesti keele arengusse, lähtudes järgmistest põhimõtetest:
1. Eesti oskuskeele järjekindel arendamine:
toetades Vabariigi Presidendi algatust eesti keele rikastamiseks, kujundame välja senisest süsteemsemad keelevärskenduse ja oskussõnavara loomise võimalused;
kanname hoolt, et õnnestunud sõna- ja mõisteloome tulemused leiaksid kiiresti koha kõrgkoolide õppematerjalides;
toetame erialaste uudisteoste tõlkimist ja avaldamist e-raamatuna.
2. Keele- ja aineõppe tugevam seostamine kõigil haridusastmeil:
tagame lisaks heale keeleõppele täpse ja selge keelekasutuse kujundamise kõigi õppeainete kaudu. Selleks uuendame õppekavasid ja õppematerjale ning panustame keeleõppe osakaalu suurendamisse õpetajakoolituses;
suurendame veebipõhiste õppematerjalide hulka ja kättesaadavust, et võimaldada igale soovijale osasaamine parimast keele- ja aineõppest.
3. Keele- ja kõnetehnoloogiate pidev edasiarendamine sihtrahastamise toel:
toetame kõnesünteesi tehnoloogia täiustamist, kõnetuvastuse valdkondlike rakenduste loomist ja kasutuselevõttu, eestikeelse ja eesti keelele suunatud tarkvara loomist ja rakendamist.
4. Keelekasutuse heade tavade juurutamine:
toetame keelekorraldusasutusi ja -vabakondi nende tegevuses, mis väärtustavad täpset, asjatundlikku ja stilistiliselt rikkalikku keelekasutust ühiskonnas;
laiendame keelenõustamise tehnilisi võimalusi, tagame sõnastike vaba kättesaadavuse veebis;
saavutamaks eeskujuliku kirjakeele kasutamine ametlikus suhtluses, õigusaktides ja avalikus teabelevis, panustame selleks vajalike koolituste korraldamisse.
5. Eesti keele õppe süvendatud jätkamine muu emakeelega inimestele:
eesti keelest erineva õppekeelega õppeasutustes tagame kõigil haridusastmeil kõrgel tasemel õppematerjalid ning laiendame keelekümblusvõimalusi;
panustame õpetajate ettevalmistusse ja täiendkoolitusse;
muukeelsetes kutseõppeasutustes ja -rühmades peame eriti silmas õppijate erialase keeleoskuse arendamist;
toetame ülikoolide valmisolekut pakkuda esimestel õppesemestritel eesti keele tihendatud õpet ebapiisava keeleoskusega üliõpilastele;
suurendame riigikeeleõppe võimalusi täiskasvanuile;
seame sihiks nõustamisteenuse loomise muukeelsete koolide eesti keelele ülemineku toetamiseks ja keelehaldusküsimuste lahendamiseks.
6. Eesti keele murrete väärtustamine:
näeme eesti keele murretes tagatist ja ammendamatut allikat eesti ühiskeele kestvale arengule. Toetame sihtprogrammide kaudu kõigi tugevamate piirkondlike keele- ja kultuuritavade õpet, edasiarendamist, praktiseerimist ja laialdast tutvustamist.
7. Eesti keele toetamine välismaal:
peame vajalikuks tagada välismaal elavate ja töötavate eestlaste kontaktid kodumaaga ja nende lastele võimalused õppida eesti keelt;
seame sihiks, et üha enamates välisülikoolides avataks eesti keele ja kultuuri õppetoolid.
8. Keeleseaduse täitmise järelevalve: tagame, et igaühel on kõikjal Eestis tõrgeteta võimalus ametlikus suhtluses ja teeninduses ajada asju eesti keeles.
9. Ajaloo teadvustamine:
edendame isamaalist kasvatust ja toetame isamaaliste noorteorganisatsioonide tegevust;
jätkame represseeritute toetamist vastavalt okupatsioonirežiimide poolt represseeritute seadusele;
toetame Eesti riikliku iseseisvuse eest võidelnute tunnustamist Riigikogu otsusega;
toetame president Meri algatust rahvusvahelise kommunismikuritegude muuseumi asutamiseks, samuti Tallinna kommunismiohvrite memoriaali rajamist ning jätkame Kaitseväe kalmistu ja Vabadussõja mälestusehise taastamist;
toetame Rahvusvahelise Kommunismikuritegude Uurimise Komisjoni moodustamise algatust sarnaselt Rahvusvahelisele Kriminaalkohtule;
edendame Eesti lähiajaloo uurimist ja selgitamist rahvusvahelisele üldsusele;
toetame lähiajaloo tutvustamist koolides erinevates regioonides ja keeltes.
LÕIMUMINE
Valitsusliidu eesmärk on tagada võrdsed võimalused edukaks toimetulekuks ja heaoluks kõigile Eestis elavatele inimestele, olenemata rahvuslikust kuuluvusest ja emakeelest. Valitsusliit tagab, et Eesti Vabariigis on kaitstud iga siin elava isiku põhiõigused ja -vabadused.
Lisaks eestlastele kui põhirahvusele elab siin hulgaliselt muu rahvuslik-kultuurilise taustaga ja erasuhtluses teisi keeli kasutavaid inimesi. Valitsusliit näeb mitmekesisuses rikastavat võimalust Eesti eduks ja arenguks.
Eesmärgi saavutamiseks peab Valitsusliit vajalikuks, et riiklik lõimumiskava sisaldaks alljärgnevaid struktuurseid reforme ja põhimõtteid:
1. Vähemusrahvusest eestimaalaste, eriti noorte, konkurentsivõime tugevdamine tööturul:
edukas toimetulek Eestis eeldab eesti keele oskust. Viime lõpule ülemineku eestikeelsele gümnaasiumile;
panustame veelgi enam eesti keele õppe ja eestikeelse aineõppe kättesaadavusse ja kvaliteeti kõigil haridustasandeil – venekeelses lasteaias ja koolis peab eesti keele õpe toimuma iga päev. Muudame vastavate õpetajate, ainekavade ja õppematerjalide ettevalmistamise süsteemseks ja järjekindlaks;
tugevdame projektipõhiseid võimalusi õpetajate täiendõppeks ja muid tugitegevusi;
toetame keelekümblusmetoodika laiemat rakendamist alates lasteaiast;
majanduslike võimaluste tekkel taassuurendame laste keeleõppelaagrite (perelaagrite) ja ekskursioonide korraldamise võimalusi;
peame oluliseks, et kõrgharidust omandada soovivad mitte-eestlased õpiksid edasi Eesti ülikoolides;
suurendame mitte-eestlastest avalike teenistujate ning haridus- ja kultuuritöötajate võimalusi erialase keelevaldamise kinnistamiseks;
arendame edasi tööjõuvahetuse programme. Tihendame koostööd Töötukassa, Sihtasutuse Meie Inimesed (MISA) ja kohalike omavalitsuste vahel, pakkumaks vähemuspäritoluga töötutele tõhusamat tuge ja õpet;
tagame riigikeeleõppe kättesaadavuse ka mitte-eestlastest töötutele, pensionäridele ja puuetega inimestele;
arendame järelevalvet täiskasvanuile eesti keele õpetamise, sh koolitajate kvaliteedi üle;
algatame riikliku lõimumiskava pideva jälgimise, eesmärgiga kohandada selle rakenduskavu muutuvatele vajadustele.
2. Eri ühiskonnarühmade omavahelise suhtluse tihendamine:
väärtustame ja toetame algatusi, mis viivad ühiste eesmärkide saavutamiseks kokku eri rahvusrühmadest pärinejaid. Majanduslike võimaluste tekkel tugevdame Sihtasutuse Meie Inimesed ja Kodanikuühiskonna Sihtkapitali võimalusi sellesuunaliste projektide toetamiseks;
jätkame mitmekeelset teabepakkumist, sealhulgas rahvusringhäälingus ja sotsiaalmeedias.
3. Eesti põlisvähemuste kultuuripärandi väärtustamine ja avalikkusele kättesaadavaks tegemine:
hindame kõrgelt Eesti ajalooliste põlisvähemuste (juudid, baltisakslased, vene vanausulised, eestirootslased, ingerisoomlased) pikaajalist panust Eesti rikkaliku kultuuripildi väljakujunemisse. Toetame selle kultuuripärandi hoidmist, uurimist ja väärikat eksponeerimist, sealhulgas ka välismaal, vastavate kultuuriühenduste, riigi, omavalitsuste ja erasektori koostööl;
eelarvevõimaluste avanemisel parandame Peipsi-ääre arengukava, pühakodade programmi, vana-slaavi keeleõppe ja kultuuripärandi uurimise rahastamist;
korrastame Kloogal asuva holokausti memoriaali.
4. Vähemuskultuuride püsimise toetamine:
austame iga inimese õigust oma rahvuskultuurilisele identiteedile;
peame vältimatuks rahvusvähemuste kultuuriühenduste ja pühapäevakoolide jätkuvat toetamist riigi ja omavalitsuste poolt;
eelarvevõimaluste tekkel suurendame soome-ugri rahvaste toetusprogrammi kõrghariduse omandamiseks Eestis.
5. Jätkuvalt austades iga inimese vaba tahet oma kodakondsuse määratlemisel, parandame Eestis elavate teiste riikide kodanike ja määratlemata kodakondsusega isikute teavitamist Eesti kodakondsuse omamise eelistest ja võimalustest:
tagame mittekodanikest vanemaile informatsiooni võimaluste kohta omandada Eesti kodakondsus oma kuni 15-aastasele lapsele;
pöörame erilist tähelepanu vast-naturaliseerunud Eesti Vabariigi kodanikele, et hõlbustada nende sulandumist ühiskonda;
kodakondsuspoliitika põhimõtteid ei muudeta.
ILUS JA PUHAS EESTI
Valitsusliidu keskkonnapoliitika eesmärk on vastutustundliku suhtumise kujundamine loodusesse ning Eesti inimestele rahva püsimist toetava puhta ja looduslikult mitmekesise elukeskkonna säilimine põlvest põlve. Valitsusliit paneb erilist rõhku Eesti inimeste loodussäästliku mõtteviisi kujundamisele ning maa- ja loodusvarade heaperemehelikule kasutamisele.
Nende eesmärkide saavutamiseks lähtub Valitsusliit oma keskkonnapoliitikas järgmistest põhimõtetest:
1. Puhta elukeskkonna kindlustamine igale Eesti elanikule:
jätkame reoveepuhastite uuendamist, kõik ühisveevärki tarbivad Eesti elanikud saavad puhta joogivee hiljemalt aastaks 2013;
seame eesmärgiks puhtad metsaalused, üldise jäätmetekke vähendamise ning jäätmete taaskasutamise suurendamise, muuhulgas energiatootmiseks;
arendame jäätmete taaskasutussüsteeme, et need oleksid tarbijale võimalikult mugavad. Toetame kohalikke omavalitsusi jäätmekogumispunktide rajamisel;
õhusaaste ja mürakoormuse vähendamiseks linnades kindlustame küllaldase haljastuse;
õhusaaste leevendamiseks siirdume järk-järgult väiksema süsinikukoormusega majandusmudelile. Energia ja soojuse tootmisel eelistame väiksema keskkonnamõjuga taastuvaid (kodumaiseid) energiaallikaid. Jätkame energiasäästuprojektide toetamist;
soovime avada eraldi meetme nõukogude aegse maastikureostuse (tondilosside) likvideerimiseks;
võtame fookusesse ka võitluse kaaskodanike avaliku korra rikkumisest lähtuva mürareostusega.
2. Täisväärtuslikuks eluks vajaliku loodusliku mitmekesisuse säilitamine:
peame looduskaitsemeetmete rakendamisel oluliseks ökosüsteemide sidusust ning keskkonnakasutuse eesmärgipärast ja mõistlikku piiramist;
kaitsealade puhul peame tähtsaks kaitsekavade tegelikku rakendamist, mitte nende formaalset laiendamist uutele aladele;
tagame Nabala karstiala ja Tuhala Nõiakaevu säilimise;
jätkame eraomanike toetamist, kes oma maal loodust kaitsevad ja aitavad traditsiooniliste majandamisviisidega kaasa pärandmaastike ja -koosluste säilimisele;
tagame traditsiooniliste kalajõgede elujõulisuse, hea seisundi ja kalade läbipääsu paisudest.
3. Eesti maavarade kui rahvusliku rikkuse heaperemehelik majandamine:
riik võtab Eesti maavaravarude kasutuselevõtu ettevalmistamisel ja korraldamisel juhtiva rolli;
kindlustame, et ressursi- ja keskkonnakasutuse tasude määrad on pikaajaliselt ette teada;
pöörame lisaks põlevkivivarudele ja ehitusmaavaradele tähelepanu ka seni kasutuseta maavarade uurimisele ning toetama uute tehnoloogiate kasutuselevõttu;
uute kaevanduste avamine toimub kokkuleppel kohaliku kogukonnaga.
4. Loodusvarade keskkonnasäästlik kasutamine:
laiendame aheraine kasutust ehitusmaterjalina teede ja parklate rajamisel;
ammutame lõpuni pooleldi kasutatud turbaalad ning toetame kasutatud turbaalade rekultiveerimist;
loome tingimused kestlikuks, kasumlikuks ja isemajandavaks erametsanduseks. Selleks viime läbi tulumaksumuudatuse, mille kohaselt lubame raieõiguse või uuendusraie käigus raiutud metsamaterjali võõrandamisel saadud maksustatavast tulust maha arvata kuni kolme aasta jooksul pärast võõrandamist tehtud metsa majandamise kulud;
toetame erainitsiatiivi ühistulise tugisüsteemi arendamisel, mis oleks metsaomanikule toeks metsatööde korraldamisel ja puidu turustamisel;
põline riigimets jääb riigi omandisse;
laiendame harrastuspüügivõimalusi kudemiskohtade ja kalapüügikohade taastamise kaudu;
kaasajastame jahinduse õiguslikku korraldust.
5. Puhta ja turvalise Läänemere eest võitlemine:
seame eesmärgiks saavutada Läänemerele aastaks 2020 Euroopa Liidu kriteeriumidele vastav hea seisund. Selleks rakendame tegevuskava, mis arvestab siseveekogusid ja merd tervikliku ökosüsteemina, hajutab tihedast tankeriliiklusest tulenevaid keskkonnariske ning suurendab reostustõrjevõimekust;
pöörame tähelepanu rannikumere puhtana hoidmisele;
osaleme aktiivselt rahvusvahelises Läänemere kaitse ja kasutamise alases koostöös ning võitleme Läänemere-äärsete riikide ühtse keskkonnaseiresüsteemi loomise eest;
viime läbi uuringud merekaitsealade kiiremaks määratlemiseks ja Läänemere seisundi täpseks hindamiseks.
6. Keskkonnateadlikkuse kasvatamine:
toetame keskkonnahariduse edendamist. Selleks tagame keskkonnahariduse andmiseks pädevate õpetajate juurdekasvu ja toetame loodusõppeprogrammide arendamist;
riik näitab eeskuju, rajades uued avaliku sektori hooned maksimaalselt energiasäästlikena ning rakendades kõrgemaid keskkonnastandardeid transpordivahendite hangetel;
säilitame juurdepääsu merele ja veekogudele ning riigimetsa koos metsa traditsiooniliste andide (puhas õhk, seened, marjad) kasutamise võimalusega;
keskkonnateadlikkuse suurendamiseks tagame kõigile e-juurdepääsu riigi valduses olevatele keskkonnaandmetele.
7. Arukam haldus: ehitus- ja planeerimistegevuse seadustiku loomise käigus kaalume riigiarhitekti ametikoha loomist ning planeerimistegevuse viimist keskkonna- või majandus- ja kommunikatsiooniministeeriumisse.
MAAELU EDENDAMINE
Valitsusliidu maaelu-, põllumajandus- ja regionaalpoliitika eesmärk on maapiirkondade kõrge elukvaliteet ning hästi tasustatud töökohtade juurdekasv maal. Selleks teeb Valitsusliit panuse taristu arendamisele, ettevõtluskeskkonna jätkuvale parandamisele ning inimeste koolitamisele ja nõustamisele. Valitsusliit peab seejuures oluliseks koostööd omavalitsuste, kodukandi- ja külaliikumisega, seltside, koguduste ning ettevõtjatega.
Eesmärgi saavutamiseks viib Valitsusliit läbi poliitikaid, mis lähtuvad järgmistest põhimõtetest:
1. Eesti põllumehele EL tootjatega võrdsete konkurentsitingimuste tagamine:
seisame selle eest, et Eesti põllumehele rakenduksid alates järgmisest EL eelarveperioodist (2014) kõigi teiste Euroopa Liidu tootjatega võrdsed konkurentsitingimused;
toetame Ühise põllumajanduspoliitika (ÜPP) muutmist üha rohkem maaelu kui terviku (maaelu arengukava alusel eraldatavateks) toetusteks. Selleks tuleb ÜPP lahti siduda mineviku tootmismahtudest ning maksta otsetoetusi järjest rohkem avaliku huvi alusel, nagu omamaise toidu kättesaadavus, piisav sissetulek tootmise kestlikuks käigushoidmiseks, põllumajandusmaastike hooldus, bioloogiline mitmekesisus, maapiirkondade elujõulisus;
seisame selle eest, et Ühise põllumajanduspoliitikat rahastataks jätkuvalt Euroopa Liidu ühisest eelarvest;
tagame Ühise põllumajanduspoliitika ja Eesti Maaelu arengukava riigi poolse kaasfinantseerimise;
tagame põllumajanduse otsetoetuste siseriikliku juurdemakse (top-up) 2012. aasta eest Euroopa Liidu lubatud ulatuses;
jätkame siseriiklike põllumajandustoetuste maksmist senises mahus.
2. Maaelu mitmekesistamine, ettevõtluse paljususe edendamine Ühtse põllumajanduspoliitika raames:
toetame uute innovaatiliste ettevõtlusvaldkondade levikut maal lisaks põllumajandusele väike- ja pereettevõtluse mitmekesiste tegevusalade arengut. Senisest enam võimalusi näeme metsamajanduse ja vesiviljelusega seotud valdkondades;
uuendusliku maaettevõtluse arendamiseks tõstame teavitustegevuse ja nõuandeteenuse taset, parandades selleks nõustajate kvalifikatsiooni.
3. Ühistegevuse ja koostöö edendamine:
toetame oma kodukanti arendavaid, loovaid ja tegusaid liidriomadustega inimesi ning peame oluliseks selgitada ühistegevuse eeliseid;
toetame senisest enam majanduslikku ühistegevust nii tootmise, töötlemise kui turustamise valdkonnas;
toetame jätkuvalt külaliikumise ja talu kui traditsioonilise tootmisüksuse arendamist ning külavanemate institutsiooni tugevdamist vallavolikogu ja vallavalitsuse koostööpartnerina. Soosime omavalitsuste, kodukandi-, külaliikumise ja kohaliku omaalgatuse (Leader) programmi osaliste, mittetulundusühingute, koguduste ja ettevõtjate koostööd.
4. Eeskujuliku taristu arendamine maal:
ehitame uue põlvkonna fiiberoptilistel kaablitel põhineva ülikiire lairibaühenduse kõikide Eesti maapiirkondadeni;
tagame elektrienergia varustuskindluse, ehitame ringtoite kaabli Hiiumaa ja mandri vahele;
jätkame riigi kruusateedele tolmuvaba katte ehitamist, kasutades Põhjamaade tehnoloogiaid;
jätkame Tallinna ja Tartu ringtee, Tallinn-Tartu maantee neljarealiseks ehitamist, Saaremaa püsiühenduse ja Via Baltica rajamist ning Tallinn-Narva maantee rekonstrueerimist;
jätkame reoveepuhastite uuendamist, kõik ühisveevärki tarbivad Eesti elanikud saavad puhta joogivee hiljemalt aastaks 2013;
tervishoiuteenuse tagamiseks kõikjal Eestis loome asendusperearstide süsteemi, mis tagaks perearsti olemasolu igale elanikule ka siis, kui oma perearst puhkab või tekib muu ettenägematu takistus teenuse osutamiseks raskesti ligipääsetavates paikades;
erakorralise meditsiini ja päästeteenuse osutamiseks kindlustame kõikide kõrgema tähtsusega väljakutsete puhul helikopteriteenuse olemasolu saartel;
siseturismi elavdamiseks ja uute töökohtade loomiseks investeerime EL vahendeid väikesadamate arendamiseks;
toetame ajaloo- ja kultuuripärandi taastamist ja selle toomist kohalikku ja turismitarbelisse kasutusse. Lisame Eesti turismi arengukavasse meie omanäolise toidukultuuri arendamise ja propageerimise. Jätkame Eesti Toidu programmi.
5. Halduse korrastamine: koondame kalandusvaldkonna korralduse, välja arvatud ressurside üle teostatava järelevalve põllumajandusministeeriumisse.
VÄLISPOLIITIKA
Valitsusliidu välispoliitika eesmärk on Eesti julgeoleku ja heaolu kasvu kindlustamine. 
Eesti julgeoleku ja heaolu kasvu kindlustamiseks peab Valitsusliit oluliseks lähtuda Eesti välispoliitikas järgmistest põhimõtetest:
1. Eesti on aktiivne Euroopa Liidu, NATO, ÜRO, Euroopa Julgeoleku- ja koostööorganisatsiooni (OSCE), Euroopa Nõukogu ja teiste rahvusvaheliste organisatsioonide poliitikate kujundamisel:
Eesti teeb ettevalmistusi eesistumisperioodiks Euroopa Liidus 2018. aastal;
peame oluliseks Eesti pääsu ÜRO Inimõiguste nõukokku 2012. aastast ning ÜRO Julgeolekunõukokku 2020. aastast.
2. NATO kui Eesti peamine julgeolekutagatis:
panustame NATO strateegilise kontseptsiooni elluviimisse, sealhulgas olulistesse NATO missioonidesse;
missioonide kõrval peame Eesti olulisimaks panuseks NATO küberkaitse arendamist, milles soovime olla üheks juhtriikidest;
peame terrorismivastast võitlust Afganistanis üheks NATO olulisimaks missiooniks turvalisema homse kujundamisel ning narkokaubanduse leviku tõkestamisel. Otsuse selle missiooni lõpetamiseks vajalike tingimuste täitmise kohta peavad NATO liikmed tegema ühiselt.
3. Aktiivne äri- ja kultuuridiplomaatia, Eesti ettevõtjate, ekspordi ja kultuuritegelaste toetamine Välisministeeriumi ja Ettevõtluse Arendamise Sihtasutuse välisesinduste koostöös:
sõlmime võimalikult paljude riikidega topeltmaksustamise vältimise ning investeeringute kaitse lepingud;
laiendame aukonsulite võrgustikku ning kasutame Eesti huvides rohkem koostööd teiste EL riikide diplomaatiliste esindustega.
4. Toetus Euroopa Liidu ja NATO senise laienemispoliitika jätkamisele:
toetame Euroopa Liidu liitumiskõneluste jätkamist Lääne-Balkani riikidega, Islandi ja Türgiga ning valmisolekut kõneluste alustamiseks organisatsiooni mittekuuluvate Ida-Euroopa riikidega;
toetame NATO avatud uste poliitika jätkamist nii Balkanil, Lõuna-Kaukaasias kui ka mujal Euroopas.
5. Turvalisuse suurendamine Euroopa Liidu piiridel:
peame tähtsaks EL naabruspoliitikat ja idapartnerlust, arendame Idapartnerluse Koolituskeskust;
peame oluliseks Euroopa uute demokraatiate toetamist ning rahvusvahelise õiguse põhimõtete kaitsmist Euroopa Liidu vahetus naabruses, mistõttu ei ole alternatiivi Gruusia territoriaalsele terviklikkusele. Ka tuleb tagada Moldova territoriaalne terviklikkus ning leida lahendus Transnistria külmutatud konfliktile.
6. Tihedad suhted kõigi oma naabritega:
peame tähtsaks Läänemere strateegia rakendamist Läänemere piirkonna arenguks, muuhulgas uute transpordi- ja energiaühenduste loomisel;
tähtsustame ja peame arendamist väärivaks NB 8 ehk Põhjamaade ja Balti riikide igakülgset koostööd;
lisaks tihedatele ja headele suhetele Euroopa Liitu ja/või NATOsse kuuluvate naabritega, on Eesti huvides ka heanaaberlikud suhted Venemaaga. Toetame konkreetseid ja praktilisi algatusi vastastikuste suhete arendamiseks.
7. Inimõiguste ja heade valitsemistavade rahvusvaheline edendamine:
Eesti näeb arengukoostöösse ja humanitaarabisse panustamises olulist välis- ja julgeolekupoliitika vahendit ning annab oma võimetele vastava panuse maailma vaesuse vähendamisse ning demokraatia, õigusriigi ja heade valitsemistavade põhimõtete kinnistamisse arengukoostöö sihtriikides; tegutseme aktiivselt totalitarismi kuritegude teadvustamisel ja nende ühemõttelise hukkamõistu saavutamisel.
8. Toetame igati transatlantilise koostöö arendamist kõigis valdkondades ning Eesti-USA suhete süvendamist.
9. Taotleme Eesti kodanikele viisavaba pääsu enamatesse riikidesse.
10. Eesti huvide paremaks esindamiseks tugevdame Eesti välisesinduste võrgustikku keskendudes peamistele julgeolekualastele ja majanduslikele prioriteetidele ning Eesti kodanike huvide kaitsele.
RIIGIKAITSE- JA JULGEOLEKUPOLIITIKA
Valitsusliidu julgeoleku- ja riigikaitsepoliitika eesmärk on parimate julgeolekutagatistega iseseisev Eesti riik, mis on kaitseks sisemisele ja välisele rahule, praeguste ja tulevaste põlvede eneseteostusele ning eesti rahvuse, keele ja kultuuri säilimisele läbi aegade. Eesti riigi kaitsmine on meie ühisväärtus, -hüve ning -vastutus. Eesti julgeolekut tugevdab sidus kodanikuühiskond, kus teadlikul kodanikuaktiivsusel on oluline roll julgeoleku ja turvatunde edendamisel. Riigikaitse oluline eeldus on kodanike kaitsetahe.
Nende eesmärkide saavutamiseks arendab Valitsusliit Eesti rahvusliku julgeoleku võimekust ja riigikaitset järgmiste põhimõtete kohaselt:
1. Eesti peamine julgeolekutagatis on kollektiivkaitse ja NATO:
Eesti riigikaitse tugineb esmasele iseseisvale kaitsevõimele ning NATO kollektiivkaitsele. Eesti sõjaline kaitse on kavandatud kollektiivkaitseoperatsioonina;
kollektiivkaitse veenvuse tugevdamiseks tuleb suurendada NATO kohalolekut, arendada kahepoolset kaitsekoostööd liitlastega ning tagada Kaitseväe koostegutsemisvõime liitlasvägedega;
Eesti esmane iseseisev kaitsevõime peab tagama eeldused kollektiivkaitse toimivaks rakendumiseks.
2. Eesti riigikaitse kiire rakendatavus ja selle eelduseks oleva juhtimisselguse tagamine:
riigikaitse arendamisel lähtutakse riigikaitse laiast käsitlusest vastavuses kehtestatud Riigikaitsestrateegiaga. Kindlustame, et kõik riigiasutused valmistuvad oma riigikaitseliste ülesannete täitmiseks võimalike ohtude korral ning tagame, et sõjaline kaitse ei arene ülejäänud ühiskonnast eraldiseisvalt;
toetame riigikaitseliste Põhiseaduse muudatuste vastuvõtmist Riigikogu poolt;
algatame rahu- ja sõjaaja riigikaitseseaduste kaasajastamise. Toimekindluse tagamiseks muudame rahu- ja sõjaaja riigikaitselised juhtimissüsteemid ning vastutusalad võimalikult sarnasteks;
riigikaitse juhtimise korraldamisel lähtutakse kaitsejõududest kui täitevvõimu osast. Tagame erinevate riigikaitseliste tegevuste juhtimise koordineerituse ning juhtimise selguse ja läbipaistva tsiviilkontrolli;
jätkame riigi lennuvahendite ja laevade ning nende käitamiseks vajaliku teenindusressursi koondamist. Loome aluse militaar- ja päästeressursi võimete koostoimeks;
3. Aktiivne panustamine NATO ja Euroopa Liidu ühispoliitikatesse:
osaleme aktiivselt NATO arengute suunamisel, peame õigeks NATO nähtavuse ja kohaloleku suurendamist;
taotleme NATO Balti õhuturbemissiooni muutmist alaliseks;
tagame Eesti osaluse operatsioonidel senises mahus kooskõlas NATO sihttasemega (10% maaväe koosseisust);
osaleme võimetekohaselt Euroopa Liidu ühise julgeoleku- ja kaitsepoliitika alastes ettevõtmistes, sealhulgas EL operatsioonidel;
koos sõjaliste missioonide planeerimise ja läbiviimisega arendame ka tsiviilmissioonidesse panustamise võimekust;
süvendame kaitsekoostööd USA-ga, sealhulgas operatsioonidel;
panustame aktiivselt Põhjala-Balti riikide kaitsealasesse koostöösse eesmärgiga muuta see peamiseks regionaalseks kaitsekoostöö formaadiks Põhja-Euroopas.
4. Riigikaitse toetumine kodanike vabatahtlikule kaasatusele ja kaitsetahtele:
jätkame ja laiendame vabatahtlikkuse alusel toimuvat riigikaitseõpetust kesktaseme õppeasutustes eesmärgiga suurendada vastavate koolide arvu 150-ni;
peame oluliseks toetada Kaitseliidu arendamist ning kasvavat rolli riigikaitses. Tagame Kaitseliidu ja tema eriorganisatsioonide stabiilse arengu, Kaitseliidu rahastamiseks näeme ette kindla osa sõjalise riigikaitse eelarvest. Võtame vastu uue Kaitseliidu seaduse.
5. Eesti kaitsekulude taseme tõstmine 2% SKTst. Eesti iseseisvus ja julgeolek on väärtused, mille arvelt ei tohi kokku hoida:
saavutame aastaks 2012 kaitsekulude tasemeks 2% SKTst ning tagame selle taseme stabiilsuse;
alustame Jägala linnaku väljaehitust, kavandades selle valmimise 4 aastaga;
tagame Ämari lennubaasi täieliku tegutsemisvalmiduse saavutamise aastaks 2015;
jätkame Kaitseväele moodsa relvastuse hankeid. Parimate hanketingimuste saamiseks teeme vajadusel koostööd partnerriikidega;
kindlustame Kaitseväele tänapäevased elamis- ja väljaõppetingimused.
6. Riigi sõjalise kaitse professionaalsuse edendamine:
riigikaitse mehitamisel lähtume senisest segasüsteemist, mis hõlmab ajateenistust üldise kaitsetahte ja oskuste arendajana, elukutselist kaadrikaitseväge, reservväelasi ning Kaitseliitu ühinenud vabatahtlikke. Võtame vastu uue Kaitseväeteenistuse seaduse;
tugineme ajateenistuse arendamisel Riigikaitse 10-aastases arengukavas sätestatule. Kaalume üleminekut 6-9-12-kuulisele ajateenistuse süsteemile järgmise 10-aastase arenguplaani koostamise käigus aastal 2012. Eelistatult tuleb ajateenistusse võtta kõik omal initsiatiivil sinna astuda soovijad;
kasvatame kaadrikaitseväelaste arvu 125 võrra igal aastal kuni piirarvu 4000 saavutamiseni.
7. Rahvusvahelise initsiatiivi hoidmine küberjulgeoleku arengutes:
a. arendame aktiivselt Eesti küberkaitsevõimekust, sealhulgas siseriiklikus ja rahvusvahelises koostöös. Tugevdame koostööd NATO liitlastega tugevdatakse Küberkaitsekeskust eesmärgiga muuta see juhtivaks rahvusvaheliseks kompetentsikeskuseks;
b. toetame Kaitseliidu juurde loodud küberkaitseliitu. Suurendame küberkaitse alast väljaõpet Kaitseväes.
8. Eesti kaitsetööstuse ja kaitseotstarbelise teadus- ning arendustegevuse toetamine:
koostöös Kaitsetööstuse Liiduga jätkame rahvusliku kaitsetööstuse arendamist eesmärgiga saavutada arvestatav ekspordivõimekus mõnes tegevussuunas;
kasvatame kaitsealase teadus- ja arendustegevuse rahastamist lähtudes eelkõige Kaitseväe vajadustest ja suunatuna kaitsetööstuse arendamisele.
9. Algatame Eesti iseseisvuse ja julgeoleku nimel välismissioonidel osalenute kodanikuühiskonda ja -ellu tõhusa taasrakendamise poliitika: toetame veteranide organisatsiooni, töötame välja tervikliku veteranidepoliitika missioonidel osalenud kaitseväelaste toetuseks ning alustame vastavate teenuste arendamist ja võimekuste suurendamist.
KODANIKE RIIK
Valitsusliidu eesmärk on riigikorraldus, mis toetab Eesti kodanike loomulikku soovi elada vaba ja täisväärtuslikku elu. Me soovime, et Eesti riik kasutaks igat maksumaksja poolt makstud senti säästlikult, eesmärgiga pakkuda selle eest parimat võimalikku avalikku taristut ja teenust võimalikult paljudele. Me soovime, et Eesti oleks tugeva kogukondliku võrgustiku ja identiteediga, loogiliselt, lihtsalt ja mõistuspäraselt korraldatud ning tõhusalt toimiv demokraatlik riik.
Nende sihtide saavutamiseks peab Eesti riigi- ja kohalik haldus järgnevatel kümnenditel arvestama jätkuva linnastumise ja elanikkonna vananemisega. Kohaliku halduse kaasajastamine peab toimuma järk-järgult, paindlikke lahendusi võimaldades ning kogukondlikke võrgustikke ja identiteete lõhkumata. Valitsusliit on veendunud, et tugev kogukondlik identiteet on parim demokraatia tagatis.
PÕHISEADUS JA DEMOKRAATIA
1. Toetame Eesti Põhiseaduse ja põhiseaduslike seaduste järjepidevat akadeemilist analüüsi, et vältida Põhiseaduse põhjendamatut muutmist, kuid hoida meie riigi alusseadus ja selles sisalduvate väärtuste kaitse ajakohasena.
2. Loome õigusliku raamistiku demokraatia arendamise sihtasutuste tekkeks erakondade kõrvale, mille ülesandeks on Euroopa Liidu naabruspoliitika, maailmavaatelise kodanikuhariduse ja ühiskondliku poliitilise mõtte edendamine.
KODANIKUÜHENDUSED
Valitsusliit peab riigi arengus oluliseks eelkõige kodanikuühiskonna tugevnemist. Eesti riik peab tugevnema mitte uute ametiasutuste loomise ja täiendavate ametnike teenistusse võtmise teel, vaid kaasates kodanikuühendusi riigivalitsemisse ja võttes laiemalt kasutusele uusi tehnoloogiaid. Valitsusliit soovib, et vabad kodanikud osaleksid oma ühenduste kaudu tegusalt nii ühiskondlike otsuste langetamise protsessis kui ka ühiskonnaelu korraldamises. Selleks peame oluliseks ellu viia poliitikat, mis on suunatud järgmistele eesmärkidele:
3. Kodanikeühenduste laiem ja lihtsam kaasamine:
teeme kodanike ja vabaühenduste paremaks kaasamiseks ühe portaali kaudu kättesaadavaks informatsiooni kõigi riigi tasandil toimuvate strateegiate ja arengukavade ning õigusaktide eelnõude kohta, näidates ära protsessi etapid, ajakava ning avalikkuse võimalused otsuse kujundamises osaleda;
rakendame Eesti Kodanikuühiskonna arengukava (EKAK) ja „Kaasamise hea tava" põhimõtteid. Anname äriregistris vabaühenduste kohta olevad andmed vabalt kasutusse, et oleks lihtne leida organisatsioone, kes vajavad vabatahtlikke, kellele annetada ja keda kaasata.
4. Kodanikühendustele kindel rahastamine:
muudame riigi kogutavad andmed vabaühenduste kohta - aastaaruanded ja põhikirjad kättesaadavaks ning eristame registris vabaühendused ja avaliku võimu asutatud ja kontrollitavad mittetulundusühendused;
analüüsime valitsuse kinnitatava tulumaksusoodustusega mittetulundusühenduste nimekirja pääsemise tingimusi;
toetame jätkuvalt kodanikühiskonna organisatsioone ja algatusi Kodanikuühiskonna Sihtkapitali (KÜSK), kohaliku omaalgatuse programmi, hasartmängumaksu nõukogu ja muude rahastamiskanalite kaudu. Jätkame KÜSKi riigieelarvelist toetamist.
5. Noortele rohkem õigusi: algatame ühiskonnas debati selle üle, kas ja kuidas oleks ühiskonnas stabiilse tasakaalu hoidmiseks mõistlik arvestada valimistel laste ja noortega. Algatame arutelu valimisea 16. aastani viimise üle.
6. Jätkuv koostöö kirikute ja kogudustega: teeme igakülgset koostööd kirikute ja kogudustega, eeskätt traditsiooniliste konfessioonidega Eestis. Näeme kirikut ja kogudusi aktiivsete partneritena teenuste osutamises Eesti elanikele.
RIIGIHALDUS
Riigihalduse tänapäevastamisel peab Valitsusliit oluliseks järgmiste struktuursete reformide ja poliitikate elluviimist:
7. Riigiga suhtlemine kiiremaks ja mugavamaks: muudame lihtsamaks inimeste ja ühingute suhtlemist riigiga, seda eelkõige e-riiki ja e-teenuseid arendades. Sõltumata elukohast peab riik ja omavalitsus olema igaühele käeulatuses.
8. Eriseisundi ja -õigustega ametnike vähendamine, nende hüvede ühtlustamine võrreldes erasektoriga ning avaliku teenistuse muutmine nüüdisaegselt dünaamiliseks:
võtame vastu uue Avaliku teenistuse seaduse, mis korrastab avaliku teenistuse, muutes läbipaistvaks ja võrreldavaks avaliku sektori palgasüsteemi ja ametihüvede kasutamise;
täidame ametikohad avalikus teenistuses ja riigile kuuluvate ettevõtete juhatustes konkursi korras ning soodustame kvalifitseeritud tööjõu liikumist avaliku ja erasektori vahel;
vähendame avalikus sektoris hõivatud inimeste hulka uute tehnoloogiate ja tõhusama töökorralduse kasutuselevõtu teel, mitte teenuste kvaliteedi arvel;
koondame avaliku teenistuse seaduse rakendamise, samuti riigi kui tööandja tegevuse koordineerimise eest vastutuse ja kompetentsi Rahandusministeeriumisse.
9. Riigihalduse muutmine lihtsamaks ja tõhusamaks:
parandame riigi poliitikate strateegilist planeerimist ja ministeeriumide vahelist koostööd. 2014. aastal algava Euroopa Liidu eelarveperioodi vahendite tulemuslikumaks ja tõhusamaks kasutamiseks tugevdame keskset koordineerimist, koondame funktsioone ja vähendame juhtimistasandeid. Võimalusel koostame kõikide fondide kohta ühe arengukava, mis muuhulgas tagab rakendamise käigus suurema paindlikkuse vahendite ümbertõstmiseks:
tagame avalik-õiguslike isikute ja riigi poolt asutatud sihtasutuste tegevuse läbipaistvuse, aruandluse ja juhtorganite vastutuse;
tõhusama juhtimise ja haldamise saavutamiseks koondame 2011. aasta lõpuks kogu riigiasutustele mittevajaliku kinnisvara ning 2013. aastaks riigiasutuste poolt kasutatava kinnisvara (välja arvatud sümbolkinnisvara) ja selle haldamise ning arendamisega seotud tegevused Riigi Kinnisvara Aktsiaseltsi;
koostöös erasektoriga jätkame ministeeriumide ja nende valitsemisealade tugiteenuste (raamatupidamine, personalitöö, hanked jmt) koondamist ühtsetesse keskustesse, pakkudes sama teenust ka kohalikele omavalitsustele ning sulgeme mittevajalikud asutused. Võtame riigi tugitegevuses kasutusele ühtsed standardid ja infosüsteemid. Toetame omavalitsuste tugifunktsioonide (õigusteenistus, raamatupidamine) konsolideerimist;
määrame riigihangete läbiviimiseks kompetentsikeskuste näol kesksed hankijad ja läheme üle e-hangete korraldamisele hiljemalt aastaks 2014.
10. Omavalitsuste, kodanikeühenduste ja erasektori suurem kaasamine riigivalitsemisse:
anname kodanikeühendustele ja erasektorile võimaluse täita senisest suuremat rolli sotsiaalhoolekandes, kultuuri-, spordi-, keskkonnakaitse, tervishoiu- ja turvalisuse vallas, hariduses ning teistes valdkondades. Seal kus võimalik, anname riiklikke ülesandeid omavalitsustele, kodanikeühendustele ja eraettevõtetele üle anda halduslepingute alusel.
KOHALIK HALDUS
Kohalik omavalitsus ei ole riigi käepikendus, vaid vabade kodanike iseseisev kohalik valitsus. Eesti Vabariigi Põhiseadusega, Kohalike omavalitsuste korralduse seadusega, Euroopa kohaliku omavalitsuse harta ratifitseerimisega on Eesti valinud ja kinnistanud autonoomse, kogukonnapõhise kohaliku omavalitsuse. Tugev kohalik identiteet, laiapõhjaline demokraatlik riigikorraldus, keskvõimu tasakaalus hoidmine on väga suured väärtused, millel põhineb Eesti iseseisvus. 
Kohaliku halduse tänapäevastamisel peab Valitsusliit oluliseks reformide elluviimist järgmistest põhimõtetest lähtuvalt:
11. Omavalitsuste koostöö ja omavalitsuste ühisasutuste moodustamise soodustamine seaduse ja lepingute alusel riiklike ning mitut omavalitsust hõlmavate omavalitsuslike ülesannete täitmiseks;
12. Omavalitsustele iseseisva tulubaasi, regionaalse tasakaalustatuse ja kohaliku demokraatia suurendamine:
viime omavalitsuste tulubaasi pikaajalise planeerimise Riigieelarve strateegiasse;
eelarvevõimaluste tekkel vaatame üle omavalitsuste tulubaasi kujunemise alused võttes arvesse omavalitsuste koonddefitsiiti. Üldise suundumusena peab tänaste väikeste kohalike maksutulude, suure osatähtsusega riigitoetuste ja niinimetatud kohaliku iseloomuga riiklike maksude asemel oluliselt suurenema omavalitsuste roll oma maksutulu kujundamisel;
Omavalitsustele riigieelarvest investeeringutoetuste eraldamisel võtame arvesse omavalitsuste finantssuutlikkust (sh võlakoormus piirmäärast kinnipidamine);
võimaldame igal Eesti elanikul omandi, töökoha või perekondlike sidemete alusel määrata kuni kaks ametlikku elukohta ja sellest tulenevalt jagada nende vahel tulumaksu;
seame eesmärgiks suurendada kohalike teede hoiu rahastamise osakaalu üldises teehoiu rahastamises;
tihendame koostööd kohalike omavalitsustega kvaliteetsete e-teenuste arendamisel.
13. Aitame arendada ja finantseerida omavalitsuste arengu mõttekoda, kus kohtuvad teadlased, ametnikud, poliitikud omavalitsejad ja vabasektor."""

valdkond = None
inlist = -1
inordlist = -1
sup="NULL"
insup = "NULL"

for line in txt.split("\n"):
	if line.isupper():
		valdkond = vk[line][0]
		sup = "NULL"
		inlist=-1
		#print()
		#print(line, vk[line])
		continue
								
	if line[len(line)-1]==":":
		l[i]=[sup, valdkond, line]
		inlist=0
		sup = str(i)
		print(">>> (" + str(sup) + ") "  +line)
	elif line[len(line)-1]==";":
		if sup!="NULL":
			print("* [" + str(sup) + "] "  +line)
			l[i]=[sup, valdkond, line]
		else:
			print(line)
			l[i]=["NULL", valdkond, line]
	else:
		if sup!="NULL":
			print("* [" + str(sup) + "] "  +line)
			l[i]=[sup, valdkond, line]
		else:
			print(line)
			l[i]=["NULL", valdkond, line]
		inlist=-1
		sup="NULL"

	i+=1
	if inlist >= 0: inlist+=1

lid=-1
lnr=-1

for x in l:
	st = l[x][2].split(". ")
	if len(st)>0 and st[0].isnumeric():
		if st[0]=="1":
			lid=x-1
			lnr=1
		if lnr==int(st[0]):
			l[x][0]=lid
			lnr += 1
		else:
			lid=-1
			lnr=-1

lid=None
oid=None
vid=None

for x in l:
	if vid != l[x][1]:
		for title, idv in vk.items():
			if idv[0] == l[x][1]:
				print(idv[0], title)
				vid = idv[0]
				lid = None
				break

	if l[x][0] != "NULL" :
		st = l[x][2].split(". ")
		if len(st)>0 and st[0].isnumeric():
			print(x, l[x][0], l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])
		else:
			print(x, l[x][0], "\t* " + l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])
	else:
		print(x, l[x][2][0:60] + " /---/ " + l[x][2][len(l[x][2])-40:9999])

	if l[x][0]!="NULL": lid = l[x][0]






#pprint(l, width=156)

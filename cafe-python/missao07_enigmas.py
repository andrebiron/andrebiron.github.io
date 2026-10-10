# =====================================================
#  CAFÉ PYTHON - Missão 7: Os enigmas do sábado
# =====================================================
# Todo sábado o Café & Letras faz uma gincana de enigmas com os clientes.
# Este sábado você vai resolver os dois enigmas com laços de repetição.

palavras = [
    "befazoco", "bele", "lacabe", "mopa", "pafifi", "nedera", "sotuvabatu", "xaxa",
    "tuberiripa", "labapo", "nasa", "fibe", "raponeriri", "tusomaco", "tezo", "motexa",
    "tevalamo", "bapo", "tavanebena", "riletegade", "tatalebale", "coraramoda", "daralera", "falenazo",
    "zogoxamola", "conamo", "viberana", "gaxara", "lucada", "poriluri", "galurari", "balaca",
    "saga", "lumosane", "luga", "banalafico", "xabarida", "gafivisazo", "vigamosa", "netu",
    "filuri", "gacobexa", "rigoxa", "sasole", "xamaderi", "nabalucara", "viteba", "ravimagoso",
    "xacotapo", "pofite", "sote", "vineri", "maso", "tale", "delamaba", "neva",
    "napopo", "gatacalu", "rari", "vana", "basacozo", "marira", "risalecala", "tulamodama",
    "xasamogapo", "farifapada", "gabaso", "gode", "sonazodafa", "xata", "popa", "sotumo",
    "xalenadasa", "beda", "tafavilade", "vilazotupo", "xalatugo", "tumafa", "soma", "vilelapo",
    "dabexale", "nelusone", "nacosobe", "necogopa", "xamoga", "copotu", "xagasavi", "cacago",
    "falebatude", "xabapoda", "ledede", "delemama", "visopo", "zogavalata", "lule", "dagodeda",
    "lulugane", "zocamafa", "gagodagotu", "tuba", "matasa", "colu", "riviso", "somolugada",
    "gazofi", "caxavisote", "fapaco", "gaca", "tuzodaba", "dadana", "firidele", "leladaralu",
    "taleravi", "lupa", "comafi", "xavirala", "gomozosopa", "varilalu", "demo", "neganefi",
    "gorada", "dexa", "bamatasaca", "sodalu", "bevizofaca", "lapo", "tafivabexa", "cacapo",
    "comosopo", "cova", "dexala", "manefapova", "tevita", "tatuzodeda", "nacaca", "lalazo",
    "vamomo", "cavitede", "rita", "fidene", "lanebaco", "vada", "bafa", "turafa",
    "xafatetede", "finale", "lafariva", "pozotugago", "para", "radete", "momo", "catacaxapa",
    "nasogozo", "tulutunene", "pasalusa", "zolunelaso", "fagocofaga", "sobeteda", "cararifama", "soda",
    "lucomomasa", "codavavi", "fada", "carigosomo", "zofalusopo", "golu", "zonagalu", "zomo",
    "bemamo", "lucatede", "naneco", "fanete", "lagari", "xalu", "covi", "nariva",
    "datepagafa", "befinaluva", "nesode", "sasa", "coralafigo", "navivila", "nedetemo", "beso",
    "gopabe", "batusobe", "ganaxa", "tubedadafi", "vata", "bedesotu", "lenema", "detelapa",
    "bafidegoxa", "mopolusa", "filepaxa", "fitarama", "bafaga", "temogavipa", "rasotatuda", "lesabepafa",
    "goxafipoga", "tanatutaca", "lupaga", "begazo", "nanevico", "bapa", "fimo", "zomofanaso",
    "fipa", "pazoma", "xanada", "lematepa", "rinetazone", "racovi", "cobema", "xazobepa",
    "derisa", "sotelalaxa", "goga", "famalebeco", "racogo", "fagabe", "sagotazo", "tubebefile",
    "radevanepo", "facovago", "magata", "fidavacava", "benemamo", "deberibeva", "palaco", "matube",
    "povica", "tavafico", "xasole", "tudamopo", "sovaluvabe", "nagafi", "moga", "rate",
    "rapa", "faco", "nalurale", "basocaba", "tude", "vicaleca", "bafi", "vava",
    "naga", "dacotu", "goraleda", "vabaxaxa", "begoda", "zofa", "luxa", "namodamova",
    "raluraga", "fanepaso", "safa", "dagapa", "taso", "betavagavi", "detabego", "savi",
    "sanexasa", "pamazodalu", "naderaso", "xadesanaxa", "capaxavari", "rilubadexa", "bezogo", "bebafalavi",
    "ranesada", "vinepovazo", "tapovamoga", "damalafapo", "razonepamo", "salubete", "gavizo", "coxata",
    "dezotari", "vavi", "basasanara", "sodasama", "videvada", "mabele", "fafi", "fasolecate",
    "namaca", "tefabatumo", "cafipoxane", "code", "tufa", "vapa", "zozobecosa", "faxago",
    "caralepo", "vatega", "fale", "potuxaxa", "sobetu", "sole", "gopacosapa", "gana",
    "solata", "vipofivilu", "pasasapa", "davipabe", "pobalu", "raso", "fixa", "tavi",
    "lucodezoca", "comovata", "saxaga", "gagofi", "nede", "lefibete", "visola", "desatu",
    "rirafipa", "comoralaba", "lubaba", "vasogalane", "dala", "fisolutata", "tevi", "gotufidena",
    "lacacaneca", "comozo", "motateca", "povisa", "teta", "luda", "bepa", "lugo",
    "molu", "lababesa", "tuzoxa", "nazosa", "fatelela", "savanesa", "lularivizo", "sotevapo",
    "zoxaba", "natatanene", "demabe", "gaxacatu", "balanego", "vifasogo", "rifi", "saganerima",
    "luso", "ponaluta", "tedabe", "rapaficoxa", "tuna", "gobesoca", "lega", "tebegogala",
    "gofibe", "tune", "latuta", "lexadatune", "caride", "tunatepata", "beneteva", "fibexa",
    "molasafi", "gogolu", "sazoga", "rasamo", "tula", "ramatuvi", "fitate", "caconara",
    "sasopa", "taca", "tasocofi", "pateca", "saderitu", "codama", "rirafate", "nepafifina",
    "valebe", "bamabexasa", "fadata", "povibega", "detacaxalu", "capago", "nari", "namarita",
    "nesolecoca", "ricobe", "lade", "vitepocomo", "caposaba", "xaranecoma", "sala", "fapa",
    "fabatemo", "mamomarile", "gora", "pabera", "pafa", "dalucamoca", "tugona", "gade",
    "cosale", "nagagamo", "zona", "sofiviga", "detacabe", "delunafafi", "xafidabe", "lulela",
    "naporide", "lusabegole", "tudede", "figafiga", "tamo", "zonazoga", "gobalura", "viralaca",
    "coma", "nago", "posoma", "farane", "sodatanefi", "baxarada", "natuzora", "zoco",
    "tutasova", "tevaga", "dacapo", "sazovixa", "sonaleta", "modeluco", "denasosa", "galu",
    "caca", "dedacanaga", "xamoxatara", "sadefima", "vago", "fivamoco", "bacaragago", "rifipanate",
    "tuzovapaso", "fimagobe", "vina", "rigaxabama", "lusacabeba", "labagale", "zogoraco", "mofa",
    "lama", "ratasalepa", "laxamobe", "camofagata", "fazo", "saraga", "fipapo", "xaledenane",
    "babagasabe", "nenatabe", "deficofana", "nenenedeca", "lepa", "leponeco", "lana", "lepaga",
    "nepadane", "tafiriraso", "magaga", "deribatude", "xamo", "rixaxa", "fizo", "dane",
    "pota", "fadazolate", "vamofisasa", "nanexabelu", "dataca", "xara", "tabafafasa", "soxa",
    "lenazoso", "cacogodexa", "zovigarale", "befa", "balu", "vilanate", "zolacapa", "naluga",
    "valavi", "leludemaga", "besopa", "navisole", "lalu", "vitataca", "pana", "nedalupo",
    "nalu", "xacosofifa", "zotemopa", "riririsala", "zopatu", "patu", "natupafi", "vila",
    "caxanena", "macasari", "marina", "vibemozo", "dazocovilu", "laga", "canepatutu", "navabe",
    "bebesa", "gocova", "netemora", "pagocavi", "gagalusoso", "gocofitu", "tanamocona", "dede",
    "telexa", "somalemo", "gala", "moridasava", "zocopabe", "pavifida", "ledeluma", "vipoga",
    "neca", "gogo", "poxalaviso", "salurimori", "cazo", "tedemopori", "ladedalebe", "ripapate",
    "mavamosago", "cote", "nevineteva", "devipa", "becodecogo", "betuvasode", "vimotu", "zodemopago",
    "banamotaco", "fiva", "vixabaxa", "sonapa", "paco", "ledabecolu", "texamogole", "posa",
    "fipapa", "lulenagovi", "taneri", "lulexa", "vivadezo", "fapaca", "sacomonabe", "tabemo",
    "lugorasa", "samolenada", "vapaco", "letatuxa", "besa", "dapada", "negovaco", "tuxala",
    "nana", "ritusocaca", "ladezo", "talagozovi", "camotaca", "begobete", "lutu", "bepago",
    "vicalecane", "gada", "momalugofa", "tuvago", "lesotebavi", "lumadagori", "tucaneluba", "defa",
    "farasana", "razoso", "farade", "dematude", "moso", "balavisoso", "vasaladago", "golexava",
    "mari", "rigama", "mopoxala", "sota", "gaxazozo", "dabafiteva", "saxataca", "figazobera",
    "poxabaxa", "mazoba", "lenerile", "lecovimopo", "lera", "cavadatuco", "nerixana", "luba",
    "rapavipoxa", "lutefiri", "lelu", "pomoda", "poco", "falama", "lebalu", "xalupogapo",
    "cagamo", "gavizoxaco", "bafababe", "detago", "cagacomori", "viberi", "fapaxapotu", "madalude",
    "porabepo", "rara", "nateraxa", "mopasoluco", "gazobeva", "fari", "xalatuda", "pobenaleco",
    "gabacavi", "zomacabe", "viragapa", "letunasapa", "larinaba", "vasodada", "mozo", "monecapalu",
    "lecoteneca", "fate", "caturigago", "xanebe", "fivide", "laca", "tuva", "gomatu",
    "datu", "vimopa", "lumoca", "tamomofipo", "conadepama", "zode", "nefadenezo", "cava",
    "motatecata", "rigomatupo", "maga", "fasamale", "tapole", "ledatucamo", "lacalutu", "lefa",
    "codari", "balufa", "lema", "poxava", "faleri", "gomobenego", "tesotudefi", "zoso",
    "lacobeca", "sasafi", "govafa", "godefida", "zosadaca", "fifavariba", "devima", "sofiba",
    "ganenasola", "tatuzodeco", "zotaxa", "nazo", "balari", "caletaxa", "zobefa", "bagaca",
    "somavi", "sotufi", "lecoraluvi", "desari", "viga", "soturile", "gobedaca", "xasazozoso",
    "lufiragaxa", "lanexavila", "sogatavi", "zosocate", "bafamo", "mobaco", "cacanazo", "molazozolu",
    "deratuna", "tego", "morifalaco", "reviver", "baso", "ficapazolu", "zolunavata", "como",
    "laxaxari", "betenefa", "columolate", "patupozopo", "zovalugava", "tulupa", "cama", "vasosofate",
    "daneragotu", "cobala", "lupo", "lecasona", "temamazota", "nara", "viso", "tedata",
    "zonetade", "cavagonari", "tubaba", "lala", "papocotu", "tugo", "tela", "xarila",
    "vamasa", "vifi", "soxatumo", "camala", "valalafifa", "sagosapo", "pomotazofa", "rivi",
    "gavitacana", "coletemofi", "betedana", "cosozoluxa", "camatugo", "faba", "zomava", "xatevixa",
    "cafa", "ladaxaba", "daca", "vifanateva", "fidabe", "lusavineri", "datulapa", "paratu",
    "sosasagopo", "molega", "nemopogofa", "raxaramo", "gorama", "marama", "zopaxale", "turanepo",
    "becadelefi", "dagote", "vira", "papate", "dene", "valefa", "barixatana", "cotabafisa",
    "falacole", "ribe", "catarademo", "capa", "dabago", "fasafaraga", "beponari", "zogagova",
    "rivade", "nefiso", "pafi", "samolu", "lelebega", "filubalufa", "rivipadeso", "lapomadava",
    "pofi", "garisa", "masosa", "fisago", "zodalu", "luvizode", "belalu", "rafigo",
    "pamotecone", "pogoca", "pavamoda", "pasagovi", "sasomovilu", "fiparizo", "tabafala", "betulude",
    "pane", "ribeso", "posotasa", "rilecobele", "saluso", "zone", "sovala", "tepo",
    "capafa", "falurifafi", "ridela", "farizogoxa", "dabetu", "tevimogo", "lefaconeta", "balazotuna",
    "tucatamata", "parifi", "nene", "vima", "balugama", "poba", "tesolura", "raba",
    "firabeta", "teri", "dezo", "netazo", "tatalu", "capavi", "lelexa", "gacagavara",
    "ragata", "mocacamara", "paviluzogo", "tupo", "zopasota", "podaga", "xagazolafa", "sana",
    "lexamatu", "zovizo", "moxa", "nepafipade", "sodaga", "pabamasane", "vamonele", "nelupamo",
    "facasomo", "barifivade", "beca", "vilelari", "pomo", "gomanadalu", "lafiderafa", "zoma",
    "figopovi", "tago", "tusofapo", "danevafi", "tuco", "vatamoda", "bamogo", "casa",
    "dete", "tedevi", "datatuna", "davirafamo", "mori", "cosana", "lata", "vabapo",
    "faxava", "fidecomoco", "fabebebe", "capapo", "visoluda", "vizolaxa", "palara", "vinasa",
    "vimana", "gabagopavi", "baga", "tugoxate", "vigolama",
]

# ENIGMA 1 (use while):
#   Qual é o MENOR número maior que 1000 que, ao mesmo tempo:
#     - dividido por 7 deixa resto 3
#     - dividido por 11 deixa resto 5
#     - dividido por 13 deixa resto 8
#   Comece em 1001 e vá somando 1 até achar. Use break quando achar.
#
# ENIGMA 2 (use for):
#   Na lista palavras existe UMA ÚNICA palavra que é um palíndromo
#   (se lê igual de trás para frente) com 7 letras ou mais.
#   Percorra a lista e guarde essa palavra. Use break quando achar.
#   Lembre: texto[::-1] inverte um texto.

# ---- escreva seu código abaixo desta linha ----

numero_secreto = 0
palindromo = ""

# ---- não mexa na linha abaixo ----
print("FLAG{" + str(numero_secreto) + "-" + palindromo + "}")

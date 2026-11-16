// Domande e risultati del quiz "Chi eri nella vita precedente?"
// Le stesse risposte danno sempre lo stesso risultato.
// Se cambi un risultato, rigenera anche le immagini di anteprima (cartella assets/r).
window.DOMANDE = [
  { testo: "Cosa ordini al bar?", risposte: ["Un caffè, al volo", "Un cappuccino, con calma", "Una spremuta: sono salutista", "Quello che prende chi paga", "Niente, sono qui per chiacchierare"] },
  { testo: "Il tuo posto preferito a una festa?", risposte: ["Al centro della pista", "Vicino al buffet", "Sul divano, a osservare tutti", "In cucina con i padroni di casa", "Vicino alla porta, pronto ad andarmene"] },
  { testo: "Il tuo difetto più simpatico?", risposte: ["Arrivo sempre in ritardo", "Parlo troppo", "Non so tenere un segreto", "Dico sempre \"ancora cinque minuti\"", "Mi perdo anche col navigatore"] }
];

window.RISULTATI = [
  "un generale che dava ordini solo a stomaco pieno",
  "una spia francese che non sapeva il francese",
  "una cantante di varietà con troppi ammiratori",
  "un piccione viaggiatore che sbagliava sempre indirizzo",
  "un medium che parlava solo con i cani",
  "un fantasma che non pagava l'affitto",
  "un cuoco di corte con una ricetta segreta",
  "un soldato che si perdeva anche nel corridoio",
  "un telegrafista che scriveva solo in rima",
  "un colonnello allergico alle divise",
  "una ballerina di tip tap con il passo pesante",
  "un postino che leggeva tutte le lettere",
  "un ufficiale che salutava anche i lampioni",
  "una spia che si travestiva sempre da tenda",
  "un marinaio che soffriva il mal di mare",
  "un mago che faceva sparire solo i suoi soldi",
  "un attore che dimenticava sempre l'ultima battuta",
  "un barbiere che sapeva tutti i segreti del paese",
  "un cavallo di legno che soffriva di claustrofobia",
  "un oracolo che rispondeva sempre \"dipende\"",
  "un filosofo greco che litigava con il condominio",
  "un gladiatore che chiedeva sempre il time-out",
  "un aviatore che aveva paura dell'altezza",
  "un detective che non trovava mai le chiavi",
  "una contessa che parlava solo con i ritratti",
  "un sarto che cuciva divise di una taglia in meno",
  "un trombettiere che suonava la sveglia alle undici",
  "un cuoco militare che bruciava anche l'acqua",
  "una spia che si faceva scoprire per troppa simpatia",
  "un ambasciatore che sbagliava sempre paese",
  "una cartomante che pescava solo il due di picche",
  "un fantasma timido che chiedeva permesso prima di apparire",
  "un giornalista che dava solo buone notizie",
  "un inventore di cose già inventate",
  "un generale che pianificava le battaglie a tombola",
  "un tenore che cantava solo sotto la doccia",
  "un cameriere che portava i piatti al tavolo sbagliato",
  "un cocchiere che si fermava a ogni osteria",
  "una spia con un cappello troppo vistoso",
  "un soldato che scriveva lettere d'amore per tutto il plotone",
  "un poeta che faceva rima solo con \"cuore\"",
  "un acrobata che inciampava sul tappeto",
  "un custode di museo che parlava con le statue",
  "un fornaio che impastava pensando alla guerra",
  "una spia che portava i baffi finti anche a casa",
  "un capitano che perdeva sempre la mappa",
  "un ventriloquo che litigava con il pupazzo",
  "una diva del cinema muto che parlava troppo",
  "un esploratore che si perdeva in centro città",
  "un contabile del regno che sbagliava le somme",
  "un cavaliere che aveva paura dei cavalli",
  "un monaco che non riusciva a stare zitto",
  "un cuoco che assaggiava tutto prima di servirlo. Tutto.",
  "una sentinella che si addormentava in piedi",
  "un cantastorie che svelava sempre il finale",
  "un geniere che smontava le radio per noia",
  "un fantasma che spaventava solo i gatti",
  "un pirata che soffriva il solletico",
  "un medico da campo con la calligrafia illeggibile",
  "un re senza corona ma con tanti debiti",
  "un corriere segreto che consegnava sempre in ritardo",
  "un musicista jazz che suonava una nota sola",
  "una spia che aveva bisogno del navigatore",
  "un vigile urbano dell'antica Roma",
  "un oste che annacquava il vino e lo ammetteva",
  "una principessa che preferiva la porchetta al caviale",
  "un soldato che marciava sempre col piede sbagliato",
  "un illusionista che svelava tutti i trucchi",
  "un astrologo che non trovava mai le stelle",
  "un generale con una collezione di cucchiaini",
  "un ladro gentiluomo che restituiva tutto il giorno dopo",
  "una sarta che sapeva i segreti di tutti i generali",
  "un fantasma che faceva \"buu\" con troppa educazione",
  "un capobanda che dirigeva al contrario",
  "un cuoco che salava tutto due volte",
  "un messaggero che dimenticava il messaggio",
  "una spia che si presentava dicendo \"sono una spia\"",
  "un pugile che chiedeva scusa dopo ogni colpo",
  "un tenente che non sapeva fare il nodo alla cravatta",
  "un oracolo greco con il telefono sempre occupato",
  "un mercante che vendeva sabbia nel deserto",
  "un parrucchiere di corte con le forbici ribelli",
  "un generale che si commuoveva alle parate",
  "un giocoliere che giocava solo con le uova",
  "un vicino di casa che bussava sempre all'ora di cena",
  "un fantasma che aveva paura del buio",
  "un soldato semplice con ambizioni da generale",
  "un conte decaduto che viveva di ricordi e caffè offerti",
  "una cantante d'opera che rompeva i bicchieri apposta",
  "un ingegnere che costruiva ponti per arrivare in cucina",
  "una spia che non teneva un segreto più di dieci minuti",
  "un capostazione che faceva partire i treni in anticipo",
  "un trovatore stonato ma molto convinto",
  "un esattore delle tasse che si commuoveva sempre",
  "un cuoco di trincea famoso per la frittata",
  "un ammiraglio che non sapeva nuotare",
  "un'indovina che indovinava solo il giorno dopo",
  "un soldato greco che voleva uscire per primo dal cavallo",
  "un domatore di leoni allergico ai gatti",
  "un primo attore che si inchinava anche agli applausi degli altri"
];

// Da risposte (3 numeri da 0 a 4) a risultato (da 1 a 100).
// Le 125 combinazioni vengono "mescolate" in modo fisso: tutti i 100 risultati sono raggiungibili.
window.calcolaRisultato = risposte => {
  const indice = risposte.reduce((n, r) => n * 5 + r, 0);   // 0..124
  return ((indice * 37 + 11) % 125) % 100 + 1;
};

// ---------- Legami tra due vite precedenti ----------
// Famiglia di ogni risultato (stesso ordine della lista RISULTATI):
// M militari · S spie · A artisti · F fantasmi e veggenti · K cuochi e osti · N nobili · C gente comune · X leggendari
window.FAMIGLIE = (
  "M S A X F F K M S M A C M S M A A C X F" +
  " X M M S N C M K S N F F C C M A K C S M" +
  " A A C K S M A A X N M C K M A M F X M N" +
  " S A S X K N M A F M S C F A K C S C M F" +
  " C C M A C F M N A C S C A N K M F M A A"
).split(" ");

const ORDINE_FAMIGLIE = "MSAFKNCX";
window.LEGAMI = {
  MM: ["il generale e l'unico soldato che non lo ascoltava mai", "due soldati che si erano persi andando al fronte", "compagni di trincea che si rubavano il rancio"],
  MS: ["una spia e il generale che le dava la caccia da anni", "un soldato e la spia che gli leggeva le lettere da casa", "due complici che vendevano piani di battaglia sbagliati"],
  MA: ["il soldato e la cantante degli spettacoli al fronte", "un ufficiale e l'attore che lo imitava in ogni spettacolo", "due commilitoni che mettevano in scena commedie in caserma"],
  MF: ["un soldato e il fantasma della caserma che lo svegliava di notte", "il generale e la cartomante che decideva le sue battaglie", "due reduci che parlavano con gli spiriti dei vecchi compagni"],
  MK: ["il generale e il cuoco del reggimento, l'unico che temeva", "un soldato e l'oste che gli faceva credito a fine mese", "due compagni d'armi che disertavano solo per andare a pranzo"],
  MN: ["il conte e la sua guardia del corpo, che scappava per prima", "un ufficiale innamorato di una contessa che non lo guardava nemmeno", "il re e il generale che vinceva le battaglie solo sulla carta"],
  MC: ["un soldato e il barbiere che sapeva della guerra prima di lui", "il capitano e il postino che consegnava gli ordini al reggimento sbagliato", "due vicini di casa: uno marciava, l'altro voleva dormire"],
  MX: ["due soldati chiusi nello stesso cavallo di legno, molto stretto", "il generale e il piccione che portava i suoi ordini all'indirizzo sbagliato", "un soldato e il pirata che gli aveva vinto la paga a carte"],
  SS: ["due spie che si pedinavano a vicenda senza saperlo", "due agenti segreti che si erano scambiati i travestimenti", "due spie innamorate della stessa informatrice"],
  SA: ["una spia travestita da attore e l'attore vero che non capiva niente", "la cantante di varietà e la spia che le scriveva i testi in codice", "due artisti di strada che erano in realtà agenti segreti"],
  SF: ["una spia e il medium che le passava informazioni dall'aldilà", "un detective e il fantasma testimone che nessuno ascoltava", "due agenti segreti che si davano appuntamento in un castello infestato"],
  SK: ["una spia e il fornaio che nascondeva i messaggi nel pane", "il detective e l'oste che sapeva sempre chi era passato dalla locanda", "due spie che si incontravano sempre nella stessa trattoria"],
  SN: ["una spia e l'ambasciatore che le raccontava tutto dopo il secondo bicchiere", "il ladro gentiluomo e la contessa che fingeva di non accorgersene", "due agenti segreti infiltrati allo stesso ballo di corte"],
  SC: ["una spia e il postino che leggeva le sue lettere prima di lei", "il detective e il barbiere che risolveva i casi mentre tagliava", "due vicini di casa che si spiavano dalla finestra"],
  SX: ["una spia e il piccione che portava i messaggi sbagliati", "due agenti nascosti nella pancia di un cavallo di legno", "il detective e il pirata che gli rubava sempre gli indizi"],
  AA: ["due attori che si rubavano sempre la scena", "due musicisti della stessa banda, sempre fuori tempo", "il mago e l'assistente che spariva davvero"],
  AF: ["un attore e il fantasma che infestava il suo teatro", "la cantante e la cartomante che le prevedeva sempre fischi", "il prestigiatore e il medium che si accusavano di imbrogliare"],
  AK: ["il tenore e l'oste che lo pagava in piatti di pasta", "la ballerina e il fornaio che le portava le paste di nascosto", "due artisti di strada che si esibivano davanti alla stessa trattoria"],
  AN: ["il buffone di corte e il re che lo prendeva troppo sul serio", "la diva e il conte che le mandava fiori senza firmare", "il cantante di corte e la principessa che si tappava le orecchie"],
  AC: ["il clown e il barbiere che gli rifaceva il trucco", "il poeta e il postino che consegnava le sue lettere d'amore", "l'attore e il vicino che batteva sul muro durante le prove"],
  AX: ["il domatore e il cavallo di legno che non riusciva a domare", "il cantastorie e il pirata che gli rubava le storie", "l'acrobata e il piccione che gli faceva concorrenza in piazza"],
  FF: ["due fantasmi che infestavano la stessa casa e non si sopportavano", "due oracoli che davano risposte opposte", "due fantasmi che dividevano lo stesso lenzuolo"],
  FK: ["il fantasma dell'osteria e il cuoco che gli lasciava sempre un piatto", "la cartomante e il fornaio che le chiedeva i numeri del lotto", "un medium e il cuoco che chiedeva le ricette allo spirito della nonna"],
  FN: ["il fantasma del castello e la contessa che lo trattava da maggiordomo", "l'indovino di corte e il re che non voleva sapere niente", "un oracolo e il nobile che chiedeva solo previsioni del tempo"],
  FC: ["un fantasma e l'inquilino che non si spaventava mai", "la cartomante e il barbiere che si contendevano i pettegolezzi del paese", "un medium e il postino che consegnava lettere dall'aldilà"],
  FX: ["l'oracolo e il filosofo greco che contestava ogni profezia", "un fantasma e il pirata che lo voleva come mozzo", "il medium e il piccione che portava messaggi tra i due mondi"],
  KK: ["due fornai rivali sulla stessa strada", "il cuoco e il cameriere che si mangiava metà dei piatti", "due osti che litigavano su chi faceva la frittata migliore"],
  KN: ["il cuoco di corte e il conte che rimandava indietro ogni piatto", "l'oste e il nobile decaduto che non pagava mai il conto", "la principessa e il fornaio che le portava la porchetta di nascosto"],
  KC: ["l'oste e il cliente fisso che non pagava mai", "il cuoco e il postino che passava sempre all'ora di pranzo", "il fornaio e il vicino che entrava solo per le briciole"],
  KX: ["il cuoco e il pirata che gli rubava sempre le provviste", "l'oste e il filosofo greco che pagava con le sue massime", "il cuoco che preparò il pranzo per i soldati nel cavallo di legno"],
  NN: ["il re e la regina che litigavano su chi comandava", "due contesse in gara per il cappello più assurdo", "due nobili decaduti che si offrivano il caffè a turno"],
  NC: ["il conte e il maggiordomo che sapeva tutto di tutti", "l'esattore e l'unico contribuente onesto del regno", "la contessa e la sarta che conosceva tutti i suoi segreti"],
  NX: ["il re e il cavallo di legno che gli avevano regalato (pessima idea)", "l'ambasciatore e il pirata con cui firmò un trattato improbabile", "la principessa e il piccione che portava le sue lettere d'amore"],
  CC: ["vicini di casa che litigavano per le scale del condominio", "il barbiere e il cliente che non voleva mai tagliare", "due viaggiatori che perdevano sempre lo stesso treno"],
  CX: ["il vigile e il pirata che parcheggiava la nave in doppia fila", "il postino e il piccione viaggiatore che gli rubava il lavoro", "l'esploratore e il mercante che gli vendeva mappe sbagliate"],
  XX: ["due soldati greci che volevano uscire per primi dal cavallo", "il filosofo e il piccione che ascoltava tutte le sue lezioni", "due pirati che si contendevano la stessa mappa sbagliata"]
};
window.ANIME_GEMELLE = "la stessa persona! Gli spiriti dicono che siete anime gemelle: a teatro sedetevi vicini";

// Legame tra due risultati (numeri da 1 a 100): sempre lo stesso per la stessa coppia, in qualunque ordine
window.calcolaLegame = (a, b) => {
  if (a === b) return window.ANIME_GEMELLE;
  const fa = window.FAMIGLIE[a - 1], fb = window.FAMIGLIE[b - 1];
  const chiave = ORDINE_FAMIGLIE.indexOf(fa) <= ORDINE_FAMIGLIE.indexOf(fb) ? fa + fb : fb + fa;
  const lista = window.LEGAMI[chiave];
  // Preferisce la variante che nomina gli stessi personaggi (attore, fantasma, cavallo…)
  const radici = t => new Set(t.toLowerCase().replace(/[^a-zàèéìòù ]/g, " ").split(" ")
    .filter(w => w.length >= 4 && !PAROLE_VUOTE.has(w)).map(w => w.slice(0, 5)));
  const nostre = new Set([...radici(window.RISULTATI[a - 1]), ...radici(window.RISULTATI[b - 1])]);
  const punti = lista.map(l => [...radici(l)].filter(r => nostre.has(r)).length);
  const max = Math.max(...punti);
  const migliori = lista.filter((_, i) => punti[i] === max);
  return migliori[(Math.min(a, b) * 31 + Math.max(a, b) * 17) % migliori.length];
};
const PAROLE_VUOTE = new Set(["sempre", "solo", "della", "dello", "delle", "degli", "nella", "nello", "anche", "tutti", "tutto", "tutte",
  "quando", "prima", "dopo", "come", "aveva", "erano", "faceva", "sapeva", "stesso", "stessa", "molto", "ogni", "suoi", "sue", "suo", "loro"]);

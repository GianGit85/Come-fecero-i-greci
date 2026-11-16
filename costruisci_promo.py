src = open("/home/user/specchio_2/index.html").read()
def tra(a, b):
    i = src.index(a); j = src.index(b, i); return src[i:j]
css = tra("<style>", "</style>") + "</style>"
strofina = tra("  // ---------- 2. Strofina la sfera ----------", "  // ---------- Suoni")
suoni = tra("  // ---------- Suoni (generati al momento, nessun file) ----------", "  // ---------- Sfera 3D")
sfera = tra("  // ---------- Sfera 3D (WebGL, senza librerie) ----------", "  // ---------- Lettere ritagliate")
lettere = tra("  // ---------- Lettere ritagliate ----------", "  // ---------- Rivelazione")
scint = tra("  function scintille() {", "  // ---------- 3. Foto per la storia")
disegno = tra("  function titolo3D(", "  function componiFoto()")
biglietto = tra("  // Biglietto di carta strappata", "  function scarica()")

# niente specchio nella pagina promo: il "?" va dritto e la sfera non si riflette
sfera = sfera.replace('vc.save(); vc.translate(128, 136); vc.scale(-1, 1); vc.fillText("?", 0, 0); vc.restore();',
                      'vc.fillText("?", 128, 136);')
sfera = sfera.replace("const disegna = (t, specchio = true) => {", "const disegna = (t, specchio = false) => {")
assert 'vc.fillText("?", 128, 136);' in sfera and "specchio = false" in sfera
# niente interruttore effetto sfera
sfera = sfera.replace('    $("btnMagia").classList.toggle("on", !!defMeta);\n', '')

head = '''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, user-scalable=no">
<meta name="theme-color" content="#0b0705">
<title>Il medium ha una profezia per te 🔮</title>
<meta name="description" content="Come fecero i Greci, una commedia di Copia Incolla. Strofina la sfera e scopri la tua profezia.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://giangit85.github.io/Come-fecero-i-greci/">
<meta property="og:title" content="Il medium ha una profezia per te 🔮">
<meta property="og:description" content="Come fecero i Greci, una commedia di Copia Incolla. Strofina la sfera e scopri la tua profezia.">
<meta property="og:image" content="https://giangit85.github.io/Come-fecero-i-greci/assets/anteprima.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="it_IT">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/luckiest-guy.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/special-elite.woff2" as="font" type="font/woff2" crossorigin>
'''
extra_css = '''<style>
  .info { font-family: var(--titolo); text-align: center; line-height: 1.25; }
  .info .quando { color: var(--giallo); font-size: 1.05rem; text-shadow: 0 2px 0 #6b4a10; }
  .info .dove { color: var(--rosso); font-size: .95rem; text-shadow: 0 2px 0 #5a140e; }
  .azioni { display: flex; flex-direction: column; align-items: center; gap: 10px; margin-top: 4px; }
  .bottone.prenota { background: var(--rosso); color: #fff; box-shadow: 0 5px 0 #7a1d14, 0 9px 18px rgba(0,0,0,.6); text-decoration: none; display: inline-block; }
  .bottone.prenota:active { box-shadow: 0 1px 0 #7a1d14, 0 4px 10px rgba(0,0,0,.6); }
  .riga-link { display: flex; gap: 14px; justify-content: center; }
  .sfera { cursor: default; }
</style>
'''
body = '''</head>
<body>
<div class="fumo"><i></i><i></i><i></i></div>
<button id="btnAudio" class="audio" aria-label="Suoni">🔊</button>
<div id="diag"></div>
<script src="profezie.js"></script>
<script>
  (() => { const mostra = m => { const d = document.getElementById("diag"); if (d) d.textContent = "⚠ " + m; };
    window.addEventListener("error", e => mostra((e.message || "errore") + (e.lineno ? " (riga " + e.lineno + ")" : "")));
    window.addEventListener("unhandledrejection", e => mostra("promise: " + (e.reason && (e.reason.message || e.reason.name) || e.reason)));
  })();
</script>

<!-- 1. INTRO -->
<section id="intro" class="schermata attiva">
  <div class="piccolo">UNA COMMEDIA TEATRALE DI</div>
  <img class="logo" src="assets/logo-copia-incolla.jpg" alt="Copia Incolla">
  <h1 class="titolo">COME FECERO<br>I GRECI</h1>
  <div class="info"><div class="quando" id="infoQuando"></div><div class="dove" id="infoDove"></div></div>
  <p class="medium"><span id="testoMedium"></span><span class="cursore">▌</span></p>
  <button id="btnEntra" class="bottone nascosto">Tocca per iniziare</button>
  <button id="btnSfera" class="bottone nascosto" style="display:none">Consulta la sfera 🔮</button>
</section>

<!-- 2. SFERA -->
<section id="scena" class="schermata">
  <h2 class="titolo mini">COME FECERO I GRECI</h2>
  <div class="postazione">
    <div id="sfera" class="sfera senza-camera">
      <div class="vuota">?</div>
      <canvas id="vetro3d"></canvas>
      <canvas id="nebbia"></canvas>
      <div class="vetro"></div>
    </div>
    <div class="base"><i class="piede"></i><i class="corpo"></i><i class="anello"></i></div>
    <div id="scintille" class="scintille"></div>
  </div>
  <div id="risposta" class="risposta">
    <div class="suggerimento">Strofina la sfera col dito…</div>
  </div>
</section>

<script>
(() => {
  // ====== DATI DELLO SPETTACOLO: per una replica basta cambiare queste righe ======
  const SPETTACOLO = {
    quando: "20 NOVEMBRE 2026 · ORE 21:00",
    dove: "TEATRO SANT'ANNA · TORINO",
    prenota: "https://forms.gle/PsdN4vKsmonuJ4nEA",
    sito: "https://giangit85.github.io/Come-fecero-i-greci/"
  };
  // =================================================================================
  const TITOLO = "COME FECERO I GRECI";
  const INSTAGRAM = "@copia.in.colla";
  const SOGLIA = 0.55;
  const PROFEZIE = (window.PROFEZIE && window.PROFEZIE.length) ? window.PROFEZIE
    : ["Gli spiriti vedono una risata nel tuo futuro. Molto vicino. Tipo tra dieci minuti."];
  let ultimaProfezia = -1, profezia = "", fileStoria = null, urlStoria = null;
  function nuovaProfezia() {
    let i; do { i = Math.floor(Math.random() * PROFEZIE.length); } while (PROFEZIE.length > 1 && i === ultimaProfezia);
    ultimaProfezia = i; return PROFEZIE[i];
  }
  const $ = id => document.getElementById(id);
  const attesa = ms => new Promise(ok => setTimeout(ok, ms));
  const video = document.createElement("video");          // nessuna fotocamera in questa pagina
  const senzaCamera = true;
  const logo = new Image(); logo.src = "assets/logo-copia-incolla.jpg";
  const fontPronti = Promise.all([
    document.fonts.load('40px "Luckiest Guy"'), document.fonts.load('40px "Special Elite"')
  ]).catch(() => {});
  $("infoQuando").textContent = SPETTACOLO.quando;
  $("infoDove").textContent = SPETTACOLO.dove;

  function mostra(id) {
    document.querySelectorAll(".schermata").forEach(s => s.classList.toggle("attiva", s.id === id));
  }
  async function scrivi(el, testo, vel = 50) {
    el.textContent = "";
    for (let i = 1; i <= testo.length; i++) {
      el.textContent = testo.slice(0, i);
      const ch = testo[i - 1];
      if (ch !== "…") try { suono.tasto(ch); } catch (_) {}
      await attesa(ch === "\\n" ? 350 : ch === "…" ? 400 : ch === " " ? 55 : vel);
    }
  }

  // ---------- 1. Intro ----------
  (async () => { await attesa(1500); $("btnEntra").classList.remove("nascosto"); })();
  $("btnEntra").addEventListener("click", async () => {
    suono.avvia();
    $("btnEntra").style.display = "none";
    await scrivi($("testoMedium"), "Sai qual è la cosa più importante di questo spettacolo?\\nLo scoprirai solo in sala.\\n\\nIntanto… il medium ha una profezia per te.");
    $("btnSfera").style.display = ""; await attesa(50); $("btnSfera").classList.remove("nascosto");
  });
  $("btnSfera").addEventListener("click", () => { suono.avvia(); suono.apri(); apriScena(); });

'''
fine = '''
  // ---------- Rivelazione della profezia ----------
  async function rivela() {
    svanita = true;
    canvas.classList.add("svanita");
    svanitaDa = performance.now();
    setTimeout(() => document.querySelector(".postazione").classList.add("dopo"), 1500);
    if (navigator.vibrate) navigator.vibrate([40, 60, 90]);
    suono.rivela();
    scintille();
    const box = $("risposta");
    box.innerHTML = '<div class="medium" style="min-height:0"><span id="spiriti"></span></div>';
    await attesa(500);
    await scrivi($("spiriti"), "Gli spiriti hanno parlato…", 50);
    await mostraProfezia(box);
  }

  async function mostraProfezia(box) {
    profezia = nuovaProfezia();
    box.querySelectorAll(".profezia, .azioni").forEach(n => n.remove());
    box.insertAdjacentHTML("beforeend", '<div class="profezia"><small>LA PROFEZIA DEL MEDIUM</small><span id="testoProfezia"></span></div>');
    preparaStoria();                                   // la storia è pronta prima del tocco su "Condividi"
    await scrivi($("testoProfezia"), profezia, 40);
    box.insertAdjacentHTML("beforeend", `<div class="azioni">
        <button id="btnCondividi" class="bottone">📲 Condividi la profezia</button>
        <a id="btnPrenota" class="bottone prenota" href="${SPETTACOLO.prenota}" target="_blank" rel="noopener">🎟️ Prenota il tuo posto</a>
        <div class="riga-link"><button id="btnAltra" class="link">Un'altra profezia</button><button id="btnSalva" class="link">Salva l'immagine</button></div>
      </div>`);
    $("btnCondividi").addEventListener("click", condividi);
    $("btnSalva").addEventListener("click", salva);
    $("btnAltra").addEventListener("click", () => mostraProfezia(box));
  }

  // ---------- Storia da condividere ----------
  async function preparaStoria() {
    fileStoria = null;
    await fontPronti;
    const tela = componiStoria();
    const blob = await new Promise(ok => tela.toBlob(ok, "image/jpeg", 0.9));
    if (urlStoria) URL.revokeObjectURL(urlStoria);
    urlStoria = URL.createObjectURL(blob);
    fileStoria = new File([blob], "profezia-come-fecero-i-greci.jpg", { type: "image/jpeg" });
  }

  function componiStoria() {
    const W = 1080, H = 1920;
    const t = document.createElement("canvas"); t.width = W; t.height = H;
    const c = t.getContext("2d");
    const sf = c.createRadialGradient(W / 2, H * .45, 60, W / 2, H * .45, H * .75);
    sf.addColorStop(0, "#2a1c13"); sf.addColorStop(.6, "#120c08"); sf.addColorStop(1, "#050302");
    c.fillStyle = sf; c.fillRect(0, 0, W, H);
    c.globalCompositeOperation = "screen";
    nuvola(c, 150, 1250, 650, "255,90,200", .38);
    nuvola(c, 950, 1150, 650, "79,216,255", .32);
    nuvola(c, 540, 300, 600, "122,92,255", .18);
    c.globalCompositeOperation = "source-over";

    c.fillStyle = "#f4e9d0"; c.textAlign = "center"; c.textBaseline = "alphabetic";
    c.font = '30px "Special Elite", monospace';
    c.fillText("UNA COMMEDIA TEATRALE DI", W / 2, 78);
    if (logo.complete && logo.naturalWidth) {
      const lw = 160, lh = lw * logo.naturalHeight / logo.naturalWidth;
      c.save(); c.translate(W / 2, 100 + lh / 2); c.rotate(-3 * Math.PI / 180);
      c.shadowColor = "rgba(0,0,0,.6)"; c.shadowBlur = 24; c.shadowOffsetY = 8;
      c.drawImage(logo, -lw / 2, -lh / 2, lw, lh); c.restore();
    }
    c.font = '86px "Luckiest Guy", sans-serif';
    titolo3D(c, TITOLO, W / 2, 365, Math.min(86, 86 * 980 / c.measureText(TITOLO).width));

    // Sfera con il punto interrogativo: la risposta vera si scopre solo in sala
    const cx = W / 2, cy = 720, R = 290;
    basamento(c, cx, cy + R * .74, R * 1.3);
    c.save(); c.globalCompositeOperation = "screen";
    nuvola(c, cx - 50, cy, R * 1.55, "255,90,200", .55);
    nuvola(c, cx + 50, cy, R * 1.55, "79,216,255", .45);
    c.restore();
    if (sfera3D) { sfera3D.disegna(performance.now()); c.drawImage(sfera3D.canvas, cx - R, cy - R, R * 2, R * 2); }
    else {
      const g = c.createRadialGradient(cx - R * .3, cy - R * .3, 10, cx, cy, R);
      g.addColorStop(0, "#6a4a9a"); g.addColorStop(1, "#140a24");
      c.fillStyle = g; c.beginPath(); c.arc(cx, cy, R, 0, Math.PI * 2); c.fill();
      c.fillStyle = "rgba(230,220,255,.4)"; c.font = `${R}px "Luckiest Guy", sans-serif`; c.fillText("?", cx, cy + R * .35);
    }

    c.fillStyle = "#f4e9d0"; c.font = '36px "Special Elite", monospace';
    c.fillText("IL MEDIUM HA PARLATO", W / 2, 1150);
    bigliettoProfezia(c, profezia, W / 2, 1180, 920);

    c.font = '54px "Luckiest Guy", sans-serif';
    c.fillStyle = "#6b4a10"; c.fillText(SPETTACOLO.quando, W / 2, 1529);
    c.fillStyle = "#f2c230"; c.fillText(SPETTACOLO.quando, W / 2, 1525);
    c.font = '48px "Luckiest Guy", sans-serif';
    c.fillStyle = "#5a140e"; c.fillText(SPETTACOLO.dove, W / 2, 1599);
    c.fillStyle = "#e04a3a"; c.fillText(SPETTACOLO.dove, W / 2, 1595);

    disegnaCollage(c, creaLettere("E LA TUA?"), W / 2, 1650, 82, 104, 10, 34);
    c.fillStyle = "#f4e9d0"; c.font = '32px "Special Elite", monospace';
    c.fillText(SPETTACOLO.sito.replace(/^https?:\\/\\//, "").replace(/\\/$/, ""), W / 2, 1830);
    c.font = '28px "Special Elite", monospace'; c.fillStyle = "rgba(244,233,208,.75)";
    c.fillText(INSTAGRAM, W / 2, 1878);
    return t;
  }

  async function condividi() {
    const testo = `🔮 Il medium ha una profezia anche per te. Come fecero i Greci, ${SPETTACOLO.quando.toLowerCase()}, ${SPETTACOLO.dove.toLowerCase()}.`;
    if (fileStoria && navigator.canShare && navigator.canShare({ files: [fileStoria] })) {
      try { await navigator.share({ files: [fileStoria], text: testo + " " + SPETTACOLO.sito }); return; }
      catch (e) { if (e.name === "AbortError") return; }
    }
    if (navigator.share) {                                    // niente immagine: condivide almeno il link
      try { await navigator.share({ title: "Il medium ha una profezia per te", text: testo, url: SPETTACOLO.sito }); return; }
      catch (e) { if (e.name === "AbortError") return; }
    }
    salva();
  }
  function salva() {
    if (!urlStoria) return;
    const a = document.createElement("a"); a.href = urlStoria; a.download = "profezia-come-fecero-i-greci.jpg";
    document.body.appendChild(a); a.click(); a.remove();
  }
})();
</script>
</body>
</html>
'''
out = head + css + "\n" + extra_css + body + strofina + suoni + sfera + lettere + scint + disegno + biglietto + fine
open("/home/user/come-fecero-i-greci/index.html", "w").write(out)
print(len(out))

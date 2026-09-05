from flask import Flask, request, jsonify

app = Flask(__name__)


def mention_pour_note(note):
    """Barème des mentions pour une note sur 20."""
    if note == 20:
        return "Excellent"
    elif note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"


# Couleur associée à chaque mention (pour l'affichage du badge)
COULEURS_MENTION = {
    "Excellent": "#7c3aed",
    "Très bien": "#059669",
    "Bien": "#0891b2",
    "Assez bien": "#2563eb",
    "Passable": "#d97706",
    "Insuffisant": "#dc2626",
}


@app.route('/api/mention')
def api_mention():
    """Endpoint JSON utilisé par l'intégration Moodle/Odoo (flux notes & mentions).

    Exemple : GET /api/mention?note=14.5 -> {"note": 14.5, "sur": 20, "mention": "Bien"}
    """
    note_saisie = request.args.get('note')
    if note_saisie is None:
        return jsonify({"erreur": "Paramètre 'note' manquant."}), 400
    try:
        note = float(note_saisie)
    except ValueError:
        return jsonify({"erreur": "La note doit être un nombre."}), 400
    if not 0 <= note <= 20:
        return jsonify({"erreur": "La note doit être comprise entre 0 et 20."}), 400
    return jsonify({"note": note, "sur": 20, "mention": mention_pour_note(note)})


# --- Logo IFPIG (SVG en ligne : aucun fichier image à héberger) ---------------
LOGO_IFPIG = """
<svg class="logo" viewBox="0 0 252 44" role="img" aria-label="IFPIG">
  <defs>
    <linearGradient id="g-logo" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#7c3aed"/>
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="92" height="44" rx="12" fill="url(#g-logo)"/>
  <text x="46" y="29" class="logo-sigle">IFPIG</text>
  <text x="104" y="27" class="logo-sous">Institut de formation</text>
</svg>
"""

# --- Gabarit HTML de la page --------------------------------------------------
PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Calculateur de mention — IFPIG</title>
<style>
  :root {{
    --fond: #f4f6fb;
    --carte: #ffffff;
    --texte: #111827;
    --doux: #6b7280;
    --bord: #e5e7eb;
    --primaire: #2563eb;
    --accent: #7c3aed;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 96px 20px 40px;
    font-family: "Segoe UI", Inter, system-ui, -apple-system, sans-serif;
    color: var(--texte);
    background:
      radial-gradient(900px 500px at 10% -10%, #dbeafe 0%, transparent 60%),
      radial-gradient(800px 500px at 100% 0%, #ede9fe 0%, transparent 55%),
      var(--fond);
  }}

  /* Logo dans le coin haut-gauche */
  .coin-logo {{ position: fixed; top: 22px; left: 26px; z-index: 10; }}
  .logo {{ height: 44px; width: auto; display: block; }}
  .logo-sigle {{
    font: 700 21px/1 "Segoe UI", Inter, system-ui, sans-serif;
    fill: #ffffff; text-anchor: middle; letter-spacing: 1.8px;
  }}
  .logo-sous {{
    font: 600 10px/1 "Segoe UI", Inter, system-ui, sans-serif;
    fill: #8b93a3; letter-spacing: .9px; text-transform: uppercase;
  }}

  .carte {{
    width: 100%;
    max-width: 440px;
    background: var(--carte);
    border: 1px solid var(--bord);
    border-radius: 20px;
    padding: 34px 32px 30px;
    box-shadow: 0 18px 45px -18px rgba(17, 24, 39, .28);
  }}
  .etiquette {{
    display: inline-block;
    font-size: 11px; font-weight: 700;
    letter-spacing: .1em; text-transform: uppercase;
    color: var(--accent); background: #f3e8ff;
    padding: 5px 11px; border-radius: 999px; margin-bottom: 14px;
  }}
  h1 {{ margin: 0 0 6px; font-size: 26px; letter-spacing: -.4px; }}
  .intro {{ margin: 0 0 26px; color: var(--doux); font-size: 14.5px; line-height: 1.5; }}

  label {{ display: block; font-size: 13.5px; font-weight: 600; margin-bottom: 8px; }}
  .champ {{ position: relative; }}
  input[type=number] {{
    width: 100%;
    font-size: 26px; font-weight: 600;
    padding: 14px 62px 14px 18px;
    border: 1.5px solid var(--bord);
    border-radius: 12px;
    background: #fbfcfe;
    color: var(--texte);
    outline: none;
    transition: border-color .15s, box-shadow .15s;
  }}
  input[type=number]:focus {{
    border-color: var(--primaire);
    box-shadow: 0 0 0 4px rgba(37, 99, 235, .14);
    background: #fff;
  }}
  input[type=number]::-webkit-outer-spin-button,
  input[type=number]::-webkit-inner-spin-button {{
    -webkit-appearance: none; margin: 0;
  }}
  input[type=number] {{ -moz-appearance: textfield; appearance: textfield; }}
  .sur20 {{
    position: absolute; right: 18px; top: 50%; transform: translateY(-50%);
    color: var(--doux); font-size: 16px; font-weight: 600; pointer-events: none;
  }}
  button {{
    width: 100%; margin-top: 16px; padding: 14px;
    font-size: 15.5px; font-weight: 600; color: #fff;
    border: 0; border-radius: 12px; cursor: pointer;
    background: linear-gradient(135deg, var(--primaire), var(--accent));
    box-shadow: 0 10px 22px -10px rgba(37, 99, 235, .8);
    transition: transform .12s, box-shadow .12s, filter .12s;
  }}
  button:hover {{ filter: brightness(1.06); transform: translateY(-1px); }}
  button:active {{ transform: translateY(0); }}

  .resultat {{
    margin-top: 26px; padding-top: 24px;
    border-top: 1px dashed var(--bord); text-align: center;
  }}
  .note-obtenue {{ font-size: 15px; color: var(--doux); margin: 0 0 12px; }}
  .note-obtenue strong {{ color: var(--texte); font-size: 20px; }}
  .badge {{
    display: inline-block; padding: 10px 22px; border-radius: 999px;
    font-size: 19px; font-weight: 700; color: #fff; letter-spacing: .2px;
  }}
  .jauge {{
    height: 8px; border-radius: 999px; background: var(--bord);
    overflow: hidden; margin-top: 20px;
  }}
  .jauge span {{ display: block; height: 100%; border-radius: 999px; }}
  .erreur {{
    margin-top: 20px; padding: 12px 14px; border-radius: 10px;
    background: #fef2f2; border: 1px solid #fecaca;
    color: #b91c1c; font-size: 14px;
  }}

  @media (prefers-color-scheme: dark) {{
    :root {{
      --fond: #0b1120; --carte: #131c2e; --texte: #e9edf5;
      --doux: #94a3b8; --bord: #24304a;
    }}
    body {{
      background:
        radial-gradient(900px 500px at 10% -10%, #16264a 0%, transparent 60%),
        radial-gradient(800px 500px at 100% 0%, #2a1a4a 0%, transparent 55%),
        var(--fond);
    }}
    .logo-sous {{ fill: #7c8598; }}
    .etiquette {{ background: #2c1d4d; }}
    input[type=number],
    input[type=number]:focus {{ background: #0e1728; }}
    .erreur {{ background: #3b1418; border-color: #7f1d1d; color: #fca5a5; }}
  }}
  @media (max-width: 480px) {{
    .coin-logo {{ top: 16px; left: 18px; }}
    .carte {{ padding: 28px 22px 24px; }}
  }}
</style>
</head>
<body>
  <div class="coin-logo">{logo}</div>

  <main class="carte">
    <span class="etiquette">Évaluation</span>
    <h1>Calculateur de mention</h1>
    <p class="intro">Saisissez une note sur 20 pour obtenir la mention correspondante.</p>

    <form method="GET" action="/">
      <label for="note">Votre note</label>
      <div class="champ">
        <input type="number" id="note" name="note" min="0" max="20" step="1"
               value="{valeur}" placeholder="0" required autofocus>
        <span class="sur20">/ 20</span>
      </div>
      <button type="submit">Calculer la mention</button>
    </form>

    {bloc_resultat}

  </main>
</body>
</html>
"""


@app.route('/')
def calculer_mention():
    """Page web : formulaire de saisie + affichage de la mention."""
    note_saisie = request.args.get('note')

    # Aucune note saisie : on affiche le formulaire vide
    if note_saisie is None:
        return PAGE.format(logo=LOGO_IFPIG, valeur="", bloc_resultat="")

    try:
        note = int(note_saisie)
    except ValueError:
        erreur = "<div class='erreur'>Veuillez entrer un nombre entier valide.</div>"
        return PAGE.format(logo=LOGO_IFPIG, valeur="", bloc_resultat=erreur)

    if not 0 <= note <= 20:
        erreur = "<div class='erreur'>La note doit être comprise entre 0 et 20.</div>"
        return PAGE.format(logo=LOGO_IFPIG, valeur="", bloc_resultat=erreur)

    mention = mention_pour_note(note)
    couleur = COULEURS_MENTION[mention]
    pourcentage = note / 20 * 100

    bloc_resultat = f"""
    <div class="resultat">
      <p class="note-obtenue">Note obtenue : <strong>{note}/20</strong></p>
      <span class="badge" style="background:{couleur}">{mention}</span>
      <div class="jauge">
        <span style="width:{pourcentage:.0f}%; background:{couleur}"></span>
      </div>
    </div>
    """
    return PAGE.format(logo=LOGO_IFPIG, valeur=note, bloc_resultat=bloc_resultat)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# Notes de cours (exercices precedents, conserves pour revision)
# =============================================================================
# n1 = 1
# n2 = 2.3
# n3 = 3
# addition = n1 + n2 + n3
# multiplication = n1 * n2 * n3
# print("l'addition de n1, n2, n3 est:", addition)
# print("la multiplication de n1, n2, n3 est:", int(multiplication))

# def bonjour(prenom="Philippe"):
#     print("Bonjour", prenom, "!", "Comment vas-tu ?")
# bonjour("Nathan")

# def calculatrice(a, b):
#     somme = a + b
#     produit = a * b
#     return somme, produit
# print(f"La somme et le produit de 5 et 3 sont: {calculatrice(5, 3)}")

# prix = 100.3456
# print(f"le prix est {prix:.2f} CHF")

# def boucle():
#     for i in range(5):
#         print("i=", i)

# def boucle2():
#     i = 0
#     while i < 5:
#         print("i=", i)
#         i += 1

# def boucle3():
#     i = 0
#     while True:
#         print("i=", i)
#         i += 1
#         if i >= 5:
#             break

# age = 25
# print(type(age))
# print("36" + str(36))

# prenom = input("Quel est ton prenom ? ")
# if prenom:
#     print(f"Bonjour, je m'appelle {prenom} !")
# else:
#     print("Vous n'avez rien saisi !")

# age = int(input("Quel age as-tu ? "))
# permis = True
# if age >= 18:
#     if permis:
#         print(f"Tu as {age} ans et tu as le permis, tu peux conduire !")
#     else:
#         print(f"Tu as {age} ans mais tu n'as pas le permis.")
# else:
#     print(f"Tu as {age} ans, tu n'as pas l'age requis pour conduire !")

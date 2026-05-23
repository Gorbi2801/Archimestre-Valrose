import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

# ── Chargement du token depuis le fichier .env ──────────────────────────────
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# ── Configuration des intents (permissions du bot) ──────────────────────────
intents = discord.Intents.default()
intents.members = True   # Indispensable pour lire la liste des membres

bot = commands.Bot(command_prefix="!", intents=intents)


# ══════════════════════════════════════════════════════════════════════════════
# ── EMOJIS PERSONNALISÉS ─────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

EMOJI_NAISSANCE   = "<:enfant:1305837153821130804>"
EMOJI_RECRUTEMENT = "<:officier:1277990678781100116>"
EMOJI_CANDIDATURE = "<:roturier:1277990392742285405>"
EMOJI_OUVERT      = "<:check:1274710088107692094>"
EMOJI_FERME       = "<:false:1274710086505332757>"

# Rôle global Lady (affiché séparément dans chaque maison, sans slot max)
ROLE_LADY_ID = 1267815975273631810


# ══════════════════════════════════════════════════════════════════════════════
# ── CONFIGURATION DES FACTIONS ───────────────────════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
#
# Pour ajouter une région, copie un bloc existant et remplis les IDs.
# Pour ajouter une maison, ajoute une entrée dans la liste "maisons".
#
# Types de maison :
#   "suzeraine" -> utilise role_suzerain (ou role_seigneur_override si défini)
#   "banneret"  -> utilise role_banneret
#   "special"   -> organisation sans seigneur (ex: Garde Royale)

FACTIONS = {

    "Couronne": {
        "color"         : 0xF0A500,
        "coat_emoji"    : "<:coat_targ:1274485044941029498>",
        "role_region"   : 1267815975286210638,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons": [
            {
                "nom"                   : "Targaryen",
                "role_id"               : 1267815975248597072,
                "type"                  : "suzeraine",
                "max_membres"           : 8,
                "role_seigneur_override": 1267815975320031392,
                "seigneur_label"        : "Roi",
            },
            {
                "nom"         : "Castelfoyer",
                "role_id"     : 1444664290912243762,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Sombrelyn",
                "role_id"     : 1348012851608158320,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Rosby",
                "role_id"     : 1444664287745413201,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Massey",
                "role_id"     : 1348644044519112724,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Garde Royale",
                "role_id"     : 1267815975265501230,
                "type"        : "special",
                "label"       : "Garde royaux",
                "max_membres" : 6,
                "chef_role_id": 1267815975303249976,
                "chef_label"  : "Lord-Commandant de la Garde Royale",
                "max_chef"    : 1,
            },
        ]
    },

    "Peyredragon": {
        "color"         : 0xC41E3A,
        "coat_emoji"    : "<:coat_targ:1274485044941029498>",
        "role_region"   : 1267815975286210637,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [            
            {
                "nom"         : "Velaryon",
                "role_id"     : 1267815975236145246,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Celtigar",
                "role_id"     : 1267815975236145245,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Solverre",
                "role_id"     : 1444664289532182589,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Orage": {
        "color"         : 0xF0C040,
        "coat_emoji"    : "<:coat_bara:1274485037227704400>",
        "role_region"   : 1267815975286210635,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Barathéon",
                "role_id"     : 1267815975219363966,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Caron",
                "role_id"     : 1282093811606229095,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Torth",
                "role_id"     : 1282094331003539599,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Selmy",
                "role_id"     : 1350251038770466827,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Dondarrion",
                "role_id"     : 1444664291969208451,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Wylde",
                "role_id"     : 1444664466976411711,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Penrose",
                "role_id"     : 1444664467706089658,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Morrigen",
                "role_id"     : 1444664468372979752,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Connington",
                "role_id"     : 1287447209432059924,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Swann",
                "role_id"     : 1444767820167516343,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Bief": {
        "color"         : 0x2D7A27,
        "coat_emoji"    : "<:coat_tyrell:1274485048736878613>",
        "role_region"   : 1267815975286210634,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Tyrell",
                "role_id"     : 1267815975219363964,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Redwyne",
                "role_id"     : 1267815975219363963,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Hightower",
                "role_id"     : 1267815975210713127,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Tarly",
                "role_id"     : 1324700619273142322,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Florent",
                "role_id"     : 1444769178652508222,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Rowan",
                "role_id"     : 1402453450809282660,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Caswell",
                "role_id"     : 1444663623594151976,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Roxton",
                "role_id"     : 1493308921648250950,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Cendregué",
                "role_id"     : 1444663625376727100,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Fossovoie",
                "role_id"     : 1444663626324770857,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Peake",
                "role_id"     : 1444663626324770857,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Ouest": {
        "color"         : 0xDC143C,
        "coat_emoji"    : "<:coat_lannister:1274485039488569494>",
        "role_region"   : 1267815975286210633,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Lannister",
                "role_id"     : 1267815975219363969,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Farman",
                "role_id"     : 1444768984946970824,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Reyne",
                "role_id"     : 1267815975219363968,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Marpheux",
                "role_id"     : 1310632719905984625,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Tarbeck",
                "role_id"     : 1444769070401589368,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Serret",
                "role_id"     : 1444767510204387344,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Fléaufort",
                "role_id"     : 1444767509516652584,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Brax",
                "role_id"     : 1308869276102299769,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Crakehall",
                "role_id"     : 1444767390091968612,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Kenning",
                "role_id"     : 1493308594567905434,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Lefford",
                "role_id"     : 1444767510871146607,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Nord": {
        "color"         : 0x808080,
        "coat_emoji"    : "<:coat_stark:1274485042348949604>",
        "role_region"   : 1267815975286210631,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Stark",
                "role_id"     : 1267815975236145243,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Bolton",
                "role_id"     : 1267815975236145242,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Omble",
                "role_id"     : 1412894967931601101,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Mormont",
                "role_id"     : 1281011238415110286,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Manderly",
                "role_id"     : 1281011399723847751,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Dustin",
                "role_id"     : 1444767886748025010,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Karstark",
                "role_id"     : 1342917488819699815,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Reed",
                "role_id"     : 1414530810652131348,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Glover",
                "role_id"     : 1444767989584105626,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Corbois",
                "role_id"     : 1444768250469552208,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Ryswell",
                "role_id"     : 1444768252696854719,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Conflans": {
        "color"         : 0x1A5276,
        "coat_emoji"    : "<:coat_tully:1274485046593458246>",
        "role_region"   : 1267815975286210636,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Tully",
                "role_id"     : 1267815975236145240,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Nerbosc",
                "role_id"     : 1267815975236145238,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Bracken",
                "role_id"     : 1316511073737769020,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Frey",
                "role_id"     : 1267815975236145239,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Mallister",
                "role_id"     : 1444768431311425556,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Vance d'Atranta",
                "role_id"     : 1409309856330154118,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Vance de Bel-Accueil",
                "role_id"     : 1444766878273900734,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Piper",
                "role_id"     : 1444766879167025253,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Lothson",
                "role_id"     : 1267815975236145237,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Mouton",
                "role_id"     : 1444766877774647296,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Darry",
                "role_id"     : 1493307914105127225,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },

    "Val": {
        "color"         : 0x2E86C1,
        "coat_emoji"    : "<:coat_arryn:1274485034820042855>",
        "role_region"   : 1267815975286210632,
        "role_suzerain" : 1267815975273631813,
        "role_banneret" : 1267815975273631812,
        "maisons"       : [
            {
                "nom"         : "Arryn",
                "role_id"     : 1267815975219363971,
                "type"        : "suzeraine",
                "max_membres" : 8,
            },
            {
                "nom"         : "Royce",
                "role_id"     : 1304513516580900915,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Grafton",
                "role_id"     : 1444768806063968266,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Rougefort",
                "role_id"     : 1346523705320411186,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Belmore",
                "role_id"     : 1343989950672011396,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Corbray",
                "role_id"     : 1357417620768559247,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Sunderland",
                "role_id"     : 1444767120503079012,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Templeton",
                "role_id"     : 1493308228195455076,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Veneur",
                "role_id"     : 1493308234776445129,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Vanbois",
                "role_id"     : 1444767121966895276,
                "type"        : "banneret",
                "max_membres" : 6,
            },
            {
                "nom"         : "Lynderly",
                "role_id"     : 1493014544807886909,
                "type"        : "banneret",
                "max_membres" : 6,
            },
        ]
    },
}


# ══════════════════════════════════════════════════════════════════════════════
# ── FONCTIONS UTILITAIRES ────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

def split_list(members: list, prefix: str = "•") -> list[str]:
    """Découpe une liste de membres en blocs compatibles avec les embeds Discord."""
    lines = [f"{prefix} {m.mention}" for m in members]
    chunks, current = [], ""
    for line in lines:
        if len(current) + len(line) + 1 > 1020:
            chunks.append(current)
            current = line
        else:
            current = f"{current}\n{line}" if current else line
    if current:
        chunks.append(current)
    return chunks if chunks else ["_Aucun_"]


def compter_maison(guild: discord.Guild, maison: dict, role_suzerain_id, role_banneret_id) -> dict:
    """Retourne les effectifs d'une maison."""
    role_maison = guild.get_role(maison["role_id"])
    if not role_maison:
        return {"nb_seigneur": 0, "nb_membres": 0, "nb_chef": 0}

    membres_maison = set(role_maison.members)

    if maison["type"] == "special":
        role_chef = guild.get_role(maison.get("chef_role_id", 0))
        ids_chefs = set(role_chef.members) if role_chef else set()
        return {
            "nb_chef"    : len(membres_maison & ids_chefs),
            "nb_membres" : len(membres_maison - ids_chefs),
        }

    if "role_seigneur_override" in maison:
        role_seigneur_id = maison["role_seigneur_override"]
    else:
        role_seigneur_id = role_suzerain_id if maison["type"] == "suzeraine" else role_banneret_id

    role_seigneur = guild.get_role(role_seigneur_id) if role_seigneur_id else None
    ids_seigneurs = set(role_seigneur.members) if role_seigneur else set()

    # Comptage des Dames (rôle global Lady, exclues des membres normaux)
    role_lady  = guild.get_role(ROLE_LADY_ID)
    ids_ladies = set(role_lady.members) if role_lady else set()
    nb_dames   = len(membres_maison & ids_ladies)

    # Membres normaux = ni seigneur, ni dame
    ids_speciaux = ids_seigneurs | ids_ladies

    return {
        "nb_seigneur" : len(membres_maison & ids_seigneurs),
        "nb_membres"  : len(membres_maison - ids_speciaux),
        "nb_dames"    : nb_dames,
    }


def extraire_statut(description: str, champ: str) -> str:
    """Lit le statut ouvert/fermé dans la description d'un embed."""
    for ligne in description.split("\n"):
        if champ.lower() in ligne.lower():
            if EMOJI_OUVERT in ligne:
                return EMOJI_OUVERT
            elif EMOJI_FERME in ligne:
                return EMOJI_FERME
    return EMOJI_FERME


def remplacer_statut(description: str, champ: str, nouvel_emoji: str) -> str:
    """Remplace le statut sur la ligne contenant le mot-clé 'champ'."""
    nouvelles_lignes = []
    for ligne in description.split("\n"):
        if champ.lower() in ligne.lower():
            ligne = ligne.rstrip()
            for emoji in [EMOJI_OUVERT, EMOJI_FERME]:
                ligne = ligne.replace(emoji, "")
            ligne = f"{ligne.rstrip()} {nouvel_emoji}"
        nouvelles_lignes.append(ligne)
    return "\n".join(nouvelles_lignes)


def construire_embed(
    region      : str,
    config      : dict,
    guild       : discord.Guild,
    ancien_embed: discord.Embed | None = None
) -> discord.Embed:
    """Construit l'embed stylisé d'une région avec les effectifs à jour."""

    desc_ancienne = ancien_embed.description if ancien_embed and ancien_embed.description else ""
    naissance   = extraire_statut(desc_ancienne, "Naissance")
    recrutement = extraire_statut(desc_ancienne, "Recrutement")
    candidature = extraire_statut(desc_ancienne, "Candidature")

    total_str = ""
    if config.get("role_region"):
        role_region = guild.get_role(config["role_region"])
        if role_region:
            total_str = f"👥 **Effectif total : {len(role_region.members)} membre(s)**\n\n"

    description = (
        f"{total_str}"
        f"• {EMOJI_NAISSANCE} Naissance : {naissance}\n"
        f"• {EMOJI_RECRUTEMENT} Recrutement : {recrutement}\n"
        f"• {EMOJI_CANDIDATURE} Candidature : {candidature}"
    )

    embed = discord.Embed(
        title       = f"{config['coat_emoji']}  {region}",
        description = description,
        color       = config["color"]
    )

    role_suzerain_id = config.get("role_suzerain")
    role_banneret_id = config.get("role_banneret")

    for maison in config["maisons"]:
        counts = compter_maison(guild, maison, role_suzerain_id, role_banneret_id)

        if maison["type"] == "special":
            value = (
                f"{maison['chef_label']} : **{counts['nb_chef']}/{maison['max_chef']}**\n"
                f"{maison['label']} : **{counts['nb_membres']}/{maison['max_membres']}**"
            )
        else:
            label = maison.get("seigneur_label", "Seigneur")
            dame_line = f"\nDame(s) : **{counts['nb_dames']}**" if counts.get("nb_dames", 0) > 0 else ""
            value = (
                f"{label} : **{counts['nb_seigneur']}/1**\n"
                f"Membres : **{counts['nb_membres']}/{maison['max_membres']}**"
                f"{dame_line}"
            )

        embed.add_field(
            name   = f"🏰 {maison['nom']}",
            value  = value,
            inline = True
        )

    embed.set_footer(text="Dernière mise à jour")
    embed.timestamp = discord.utils.utcnow()

    return embed


# ══════════════════════════════════════════════════════════════════════════════
# ── ÉVÉNEMENT : BOT PRÊT ─────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"✅ Connecté en tant que {bot.user} — {len(synced)} commande(s) synchronisée(s)")
    except Exception as e:
        print(f"❌ Erreur de synchronisation : {e}")


# ══════════════════════════════════════════════════════════════════════════════
# ── COMMANDES MEMBRES ────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@bot.tree.command(name="liste_role", description="Affiche tous les membres possédant un rôle donné.")
@app_commands.describe(role="Le rôle dont tu veux lister les membres")
async def liste_role(interaction: discord.Interaction, role: discord.Role):
    membres = sorted(role.members, key=lambda m: m.display_name.lower())
    if not membres:
        await interaction.response.send_message(f"⚠️ Aucun membre ne possède le rôle **{role.name}**.", ephemeral=False)
        return
    blocs = split_list(membres)
    embed = discord.Embed(
        title=f"📋 Membres avec le rôle « {role.name} »",
        color=role.color if role.color.value else discord.Color.blurple()
    )
    for i, bloc in enumerate(blocs):
        embed.add_field(name=f"Liste{' (suite)' if i > 0 else ''}", value=bloc, inline=False)
    embed.set_footer(text=f"Total : {len(membres)} membre(s)")
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="liste_reactions", description="Affiche tous les membres ayant réagi à un message donné.")
@app_commands.describe(
    salon="Le salon Discord contenant le message",
    message_id="L'identifiant (ID) du message"
)
async def liste_reactions(interaction: discord.Interaction, salon: discord.TextChannel, message_id: str):
    await interaction.response.defer()
    try:
        message = await salon.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable. Vérifie l'ID et le salon.", ephemeral=False)
        return
    except ValueError:
        await interaction.followup.send("❌ L'ID fourni n'est pas valide.", ephemeral=False)
        return
    if not message.reactions:
        await interaction.followup.send("⚠️ Ce message n'a reçu aucune réaction.", ephemeral=False)
        return
    reacteurs: set[discord.Member] = set()
    for reaction in message.reactions:
        async for user in reaction.users():
            if not user.bot and isinstance(user, discord.Member):
                reacteurs.add(user)
    if not reacteurs:
        await interaction.followup.send("⚠️ Aucun membre (hors bots) n'a réagi.", ephemeral=False)
        return
    membres_tries = sorted(reacteurs, key=lambda m: m.display_name.lower())
    blocs = split_list(membres_tries)
    embed = discord.Embed(title="💬 Membres ayant réagi au message", color=discord.Color.blue())
    for i, bloc in enumerate(blocs):
        embed.add_field(name=f"Liste{' (suite)' if i > 0 else ''}", value=bloc, inline=False)
    embed.set_footer(text=f"Total : {len(reacteurs)} membre(s)  |  Message dans #{salon.name}")
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="comparer", description="Compare les membres d'un rôle avec ceux ayant réagi à un message.")
@app_commands.describe(
    role="Le rôle à vérifier",
    salon="Le salon contenant le message de présence",
    message_id="L'ID du message de présence"
)
async def comparer(interaction: discord.Interaction, role: discord.Role, salon: discord.TextChannel, message_id: str):
    await interaction.response.defer()
    try:
        message = await salon.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable.", ephemeral=False)
        return
    except ValueError:
        await interaction.followup.send("❌ ID invalide.", ephemeral=False)
        return
    membres_role = set(role.members)
    ids_reacteurs: set[int] = set()
    for reaction in message.reactions:
        async for user in reaction.users():
            if not user.bot:
                ids_reacteurs.add(user.id)
    actifs   = sorted([m for m in membres_role if m.id in ids_reacteurs],     key=lambda m: m.display_name.lower())
    inactifs = sorted([m for m in membres_role if m.id not in ids_reacteurs], key=lambda m: m.display_name.lower())
    embed = discord.Embed(title=f"🔍 Comparaison — Rôle « {role.name} »", color=discord.Color.orange())
    embed.set_footer(text=f"Membres du rôle : {len(membres_role)}  |  Actifs : {len(actifs)}  |  Inactifs : {len(inactifs)}")
    for i, bloc in enumerate(split_list(actifs)):
        embed.add_field(name=f"✅ Actifs ({len(actifs)}){' — suite' if i > 0 else ''}", value=bloc, inline=False)
    for i, bloc in enumerate(split_list(inactifs)):
        embed.add_field(name=f"❌ Inactifs ({len(inactifs)}){' — suite' if i > 0 else ''}", value=bloc, inline=False)
    await interaction.followup.send(embed=embed)


# ══════════════════════════════════════════════════════════════════════════════
# ── COMMANDES FACTIONS ───────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

SALON_STATUT_FACTION_ID = 1332764322153369600

@bot.tree.command(name="poster_factions", description="Poste le message de statut d'une région pour la première fois.")
@app_commands.describe(
    region="Le nom de la région (ex: Terres de la Couronne)"
)
async def poster_factions(interaction: discord.Interaction, region: str):
    await interaction.response.defer(ephemeral=True)
    salon = interaction.guild.get_channel(SALON_STATUT_FACTION_ID)
    if not salon:
        await interaction.followup.send("❌ Salon Statut Faction introuvable.", ephemeral=True)
        return
    config_trouvee = None
    region_exacte  = None
    for nom, config in FACTIONS.items():
        if nom.lower() == region.strip().lower():
            config_trouvee = config
            region_exacte  = nom
            break
    if not config_trouvee:
        await interaction.followup.send(
            f"❌ Région introuvable. Disponibles : **{', '.join(FACTIONS.keys())}**", ephemeral=True
        )
        return
    embed         = construire_embed(region_exacte, config_trouvee, interaction.guild)
    message_poste = await salon.send(embed=embed)
    await interaction.followup.send(
        f"✅ Message posté dans {salon.mention} !\n"
        f"**ID du message : `{message_poste.id}`** — garde-le pour `/actualiser_factions` et `/statut_faction`.",
        ephemeral=True
    )


@bot.tree.command(name="actualiser_factions", description="Met à jour les effectifs du message de statut d'une région.")
@app_commands.describe(
    message_id="L'ID du message à mettre à jour"
)
async def actualiser_factions(interaction: discord.Interaction, message_id: str):
    await interaction.response.defer(ephemeral=True)
    salon = interaction.guild.get_channel(SALON_STATUT_FACTION_ID)
    if not salon:
        await interaction.followup.send("❌ Salon Statut Faction introuvable.", ephemeral=True)
        return
    try:
        message = await salon.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable.", ephemeral=True)
        return
    except ValueError:
        await interaction.followup.send("❌ ID invalide.", ephemeral=True)
        return
    if message.author.id != bot.user.id:
        await interaction.followup.send("❌ Ce message n'appartient pas au bot.", ephemeral=True)
        return
    if not message.embeds:
        await interaction.followup.send("❌ Ce message ne contient pas d'embed de faction.", ephemeral=True)
        return
    ancien_embed   = message.embeds[0]
    region_trouvee = None
    config_trouvee = None
    for region, config in FACTIONS.items():
        if region.lower() in (ancien_embed.title or "").lower():
            region_trouvee = region
            config_trouvee = config
            break
    if not region_trouvee:
        await interaction.followup.send("❌ Aucune région reconnue dans cet embed.", ephemeral=True)
        return
    nouvel_embed = construire_embed(region_trouvee, config_trouvee, interaction.guild, ancien_embed)
    await message.edit(embed=nouvel_embed)
    await interaction.followup.send(
        f"✅ Effectifs de **{region_trouvee}** mis à jour !", ephemeral=True
    )


@bot.tree.command(name="statut_faction", description="Change le statut Naissance, Recrutement ou Candidature d'une région.")
@app_commands.describe(
    message_id="L'ID du message à modifier",
    naissance="Statut des naissances",
    recrutement="Statut du recrutement",
    candidature="Statut des candidatures"
)
@app_commands.choices(
    naissance=[
        app_commands.Choice(name="✅ Ouvert", value="ouvert"),
        app_commands.Choice(name="❌ Fermé",  value="ferme"),
    ],
    recrutement=[
        app_commands.Choice(name="✅ Ouvert", value="ouvert"),
        app_commands.Choice(name="❌ Fermé",  value="ferme"),
    ],
    candidature=[
        app_commands.Choice(name="✅ Ouvert", value="ouvert"),
        app_commands.Choice(name="❌ Fermé",  value="ferme"),
    ]
)
async def statut_faction(
    interaction : discord.Interaction,
    message_id  : str,
    naissance   : app_commands.Choice[str] | None = None,
    recrutement : app_commands.Choice[str] | None = None,
    candidature : app_commands.Choice[str] | None = None,
):
    await interaction.response.defer(ephemeral=True)
    salon = interaction.guild.get_channel(SALON_STATUT_FACTION_ID)
    if not salon:
        await interaction.followup.send("❌ Salon Statut Faction introuvable.", ephemeral=True)
        return
    try:
        message = await salon.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable.", ephemeral=True)
        return
    except ValueError:
        await interaction.followup.send("❌ ID invalide.", ephemeral=True)
        return
    if message.author.id != bot.user.id:
        await interaction.followup.send("❌ Ce message n'appartient pas au bot.", ephemeral=True)
        return
    if not message.embeds:
        await interaction.followup.send("❌ Ce message ne contient pas d'embed de faction.", ephemeral=True)
        return

    def emoji_from_choice(choice):
        return EMOJI_OUVERT if choice.value == "ouvert" else EMOJI_FERME

    embed = message.embeds[0]
    desc  = embed.description or ""
    if naissance:
        desc = remplacer_statut(desc, "Naissance",   emoji_from_choice(naissance))
    if recrutement:
        desc = remplacer_statut(desc, "Recrutement", emoji_from_choice(recrutement))
    if candidature:
        desc = remplacer_statut(desc, "Candidature", emoji_from_choice(candidature))

    embed_modifie = discord.Embed(title=embed.title, description=desc, color=embed.color)
    for field in embed.fields:
        embed_modifie.add_field(name=field.name, value=field.value, inline=field.inline)
    embed_modifie.set_footer(text="Dernière mise à jour")
    embed_modifie.timestamp = discord.utils.utcnow()

    await message.edit(embed=embed_modifie)
    await interaction.followup.send("✅ Statut(s) mis à jour !", ephemeral=True)


# ══════════════════════════════════════════════════════════════════════════════
# ── COMMANDE CANDIDATS NAISSANCE ─────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

import re

CANAL_NAISSANCE_ID = 1455917148374306876

def _extraire_nom_personnage(message: discord.Message) -> str:
    """Extrait le nom du personnage depuis la ligne ## du message d'annonce."""
    contenu = message.content or ""
    for ligne in contenu.split("\n"):
        if ligne.strip().startswith("##"):
            # Supprime le ## et les emojis Discord <:nom:id>
            nom = re.sub(r"<:[^:]+:\d+>", "", ligne)
            nom = nom.replace("##", "").strip()
            return nom if nom else "Personnage inconnu"
    return "Personnage inconnu"

@bot.tree.command(
    name        = "candidats_naissance",
    description = "Affiche les candidats ayant réagi au message d'annonce d'une naissance."
)
@app_commands.describe(
    message_id = "L'ID du message d'annonce de naissance"
)
async def candidats_naissance(interaction: discord.Interaction, message_id: str):
    await interaction.response.defer(ephemeral=False)

    # ── Récupère le salon et le message ──────────────────────────────────────
    canal = interaction.guild.get_channel(CANAL_NAISSANCE_ID)
    if not canal:
        await interaction.followup.send("❌ Salon des naissances introuvable.", ephemeral=False)
        return

    try:
        message = await canal.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable dans le salon des naissances.", ephemeral=False)
        return
    except ValueError:
        await interaction.followup.send("❌ ID de message invalide.", ephemeral=False)
        return

    # ── Récupère les réactions ────────────────────────────────────────────────
    if not message.reactions:
        await interaction.followup.send("⚠️ Aucune réaction sur ce message.", ephemeral=False)
        return

    # Collecte d'abord tous les user IDs ayant réagi
    raw_users: dict[int, discord.User] = {}
    for reaction in message.reactions:
        async for user in reaction.users():
            if not user.bot:
                raw_users[user.id] = user

    # Fetch groupé : une seule requête par batch de 100 au lieu de N requêtes
    candidats: dict[int, discord.Member | discord.User] = {}
    ids = list(raw_users.keys())
    for i in range(0, len(ids), 100):
        batch = ids[i:i+100]
        try:
            members = await interaction.guild.query_members(user_ids=batch, cache=True)
            for m in members:
                candidats[m.id] = m
        except Exception:
            pass
    # Fallback pour les membres non trouvés (ont quitté le serveur)
    for uid, user in raw_users.items():
        if uid not in candidats:
            candidats[uid] = user

    if not candidats:
        await interaction.followup.send("⚠️ Aucun candidat trouvé.", ephemeral=False)
        return

    membres_tries = sorted(
        candidats.values(),
        key=lambda m: (m.display_name if hasattr(m, "display_name") else m.name).lower()
    )

    # ── Construit l'embed principal ───────────────────────────────────────────
    titre_personnage = _extraire_nom_personnage(message)

    embed = discord.Embed(
        title       = f"{EMOJI_NAISSANCE} Candidats — {titre_personnage}",
        description = (
            f"**{len(membres_tries)} candidat(s)** pour ce personnage.\n"
            f"[Voir le message d'annonce]({message.jump_url})"
        ),
        color       = discord.Color.gold(),
    )

    # ── Liste des candidats avec mentions ─────────────────────────────────────
    # Formate chaque mention explicitement — évite les <@id> non résolus
    lines = [f"• {m.mention}" for m in membres_tries]

    # Découpe en blocs de 1024 caractères max (limite Discord)
    blocs, bloc_actuel = [], ""
    for line in lines:
        if len(bloc_actuel) + len(line) + 1 > 1024:
            blocs.append(bloc_actuel.strip())
            bloc_actuel = ""
        bloc_actuel += line + "\n"
    if bloc_actuel:
        blocs.append(bloc_actuel.strip())

    for i, bloc in enumerate(blocs):
        embed.add_field(
            name   = f"Candidat(s){' (suite)' if i > 0 else ''}",
            value  = bloc,
            inline = False,
        )

    embed.set_footer(text=f"Commande utilisée par {interaction.user.display_name}")
    embed.timestamp = discord.utils.utcnow()

    await interaction.followup.send(embed=embed, ephemeral=False)


# ══════════════════════════════════════════════════════════════════════════════
# ── COMMANDE PRÉSENCE GUERRE ──────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════

@bot.tree.command(
    name        = "presence_guerre",
    description = "Affiche la liste des joueurs ayant confirmé leur présence pour la bataille."
)
@app_commands.describe(
    message_id = "L'ID du message d'annonce de bataille",
    faction    = "Nom de la faction (affiché dans le titre)",
)
async def presence_guerre(
    interaction : discord.Interaction,
    message_id  : str,
    faction     : str,
):
    await interaction.response.defer()

    canal = interaction.channel
    try:
        message = await canal.fetch_message(int(message_id))
    except discord.NotFound:
        await interaction.followup.send("❌ Message introuvable dans ce salon.")
        return
    except ValueError:
        await interaction.followup.send("❌ ID de message invalide.")
        return

    presents: dict[int, discord.Member] = {}
    for reaction in message.reactions:
        async for user in reaction.users():
            if user.bot or user.id in presents:
                continue
            try:
                member = await interaction.guild.fetch_member(user.id)
                presents[user.id] = member
            except (discord.NotFound, discord.HTTPException):
                presents[user.id] = user

    membres_tries = sorted(
        presents.values(),
        key=lambda m: (m.display_name if hasattr(m, "display_name") else m.name).lower()
    )

    heure_annonce = discord.utils.format_dt(message.created_at, style="F")
    total  = len(membres_tries)
    couleur = discord.Color.gold()

    embed = discord.Embed(
        title       = f"⚔️ Présences — {faction}",
        description = f"[Message d'annonce]({message.jump_url})\n📅 Envoyé le {heure_annonce}",
        color       = couleur,
    )

    if membres_tries:
        lines, bloc_actuel, blocs = [f"• {m.mention}" for m in membres_tries], "", []
        for line in lines:
            if len(bloc_actuel) + len(line) + 1 > 1024:
                blocs.append(bloc_actuel.strip())
                bloc_actuel = ""
            bloc_actuel += line + "\n"
        if bloc_actuel:
            blocs.append(bloc_actuel.strip())
        for i, bloc in enumerate(blocs):
            embed.add_field(name=f"Joueurs présents{' (suite)' if i > 0 else ''}", value=bloc, inline=False)
    else:
        embed.add_field(name="Joueurs présents", value="*Aucune réaction pour le moment.*", inline=False)

    embed.set_footer(text=f"Total : {total} joueur(s)")
    embed.timestamp = discord.utils.utcnow()

    await interaction.followup.send(embed=embed)


# ── Lancement du bot ─────────────────────────────────────────────────────────
bot.run(TOKEN)
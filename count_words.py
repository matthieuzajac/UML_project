#!/usr/bin/env python3
import re

# Read the LaTeX file
with open('/home/engine/project/rapport_uml.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by lines
lines = content.split('\n')

# Define sections to exclude
# Title page: lines 29-78 (titlepage environment)
# Table of contents: line 84
# Section titles (lines starting with \section, \subsection, \subsubsection)

excluded_ranges = [(29, 78), (84, 84)]  # Line numbers (1-based, inclusive)

# Track sections and their word counts
current_section = "Introduction"
section_words = {}
total_words = 0
in_titlepage = False
in_title = False

# Pattern to detect section commands
section_pattern = re.compile(r'\\(sub)?section\*?\{(.+?)\}')
figure_pattern = re.compile(r'\\begin\{figure\}.*?\\end\{figure\}', re.DOTALL)
caption_pattern = re.compile(r'\\caption\{(.+?)\}')

# Remove figure environments entirely (we only want the explanations)
content_no_figures = re.sub(figure_pattern, '', content)

# Extract and process text, keeping line info
lines = content_no_figures.split('\n')

for i, line in enumerate(lines, 1):
    line_num = i

    # Skip title page
    if 29 <= line_num <= 78:
        continue

    # Skip table of contents line
    if line_num == 84:
        continue

    # Check for section title
    section_match = section_pattern.search(line)
    if section_match:
        current_section = section_match.group(2)
        section_words[current_section] = 0
        in_title = True
        continue

    # Remove LaTeX commands but keep content
    # Remove \textbf{}, \texttt{}, \textit{}, etc.
    line = re.sub(r'\\textbf\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\texttt\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\textit\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\textsc\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\emph\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\large\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\LARGE\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\huge\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\bfseries\{([^}]*)\}', r'\1', line)
    line = re.sub(r'\\sffamily', '', line)
    line = re.sub(r'\\centering', '', line)
    line = re.sub(r'\\flush(left|right)', '', line)
    line = re.sub(r'\[.*?cm\]', '', line)  # Remove spacing commands like [1.5cm]

    # Remove other LaTeX commands
    line = re.sub(r'\\[a-zA-Z]+\*?(\[.*?\])?\{[^}]*\}', '', line)
    line = re.sub(r'\\[a-zA-Z]+\*?', '', line)

    # Remove special characters
    line = re.sub(r'[_$^%~&{}#]', ' ', line)
    line = re.sub(r'\\', ' ', line)

    # Split into words (French and English words)
    words = re.findall(r"[a-zA-ZÀ-ÿ0-9\-']+", line)

    # Count words
    word_count = len(words)
    total_words += word_count

    if current_section in section_words:
        section_words[current_section] += word_count
    else:
        section_words[current_section] = word_count

print("=" * 80)
print(f"TOTAL WORDS (excluding title page, TOC, section titles): {total_words}")
print(f"Limit: 1500 words")
print(f"Status: {'✓ PASS' if total_words < 1500 else '✗ FAIL'}")
print("=" * 80)

# Diagram explanations - identify them by context
print("\n" + "=" * 80)
print("DIAGRAM EXPLANATIONS (should be < 200 words each):")
print("=" * 80)

diagram_explanations = {
    "Cas d'Utilisation": "Ce diagramme définit les frontières du système et identifie quatre acteurs principaux organisés par héritage : \\texttt{Guest}, \\texttt{Authenticated\\_User}, \\texttt{Reader}, \\texttt{Author}, et \\texttt{Moderator}. L'héritage reflète l'accumulation de droits : un auteur hérite des capacités d'un lecteur (lecture, critiques), qui hérite lui-même d'un utilisateur authentifié (profil, notifications).\n\nLes cas d'utilisation sont regroupés en cinq packages fonctionnels : accès invité (exploration, recherche, lecture publique, inscription), gestion de compte (authentification, profil, notifications, signalement), fonctionnalités lecteur (bibliothèque, abonnements, progression, critiques), fonctionnalités auteur (création de roman, publication de chapitres, analyse de statistiques), et outils de modération (modération de contenu, gestion des utilisateurs, traitement des signalements). Les relations \\texttt{<<include>>} structurent les cas d'utilisation composites tandis que \\texttt{<<extend>>} modélise les extensions optionnelles comme le signalement de contenu.",
    "Classes": "Le diagramme de classes constitue le coeur du modèle. La classe abstraite \\texttt{Authenticated\\_user} centralise l'authentification et la gestion de profil, avec des attributs protégés (\\texttt{id}, \\texttt{username}, \\texttt{email}, \\texttt{password\\_hash}) et des indicateurs de modération (\\texttt{is\\_banned}, \\texttt{is\\_shadowbanned}).\n\n\\textbf{Choix de conception majeur :} l'héritage \\texttt{Authenticated\\_user $\\leftarrow$ Reader $\\leftarrow$ Author} reflète le fait qu'un auteur est toujours un lecteur (peut lire et commenter d'autres œuvres), mais un lecteur n'est pas nécessairement auteur. \\texttt{Moderator} hérite directement de \\texttt{Authenticated\\_user} car il possède des privilèges distincts.\n\nLes entités centrales \\texttt{Novel} et \\texttt{Chapter} sont liées par composition (diamant noir) : la suppression d'un roman entraîne celle de tous ses chapitres. \\texttt{Review} utilise l'agrégation (diamant blanc) car elle dépend du lecteur et du roman mais possède un cycle de vie partiellement indépendant.\n\nQuatre énumérations encapsulent les états critiques : \\texttt{NovelStatus} (DRAFT, ACTIVE, HIATUS, COMPLETED, SHADOWBANNED, DELETED), \\texttt{NotificationType}, \\texttt{ReadingStatus}, et \\texttt{ReportStatus}, assurant la cohérence et la validation des transitions d'états.",
    "Composants": "Le diagramme de composants illustre l'architecture technique en couches avec dépendances explicites. La couche frontend (Web UI, Mobile App) communique via une API Gateway (REST API, WebSocket Server) avec neuf services applicatifs spécialisés : Authentication, User, Novel, Chapter, Review, Notification, Search, Moderation, et Analytics.\n\nCes services s'appuient sur des composants de logique métier (User Management, Content Management, Library Management, etc.) qui utilisent les services d'infrastructure (Email Service, File Storage, Cache Service, Anti-Spam Filter, Search Engine).\n\n\\textbf{Choix architectural :} la séparation en microservices facilite la scalabilité horizontale et l'isolation des pannes. L'anti-spam est intégré au niveau infrastructure pour protéger tous les points d'entrée. Le cache (Redis) et l'index de recherche (Elasticsearch) sont découplés de la base relationnelle principale pour optimiser les performances.",
    "Déploiement": "Le diagramme de déploiement illustre la distribution physique des composants sur l'infrastructure serveur et les protocoles de communication sécurisés utilisés entre les nœuds.\n\n\\textbf{Analyse de l'infrastructure :}\n\\begin{itemize}\n    \\item \\textbf{Communication Client-Serveur :} Les échanges sont sécurisés via \\texttt{HTTPS} pour les requêtes REST et \\texttt{WSS} (WebSocket Secure) pour les mises à jour en temps réel (notifications, chats).\n    \\item \\textbf{Passerelle Applicative :} L'API Gateway fait office de point d'entrée unique, gérant l'authentification et le \\textit{rate limiting} avant de rediriger le trafic vers les services de logique métier.\n    \\item \\textbf{Traitement Asynchrone :} Le système sépare les requêtes utilisateur immédiates des tâches lourdes (envoi d'emails, calculs statistiques, traitement d'images) via des \\texttt{Background Workers} et des files d'attente de jobs (\\textit{Queue jobs}).\n    \\item \\textbf{Stratégie de Stockage Hybride :} \n    \\begin{itemize}\n        \\item \\textbf{Cache Layer :} Utilisation d'une base en mémoire (type Redis) pour les sessions et les données fréquemment accédées (Popular Content).\n        \\item \\textbf{Search Index :} Un moteur dédié (type Elasticsearch) gère les recherches textuelles complexes et l'indexation des romans.\n        \\item \\textbf{Object Storage :} Les fichiers volumineux (avatars, couvertures) sont isolés sur un stockage objet pour ne pas saturer la base de données relationnelle principale.\n    \\end{itemize}\n\\end{itemize}",
    "Objet": "Ce diagramme présente une instance concrète du système à un instant donné, illustrant un auteur (alice\\_writer) qui a créé un roman fantasy (myNovel:Novel) avec trois chapitres, tandis qu'un lecteur (bob\\_reader) a ajouté ce roman à sa bibliothèque, s'y est abonné, et a publié une critique 5 étoiles. Cette vue complète l'abstraction du diagramme de classes en montrant des valeurs réelles et l'état runtime des objets.",
    "États": "Ce diagramme modélise le cycle de vie complet d'un roman à travers sept états principaux. Un roman naît en état \\texttt{Draft} (invisible, éditable librement), passe à \\texttt{Active} lors de la publication du premier chapitre (visible dans les recherches, notifications activées), peut être mis en \\texttt{Hiatus} (pause temporaire, visible mais inactif), ou marqué \\texttt{Completed} (terminé, archivé).\n\n\\textbf{Transitions de modération :} les modérateurs peuvent appliquer \\texttt{Shadowbanned} (masqué des recherches publiques mais accessible par lien direct) en cas de violation mineure, ou \\texttt{Deleted} pour suppression définitive. Des transitions de restauration existent depuis \\texttt{Shadowbanned} vers les états précédents après révision.\n\n\\textbf{Choix de conception :} l'état \\texttt{Shadowbanned} distinct de \\texttt{Deleted} permet une modération progressive sans perte irréversible de contenu, facilitant la résolution de conflits et les appels.",
    "Activité - Lecture": "Ce workflow modélise le parcours complet d'un utilisateur depuis la recherche d'un roman jusqu'aux interactions post-lecture. Après consultation du synopsis, l'utilisateur lit les chapitres séquentiellement avec mise à jour automatique de sa progression. Les interactions (ajout à la bibliothèque avec activation des notifications, publication de critiques avec recalcul de moyenne) sont conditionnées à l'authentification, avec proposition d'inscription sinon.",
    "Activité - Écriture": "Ce diagramme détaillé couvre cinq partitions : gestion du roman (création avec métadonnées, sélection de genres/tags, initialisation en DRAFT), rédaction de chapitre (édition parallèle du titre, vérification du nombre de mots, prévisualisation), publication (vérification anti-spam, passage en ACTIVE pour le premier chapitre, notifications aux abonnés), suivi analytique (vues, notes, abonnés, reviews), et gestion du statut (transitions vers HIATUS ou COMPLETED).\n\nLa vérification anti-spam intervient avant publication pour bloquer le contenu problématique sans impacter les statistiques du roman ni spammer les abonnés.",
    "Activité - Recherche": "Workflow de recherche avec filtrage multi-critères (genre, tags, statut, note minimale), tri des résultats par pertinence ou popularité, et sauvegarde optionnelle des critères de recherche pour les utilisateurs authentifiés.",
    "Séquence - Publication": "Séquence détaillée montrant l'interaction entre l'auteur, l'UI, l'objet Novel, la création dynamique d'un objet Chapter, la persistance en base, le recalcul de la note moyenne du roman, et la notification asynchrone des followers via le système de notifications qui interroge la base pour récupérer la liste des abonnés.",
    "Séquence - Review": "Workflow montrant qu'un lecteur peut critiquer d'autres romans (héritage Reader $\\leftarrow$ Author). La séquence crée un objet Review, le sauvegarde, puis déclenche le recalcul de la moyenne du roman par agrégation (totalStars / reviewCount) avec mise à jour en base de donnée et affichage immédiat.",
    "Séquence - Authentification": "Processus complet d'inscription (validation email, hachage du mot de passe, envoi email de vérification) et de connexion (vérification logins, création de session, génération de token).",
    "Séquence - Bibliothèque": "Ajout d'un roman à la bibliothèque personnelle du lecteur avec création d'une entrée Library, initialisation de la progression de lecture, et activation optionnelle des notifications de mise à jour.",
    "Séquence - Modération": "Séquence montrant un modérateur récupérant la liste des signalements puis supprimant ou réalisant un shadowban sur un roman problématique avec suppression ou mise à jour de la base de donnée et notification de l'action à l'auteur du roman.",
}

for diag_name, diag_text in diagram_explanations.items():
    # Clean LaTeX from text
    text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', diag_text)
    text = re.sub(r'\\texttt\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textit\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\emph\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textsc\{([^}]*)\}', r'\1', text)
    text = re.sub(r'\\textit', '', text)
    text = re.sub(r'\\[a-zA-Z]+\*?(\[.*?\])?\{[^}]*\}', '', text)
    text = re.sub(r'\\[a-zA-Z]+\*', '', text)
    text = re.sub(r'\\[a-zA-Z]+', '', text)
    text = re.sub(r'[_$^%~&{}#\\]', ' ', text)
    text = re.sub(r'\$\\leftarrow\$', '←', text)
    text = re.sub(r'\$.*?\$', '', text)
    text = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\item', '', text)

    words = re.findall(r"[a-zA-ZÀ-ÿ0-9\-']+", text)
    word_count = len(words)
    status = '✓ PASS' if word_count < 200 else '✗ FAIL'
    print(f"{diag_name:40s} : {word_count:3d} words {status}")

print("\n" + "=" * 80)

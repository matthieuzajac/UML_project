#!/usr/bin/env python3

# Read the file and count words manually
with open('/home/engine/project/rapport_uml.tex', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Define text sections to count (excluding title page and TOC)
# Lines after title page (ends line 78) and TOC (line 84)

print("=" * 80)
print("MANUAL WORD COUNT ANALYSIS")
print("=" * 80)

# Key explanation sections with their line ranges (from the file I read)
explanations = {
    "Cas d'Utilisation": (117, 120),
    "Classes": (130, 137),
    "Composants": (148, 153),
    "Déploiement": (163, 177),
    "Objet": (187, 188),
    "États": (200, 205),
    "Activité - Lecture": (217, 218),
    "Activité - Écriture": (228, 231),
    "Activité - Recherche": (241, 242),
    "Séquence - Publication": (254, 255),
    "Séquence - Review": (265, 266),
    "Séquence - Authentification": (276, 277),
    "Séquence - Bibliothèque": (287, 288),
    "Séquence - Modération": (298, 299),
}

# Count words in each explanation
total_explanation_words = 0
print("\nDIAGRAM EXPLANATIONS:")
for name, (start, end) in explanations.items():
    text = ''.join(lines[start-1:end])  # Convert to 0-based
    # Remove LaTeX commands
    import re
    text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', text)
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
    text = re.sub(r'\[.*?cm\]', '', text)

    words = re.findall(r"[a-zA-ZÀ-ÿ0-9\-']+", text)
    count = len(words)
    total_explanation_words += count
    status = '✓ PASS' if count < 200 else '✗ FAIL'
    print(f"  {name:40s} : {count:3d} words {status}")

print(f"\n  {'TOTAL EXPLANATIONS':40s} : {total_explanation_words:3d} words")

# Count all content (excluding title page, TOC, and section headers)
all_content = []
skip_ranges = [(1, 86)]  # Title page and TOC

for i, line in enumerate(lines, 1):
    # Skip title page and TOC
    if i <= 86:
        continue

    # Skip section/subsection headers
    if line.strip().startswith('\\section') or line.strip().startswith('\\subsection') or line.strip().startswith('\\subsubsection'):
        continue

    # Skip figure environments and captions
    if '\\begin{figure}' in line or '\\end{figure}' in line or '\\caption' in line:
        continue
    if line.strip().startswith('\\includegraphics'):
        continue
    if line.strip().startswith('\\label'):
        continue

    all_content.append(line)

full_text = ''.join(all_content)

import re
full_text = re.sub(r'\\textbf\{([^}]*)\}', r'\1', full_text)
full_text = re.sub(r'\\texttt\{([^}]*)\}', r'\1', full_text)
full_text = re.sub(r'\\textit\{([^}]*)\}', r'\1', full_text)
full_text = re.sub(r'\\emph\{([^}]*)\}', r'\1', full_text)
full_text = re.sub(r'\\textsc\{([^}]*)\}', r'\1', full_text)
full_text = re.sub(r'\\textit', '', full_text)
full_text = re.sub(r'\\[a-zA-Z]+\*?(\[.*?\])?\{[^}]*\}', '', full_text)
full_text = re.sub(r'\\[a-zA-Z]+\*', '', full_text)
full_text = re.sub(r'\\[a-zA-Z]+', '', full_text)
full_text = re.sub(r'[_$^%~&{}#\\]', ' ', full_text)
full_text = re.sub(r'\$.*?\$', '', full_text)
full_text = re.sub(r'\[.*?cm\]', '', full_text)
full_text = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', '', full_text, flags=re.DOTALL)
full_text = re.sub(r'\\item', '', full_text)
full_text = re.sub(r'\\begin\{minipage\}.*?\\end\{minipage\}', '', full_text, flags=re.DOTALL)
full_text = re.sub(r'\\begin\{center\}.*?\\end\{center\}', '', full_text, flags=re.DOTALL)
full_text = re.sub(r'\\begin\{[a-z]+\}.*?\\end\{[a-z]+\}', '', full_text, flags=re.DOTALL)

all_words = re.findall(r"[a-zA-ZÀ-ÿ0-9\-']+", full_text)
total_all_words = len(all_words)

print("\n" + "=" * 80)
print(f"TOTAL WORDS (excluding title page, TOC, section titles, figures): {total_all_words}")
print(f"Limit: 1500 words")
print(f"Status: {'✓ PASS' if total_all_words < 1500 else '✗ FAIL'}")
print("=" * 80)

print(f"\nPer-diagram limit check: All < 200 words? {'✓ PASS' if all(len(re.findall(r'[a-zA-ZÀ-ÿ0-9\\-\']+', ''.join(lines[start-1:end]))) < 200 for _, (start, end) in explanations.items()) else '✗ FAIL'}")

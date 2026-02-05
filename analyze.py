#!/usr/bin/env python3

# Read and analyze word count directly
with open('/home/engine/project/rapport_uml.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract main text content (remove title page, TOC, figures, section headers)
import re

# Remove title page
content = re.sub(r'\\begin\{titlepage\}.*?\\end\{titlepage\}', '', content, flags=re.DOTALL)
# Remove TOC
content = re.sub(r'\\tableofcontents', '', content)
# Remove figure environments
content = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', '', content, flags=re.DOTALL)
# Remove section headers
content = re.sub(r'\\(sub)?section\*?\{[^}]*\}', '', content)

# Clean LaTeX commands
content = re.sub(r'\\textbf\{([^}]*)\}', r'\1', content)
content = re.sub(r'\\texttt\{([^}]*)\}', r'\1', content)
content = re.sub(r'\\textit\{([^}]*)\}', r'\1', content)
content = re.sub(r'\\emph\{([^}]*)\}', r'\1', content)
content = re.sub(r'\\textsc\{([^}]*)\}', r'\1', content)
content = re.sub(r'\\[a-zA-Z]+\*?(\[.*?\])?\{[^}]*\}', '', content)
content = re.sub(r'\\[a-zA-Z]+\*', '', content)
content = re.sub(r'\\[a-zA-Z]+', '', content)
content = re.sub(r'[_$^%~&{}#\\]', ' ', content)
content = re.sub(r'\$.*?\$', '', content)
content = re.sub(r'\[.*?cm\]', '', content)
content = re.sub(r'\\begin\{itemize\}.*?\\end\{itemize\}', '', content, flags=re.DOTALL)
content = re.sub(r'\\item', '', content)

# Count words
words = re.findall(r"[a-zA-ZÀ-ÿ0-9\-']+", content)
print(f"Total words (excluding title page, TOC, section titles, figures): {len(words)}")
print(f"Limit: 1500 words")
print(f"Result: {'PASS ✓' if len(words) < 1500 else 'FAIL ✗'}")

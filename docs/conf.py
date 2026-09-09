# Configuration file for Sphinx
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "PNCP em Números"
author = "COTIN/DELOG — Ministério da Gestão e da Inovação em Serviços Públicos"
copyright = "2026, COTIN/DELOG/MGI"
release = "1.0"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "pt_BR"

# ── Tema Furo ────────────────────────────────────────────────────────────────
html_theme = "furo"

html_title = "PNCP em Números"
html_short_title = "PNCP em Números"

html_static_path = ["_static"]
html_css_files = ["css/custom.css"]

html_theme_options = {
    "light_logo": "images/logo-pncp.png",   # opcional – se quiser adicionar logo
    "dark_logo": "images/logo-pncp.png",
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "light_css_variables": {
        # Paleta principal — azul PNCP/governo
        "color-brand-primary": "#1351B4",
        "color-brand-content": "#1351B4",
        "color-brand-visited": "#0D3B8E",
        # Fundo e superfícies
        "color-background-primary": "#FFFFFF",
        "color-background-secondary": "#F0F4FB",
        "color-background-hover": "#E0EBFF",
        "color-background-border": "#C5D4EB",
        # Código
        "color-code-background": "#F0F4FB",
        "color-code-foreground": "#1B1B1B",
        # Tipografia
        "font-stack": "Inter, system-ui, -apple-system, sans-serif",
        "font-stack--monospace": "JetBrains Mono, Fira Code, monospace",
    },
    "dark_css_variables": {
        # Paleta escura
        "color-brand-primary": "#5B9BD5",
        "color-brand-content": "#5B9BD5",
        "color-brand-visited": "#8AB4E8",
        # Fundo e superfícies
        "color-background-primary": "#0F1117",
        "color-background-secondary": "#1A1F2E",
        "color-background-hover": "#1E2A42",
        "color-background-border": "#2D3A52",
        # Código
        "color-code-background": "#1A1F2E",
        "color-code-foreground": "#E2E8F0",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/pablio-sousadev/manual-pncp-em-numeros",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0"
                    viewBox="0 0 16 16" height="1em" width="1em"
                    xmlns="http://www.w3.org/2000/svg">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38
                    0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13
                    -.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66
                    .07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15
                    -.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27
                    .68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12
                    .51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48
                    0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
            """,
            "class": "",
        },
    ],
    "announcement": None,
}

# MyST Parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "html_image",
]
myst_heading_anchors = 3

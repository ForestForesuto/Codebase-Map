"""Contains constant-related items."""

gitignore_patterns = [
    # 1. Operating System junk (macOS / Windows / Linux)
    '.DS_Store',
    'Thumbs.db',

    # 2. Dependency directories (JS, Python, PHP, etc.)
    'node_modules/',
    '.venv/',
    'venv/',
    'vendor/',

    # 3. Python cache files (if you use Python)
    '__pycache__/',
    '*.pyc',

    # 4. Logs, databases, and temporary files
    '*.log',
    '*.db',
    '*.sqlite3',
    '*.tmp',
    '*.cache',

    # 5. Environment variables & secrets (NEVER commit these!)
    '.env',
    '.env.local',
    '.env.*.local',   # wildcard pattern

    # 6. Build output folders (compiled code)
    'dist/',
    'build/',

    # 7. Editor configs (VSCode, IntelliJ, Vim)
    '.vscode/',
    '.idea/',
    '*.swp',
    '*.swo',

    # 8. Github items
    '.git/'
]

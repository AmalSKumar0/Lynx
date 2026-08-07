from pathlib import Path
import os
import pathspec

LANGUAGE_EXTENSIONS = {
    "python": [".py", ".pyw"],
    "javascript": [".js", ".mjs", ".cjs", ".jsx"],
    "typescript": [".ts", ".tsx", ".mts", ".cts"],
    "php": [".php", ".phtml"],
    "java": [".java"],
    "kotlin": [".kt", ".kts"],
    "scala": [".scala"],
    "groovy": [".groovy"],
    "c": [".c", ".h"],
    "c++": [".cpp", ".cc", ".cxx", ".hpp", ".hh", ".hxx"],
    "c#": [".cs"],
    "go": [".go"],
    "rust": [".rs"],
    "swift": [".swift"],
    "dart": [".dart"],
    "ruby": [".rb"],
    "perl": [".pl", ".pm"],
    "r": [".r"],
    "lua": [".lua"],
    "shell": [".sh", ".bash", ".zsh"],
    "powershell": [".ps1"],
    "objective-c": [".m", ".mm"],
    "objective-c++": [".mm"],
    "elixir": [".ex", ".exs"],
    "erlang": [".erl", ".hrl"],
    "haskell": [".hs"],
    "ocaml": [".ml", ".mli"],
    "f#": [".fs", ".fsi", ".fsx"],
    "clojure": [".clj", ".cljs", ".cljc"],
    "nim": [".nim"],
    "zig": [".zig"],
    "julia": [".jl"],
    "fortran": [".f", ".f90", ".f95"],
    "matlab": [".m"],
    "sql": [".sql"],
    "html": [".html", ".htm"],
    "css": [".css"],
    "scss": [".scss"],
    "sass": [".sass"],
    "less": [".less"],
    "vue": [".vue"],
    "svelte": [".svelte"],
    "xml": [".xml"],
    "yaml": [".yaml", ".yml"],
    "json": [".json"],
    "toml": [".toml"],
    "ini": [".ini"],
    "markdown": [".md", ".markdown"],
    "dockerfile": ["Dockerfile"],
    "makefile": ["Makefile"],
    "terraform": [".tf", ".tfvars"],
    "protobuf": [".proto"],
    "graphql": [".graphql", ".gql"],
}

EXTENSION_TO_LANGUAGE = {
    ext: language
    for language, extensions in LANGUAGE_EXTENSIONS.items()
    for ext in extensions
}

EXTENSION_TO_FRAMEWORK = {
    # Python
    "manage.py": "django",
    "wsgi.py": "django",
    "asgi.py": "django",
    "settings.py": "django",
    "urls.py": "django",
    "apps.py": "django",
    "models.py": "django",
    "views.py": "django",
    "admin.py": "django",
    "serializers.py": "django_rest_framework",
    "routers.py": "django_rest_framework",

    "main.py": "fastapi",
    "app.py": "fastapi",
    "requirements.txt": "python",
    "pyproject.toml": "python",
    "poetry.lock": "python",
    "uv.lock": "python",
    "Pipfile": "python",

    # Flask
    "app.py": "flask",
    "run.py": "flask",

    # Laravel
    "artisan": "laravel",
    "composer.json": "laravel",
    "composer.lock": "laravel",
    ".env.example": "laravel",
    "routes/web.php": "laravel",
    "routes/api.php": "laravel",

    # React
    "package.json": "react",
    "vite.config.js": "react",
    "vite.config.ts": "react",
    "react.config.js": "react",
    "index.jsx": "react",
    "index.tsx": "react",
    "App.jsx": "react",
    "App.tsx": "react",

    # Next.js
    "next.config.js": "nextjs",
    "next.config.mjs": "nextjs",
    "next.config.ts": "nextjs",
    "_app.tsx": "nextjs",
    "_document.tsx": "nextjs",
    "middleware.ts": "nextjs",

    # Vue
    "vue.config.js": "vue",
    "App.vue": "vue",
    "main.js": "vue",
    "main.ts": "vue",

    # Angular
    "angular.json": "angular",
    "main.ts": "angular",
    "app.component.ts": "angular",

    # Svelte
    "svelte.config.js": "svelte",
    "svelte.config.cjs": "svelte",
    "App.svelte": "svelte",

    # Node.js / Express
    "server.js": "express",
    "server.ts": "express",
    "app.js": "express",
    "app.ts": "express",
    "index.js": "nodejs",
    "index.ts": "nodejs",

    # NestJS
    "nest-cli.json": "nestjs",
    "main.ts": "nestjs",
    "app.module.ts": "nestjs",

    # Nuxt
    "nuxt.config.ts": "nuxt",
    "nuxt.config.js": "nuxt",

    # Remix
    "remix.config.js": "remix",
    "remix.config.ts": "remix",

    # Astro
    "astro.config.mjs": "astro",
    "astro.config.ts": "astro",

    # Spring Boot
    "pom.xml": "springboot",
    "build.gradle": "springboot",
    "build.gradle.kts": "springboot",
    "application.properties": "springboot",
    "application.yml": "springboot",

    # ASP.NET
    "Program.cs": "aspnet",
    "Startup.cs": "aspnet",
    "*.csproj": "aspnet",

    # Ruby on Rails
    "Gemfile": "rails",
    "config.ru": "rails",
    "Rakefile": "rails",

    # Phoenix
    "mix.exs": "phoenix",

    # Flutter
    "pubspec.yaml": "flutter",

    # Electron
    "electron.js": "electron",
    "electron.ts": "electron",

    # Tauri
    "tauri.conf.json": "tauri",

    # Docker
    "Dockerfile": "docker",
    "docker-compose.yml": "docker",
    "docker-compose.yaml": "docker",

    # Kubernetes
    "Chart.yaml": "helm",
    "values.yaml": "helm",

    # Terraform
    "main.tf": "terraform",
    "providers.tf": "terraform",
    "variables.tf": "terraform",

    # Git
    ".gitignore": "git",
    ".gitattributes": "git",
}

IGNORE = {".git", "node_modules","docs","document", "__pycache__", ".venv", "venv",".env"}

class Node:
    def __init__(self,path: Path):
        self.path = path
        self.languages = []
        self.evidence = {}
        self.children = []

    def mergetome(self, eviofchild: dict):
        for key,value in eviofchild.items():
            if key in self.evidence:
                self.evidence[key] = self.evidence[key]+value
            else:
                self.evidence[key] = value

    def printEvidence(self):
        print("The evidence from the root node")
        for key,value in self.evidence.items():
            print(EXTENSION_TO_LANGUAGE.get(key),":",value)

    def printLanguages(self):
        print("\nThe evidence from the root node")
        for data in self.languages:
            print(data)
        
    def cleaner(self):
        max = 0

        for key,value in self.evidence.items():
            if max<value:
                max = value
            
        max = max/2
        
        for key,value in self.evidence.items():
            if value >= max:
                lang = EXTENSION_TO_LANGUAGE.get(key)
                if lang not in self.languages:
                    self.languages.append(lang)

    


def detector(path_dir: str) -> Node:
    root = Path(path_dir).expanduser()

    node = Node(root)
    for item in os.listdir(root):
        if item in IGNORE:
            continue

        path = root / item

        if path.is_dir():
            child = detector(path)
            node.mergetome(child.evidence)
            node.children.append(child)
            node.cleaner()
        else:
            _, extension = os.path.splitext(item)
            if extension != '':
                node.evidence[extension]=node.evidence.get(extension,0)+1

    return node


node = detector("~/College Projects/noir")
node.printEvidence()
node.printLanguages()

# be a man dude solve this s#it all by yourself

# root = Path("~/College Projects/noir").expanduser()

# gitignore = root / ".gitignore"
# 

# spec = None
# if gitignore.exists():
#     spec = pathspec.PathSpec.from_lines(
#         "gitwildmatch",
#         gitignore.read_text().splitlines()
#     )

# for current_dir, dirs, files in os.walk(root):
#     dirs[:] = [d for d in dirs if d not in IGNORE]

#     current = Path(current_dir)
#     depth = len(current.relative_to(root).parts)

#     indent = "    " * depth

#     print(f"{indent}📁 {current.name}")

#     for file in sorted(files):
#         print(f"{indent}    📄 {file}")

#         if spec:
#             path = current / file
#             relative = path.relative_to(root).as_posix()
#             if spec.match_file(relative):
#                 continue

#         print(f"{indent}    📄 {file}")
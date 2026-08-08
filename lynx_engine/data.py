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

FILES_TO_TECHNOLOGY = {
    "frameworks": {
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

        "main.py": "fastapi",
        "app.py": "flask",
        "run.py": "flask",

        # Laravel
        "artisan": "laravel",
        "routes/web.php": "laravel",
        "routes/api.php": "laravel",

        # React
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

        # Vue
        "vue.config.js": "vue",
        "App.vue": "vue",

        # Angular
        "angular.json": "angular",
        "app.component.ts": "angular",

        # Svelte
        "svelte.config.js": "svelte",
        "svelte.config.cjs": "svelte",
        "App.svelte": "svelte",

        # NestJS
        "nest-cli.json": "nestjs",
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

        # Spring
        "pom.xml": "spring",
        "build.gradle": "spring",
        "build.gradle.kts": "spring",

        # ASP.NET
        "Program.cs": "aspnet",
        "Startup.cs": "aspnet",

        # Rails
        "Gemfile": "rails",
        "config.ru": "rails",
        "Rakefile": "rails",

        # Phoenix
        "mix.exs": "phoenix",

        # Flutter
        "pubspec.yaml": "flutter",
    },

    "libraries": {
        "serializers.py": "django_rest_framework",
        "routers.py": "django_rest_framework",
    },

    "runtimes": {
        "index.js": "nodejs",
        "index.ts": "nodejs",
        "server.js": "nodejs",
        "server.ts": "nodejs",
    },

    "tools": {
        # Docker
        "Dockerfile": "docker",
        "docker-compose.yml": "docker",
        "docker-compose.yaml": "docker",

        # Kubernetes / Helm
        "Chart.yaml": "helm",
        "values.yaml": "helm",

        # Terraform
        "main.tf": "terraform",
        "providers.tf": "terraform",
        "variables.tf": "terraform",

        # Git
        ".gitignore": "git",
        ".gitattributes": "git",

        # Electron
        "electron.js": "electron",
        "electron.ts": "electron",

        # Tauri
        "tauri.conf.json": "tauri",
    },

    "package_managers": {
        "package.json": "npm",
        "package-lock.json": "npm",
        "bun.lock": "bun",
        "composer.json": "composer",
        "composer.lock": "composer",
        "poetry.lock": "poetry",
        "Pipfile": "pipenv",
        "uv.lock": "uv",
    },

    "configuration": {
        "pyproject.toml": "python",
        "requirements.txt": "python",
        ".env.example": "environment",
        "application.properties": "spring",
        "application.yml": "spring",
    },
}

IGNORE = {
    ".git",
    "node_modules",
    "docs",
    "document",
    "__pycache__",
    ".venv",
    "venv",
    ".env",
}
# Lynx
Python Program that scans the user's current working directory and identifies the Language, Tech stack etc..


There are 3 parts to this, first a scanner function that scans and returns this following format
```
{
    "extensions": {
        ".py": 183,
        ".js": 51,
        ".html": 12
    },

    "files": {
        "manage.py",
        "settings.py",
        "package.json",
        "vite.config.ts"
    },

    "directories": {
        "templates",
        "migrations",
        "node_modules"
    },

    "dependencies": {
        "django",
        "djangorestframework",
        "react",
        "vite"
    }
}

```
def validate_solution(challenge, solution):
    s = solution.lower()
    title = challenge.title.strip().lower()

    rules = {

        # ===================== PYTHON =====================
        "variables & loops": [
            "for", "if"
        ],

        "file manager script": [
            "open(", "read", "write"
        ],

        "api data processor": [
            "requests", "json"
        ],

        # ===================== DJANGO =====================
        "first django view": [
            "def", "render"
        ],

        "crud blog app": [
            "models", "create", "update", "delete"
        ],

        "authentication system": [
            "login", "logout"
        ],

        # ===================== JAVASCRIPT =====================
        "dom click counter": [
            "addeventlistener", "click"
        ],

        "to-do list app": [
            "add", "delete"
        ],

        "weather dashboard": [
            "fetch", "weather"
        ],

        # ===================== REACT =====================
        "counter component": [
            "usestate"
        ],

        "movie search app": [
            "fetch", "search"
        ],

        "authenticated dashboard": [
            "login"
        ],

        # ===================== VUE =====================
        "vue counter": [
            "data", "methods"
        ],

        "notes app": [
            "add", "delete"
        ],

        "real-time chat app": [
            "realtime"
        ],

        # ===================== HTML =====================
        "personal profile page": [
            "<header", "<section"
        ],

        "multi-page website": [
            "nav", "href"
        ],

        "accessible website": [
            "aria", "alt"
        ],

        # ===================== CSS =====================
        "styled card": [
            "box-shadow", "hover"
        ],

        "responsive layout": [
            "flex", "grid"
        ],

        "animation portfolio": [
            "keyframes", "transition"
        ],

        # ===================== TAILWIND =====================
        "button styling": [
            "bg-", "text-"
        ],

        "responsive card grid": [
            "grid", "gap-"
        ],

        "full landing page": [
            "flex", "container"
        ],

        # ===================== NODE =====================
        "simple server": [
            "http", "hello"
        ],

        "rest api": [
            "get", "post"
        ],

        "auth api system": [
            "jwt"
        ],
    }

    if title not in rules:
        return False

    return all(keyword in s for keyword in rules[title])
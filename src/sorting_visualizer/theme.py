WARM_EDITORIAL: dict[str, str] = {
    # UI elemnts
    "main-bg": "#FAF7F2",
    "panel": "#FFFFFF",
    "secondary-surf": "#F0E9DF",
    "border": "#DDD3C5",
    "primary-text": "#202938",
    "secondary-text": "#287D78",
    "primary-accent": "#C65D45",
    "secondary-accent": "#287D78",
    # Sorting colors
    "bar-def": "#8B95A5",
    "bar-cmp": "#D97706",
    "bar-swp": "#D9485F",
    "bar-piv": "#805AD5",
    "bar-srt": "#218568",
    "bar-act": "#2878B5",
}

MIDNIGHT_INDIGO: dict[str, str] = {
    # UI elemnts
    "main-bg": "#0B1020",
    "panel": "#151C30",
    "secondary-surf": "#202A42",
    "border": "#303B55",
    "primary-text": "#F1F5F9",
    "secondary-text": "#94A3B8",
    "primary-accent": "#818CF8",
    "secondary-accent": "#38BDF8",
    # Sorting colors
    "bar-def": "#64748B",
    "bar-cmp": "#FBBF24",
    "bar-swp": "#FB7185",
    "bar-piv": "#A78BFA",
    "bar-srt": "#34D399",
    "bar-act": "#38BDF8",
}


class Theme:
    def __init__(self, theme: dict[str, str] = WARM_EDITORIAL) -> None:
        self.main_background: str = theme["main-bg"]
        self.panel: str = theme["panel"]
        self.secondary_surface: str = theme["secondary-surf"]
        self.border: str = theme["border"]
        self.primary_text: str = theme["primary-text"]
        self.secondary_text: str = theme["secondary-text"]
        self.primary_accent: str = theme["primary-accent"]
        self.secondary_accent: str = theme["secondary-accent"]

        self.bar_default: str = theme["bar-def"]
        self.bar_compare: str = theme["bar-cmp"]
        self.bar_swap: str = theme["bar-swp"]
        self.bar_pivot: str = theme["bar-piv"]
        self.bar_sorted: str = theme["bar-srt"]
        self.bar_active: str = theme["bar-act"]

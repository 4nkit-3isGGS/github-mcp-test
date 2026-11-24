"""A tiny greeting utility for repository and MCP testing."""

from datetime import datetime


def make_greeting(name: str, *, moment: datetime | None = None) -> str:
    """Return a friendly greeting, with a time-aware welcome."""
    current_hour = (moment or datetime.now()).hour
    if current_hour < 12:
        daypart = "Good morning"
    elif current_hour < 18:
        daypart = "Good afternoon"
    else:
        daypart = "Good evening"

    return f"{daypart}, {name}! Welcome to the sample project."


if __name__ == "__main__":
    print(make_greeting("MCP explorer"))

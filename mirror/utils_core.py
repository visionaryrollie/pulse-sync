# utils_core.py — Core data bridge between mirrored pages

__state_cache = {
    "A_to_B": "No message from A yet.",
    "B_to_A": "No message from B yet."
}

def update_message(origin: str, payload: str) -> None:
    """
    Accepts a message from one page and updates the mirrored state.
    """
    if origin == "A":
        __state_cache["A_to_B"] = payload
    elif origin == "B":
        __state_cache["B_to_A"] = payload

def get_message(target: str) -> str:
    """
    Retrieves the latest message intended for the target page.
    """
    if target == "B":
        return __state_cache["A_to_B"]
    elif target == "A":
        return __state_cache["B_to_A"]
    return "No message."



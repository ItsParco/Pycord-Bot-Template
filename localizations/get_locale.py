from typing import Optional, Union
from utils import utils


def get_locale(
    *,
    name: str,
    item: str,
    locale: Optional[str] = None,
    type_: str = "commands"
) -> Union[str, dict]:
    locale_responses = utils.load("./localizations/locale.json")

    try:
        section = locale_responses[type_][name]
    except KeyError:
        raise KeyError(
            f"Localization type '{type_}' or command '{name}' not found.")

    if locale:
        try:
            responses = section[item]
        except KeyError:
            raise KeyError(f"Locale item '{item}' not found.")
        return responses.get(locale, "en-US")
    else:
        try:
            return section[item]
        except Exception:
            raise KeyError(
                f"Item '{item}' not found in any locale for '{name}'.")

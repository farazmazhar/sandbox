"""

A small map demo.
"""

list_of_str = [
    'shadow of the tomb raider',
    'batman: Arkham knight',
    'half-life',
    'portal',
    'dota 2',
    'counter-strike: global offensive'
]


def title_case(string: str) -> str:
    """
    Makes text title case.

    Args:
        string (str): Input string.

    Returns:
        str: String in title case.
    """
    return string.title()


if __name__ == "__main__":
    list_of_title_str = list(map(title_case, list_of_str))

    print(list_of_title_str)

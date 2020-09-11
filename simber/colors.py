"""Handle formatting related to colors."""

from colorama import init, Fore
from re import findall


class ColorFormatter(object):
    """Format colors to the passed string.

    The colors will be decided based on the level
    passed and accordingly replaced in the string
    and returned.
    """
    def __init__(self):
        init()
        self.color_mapping = {
            'g': Fore.GREEN,
            'r': Fore.RED
        }
        self.default = Fore.RESET

    def _get_color_replacement(self, special_str):
        """Get the colored replacement of the passed
        special str.

        The string will be of the following type
        `%gsample_string%`

        where, g is the color code. We need to replace
        `%g` with the color code and we need to replace the
        ending `%` with proper reset code.
        """
        prefix = special_str[:2]
        postfix = special_str[:-1]  # This will always be % tho
        color = prefix[1]

        replaced_color = self.color_mapping.get(color, self.default)

        # Do the substitution now
        special_str = special_str.replace(prefix, replaced_color)
        special_str = special_str.replace(postfix, self.default)

        return special_str

    def _replace_with_colors(self, str_passed):
        """Find the special characters in the string
        and replace them with the colors as passed by the
        user.
        """
        occurences = findall(r'%.*?%', str_passed)

        for occurence in occurences:
            str_passed.replace(occurence,
                               self._get_color_replacement(occurence))

        return str_passed

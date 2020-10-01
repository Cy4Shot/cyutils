#Store color codes
colors = {
  "standard"   :  "\033[0m",
  "black"   :  "\033[30m",
  "red"     :  "\033[31m",
  "green"   :  "\033[32m",
  "yellow"  :  "\033[33m",
  "blue"    :  "\033[34m",
  "magenta" :  "\033[35m",
  "cyan"    :  "\033[36m",
  "white"   :  "\033[37m"
}

def clrprint(text, color):
  """Prints text with a certain color.

    Parameters:
    text (string): Text to be printed.
    color (string): Color of the text. (Accepts: standard, black, red, green, yellow, blue, magenta, cyan, white)

    Returns:
    list: List filled with 0.0s.
    """
  print(colors[color] + text + colors["standard"])
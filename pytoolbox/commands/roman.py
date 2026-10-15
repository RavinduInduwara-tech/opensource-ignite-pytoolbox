import typer
from rich.console import Console

NAME = "roman"
HELP = "convert int to roman and roman to int"

console = Console()

int_roman ={'1':'i','2':'ii','3':'iii','4':'iv','5':'v','6':'vi','7':'vii','8':'viii','9':'ix','10':'x'}
roman_int = {value: key for key, value in int_roman.items()}

def _integer_to_roman(text: str) -> str:
    return int_roman[text]

def _roman_to_integer(text: str) -> str:
    return roman_int[text]


def main(text: str, words: bool = False) -> None:
    if text == "":
        console.print("[red]Error:[/red] text must not be empty")
        raise typer.Exit(code=1)

    result = _integer_to_roman(text) if words else _roman_to_integer(text)
    console.print(result)
import typer
import datetime

app = typer.Typer()

DATETIME_OBJ = datetime.datetime(1970, 1, 1)


@app.command()
def day(date_string: str = DATETIME_OBJ.now().strftime("%d/%m/%Y")):
    date = DATETIME_OBJ.strptime(date_string, "%d/%m/%Y")
    if date_string == DATETIME_OBJ.now().strftime("%d/%m/%Y"):
        typer.echo(f"Today is {date.strftime('%A')}")
    else:
        typer.echo(f"It's a {date.strftime('%A')}")


if __name__ == "__main__":
    app()

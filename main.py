import typer
import datetime
import emoji

app = typer.Typer()

DATETIME_OBJ = datetime.datetime(1970, 1, 1)

DAY_EMOJIS = {
    'Monday': ':confounded_face:',
    'Tuesday': ':smirking_face:',
    'Wednesdat': ':relieved_face:',
    'Thursday': ':smiling_face_with_smiling_eyes:',
    'Friday': ':winking_face_with_tongue:',
    'Saturday': ':squinting_face_with_tongue:',
    'Sunday': ':woozy_face:'
}

@app.command()
def day(date_string: str = DATETIME_OBJ.now().strftime("%d/%m/%Y")):
    date = DATETIME_OBJ.strptime(date_string, "%d/%m/%Y")
    day = date.strftime('%A')
    day += f" {emoji.emojize(DAY_EMOJIS[day])}"
    if date_string == DATETIME_OBJ.now().strftime("%d/%m/%Y"):
        typer.echo(f"Today is {day}")
    else:
        typer.echo(f"It's a {day}")


if __name__ == "__main__":
    app()

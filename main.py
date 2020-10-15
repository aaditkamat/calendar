import click
import typer
import datetime
import emoji

app = typer.Typer()

DATETIME_OBJ = datetime.datetime(1970, 1, 1)

DAY_EMOJIS = {
    "Monday": ":confounded_face:",
    "Tuesday": ":smirking_face:",
    "Wednesday": ":relieved_face:",
    "Thursday": ":smiling_face_with_smiling_eyes:",
    "Friday": ":winking_face_with_tongue:",
    "Saturday": ":squinting_face_with_tongue:",
    "Sunday": ":woozy_face:",
}


@app.command()
def day(date_string: str):
    try:
        # Allow use to key in special keyword today as an argument
        if date_string.strip().lower() == "today":
            date_string = DATETIME_OBJ.now().strftime("%d/%m/%Y")
        date = DATETIME_OBJ.strptime(date_string, "%d/%m/%Y")
        day = date.strftime("%A")
        day += f" {emoji.emojize(DAY_EMOJIS[day])}"
        if date_string == DATETIME_OBJ.now().strftime("%d/%m/%Y"):
            typer.echo(f"Today is {day}")
        else:
            typer.echo(f"{date.strftime('%B %d %Y')} was a {day}")
    except ValueError:
        raise click.BadArgumentUsage(
            "DATE_STRING argument {date_string} is not of the expected format DD/MM/YYYY"
        )


@app.command()
def duration(
    start_date_string: str, end_date_string: str,
):
    try:
        start_date, end_date = (
            DATETIME_OBJ.strptime(start_date_string, "%d/%m/%Y"),
            DATETIME_OBJ.strptime(end_date_string, "%d/%m/%Y"),
        )
        difference = (end_date - start_date).days
        print(
            f"Duration between {start_date_string} and {end_date_string} (including the end date): {difference + 1} days"
        )
        print(
            f"Duration between {start_date_string} and {end_date_string} (excluding the end date): {difference} days"
        )
    except ValueError:
        raise click.BadArgumentUsage(
            f"Either the START_DATE_STRING argument {start_date_string} or the END_DATE_STRING argument {end_date_string} is not of the expected format DD/MM/YYYY"
        )


if __name__ == "__main__":
    app()

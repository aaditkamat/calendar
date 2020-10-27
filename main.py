import click
import typer
import datetime
import emoji

app = typer.Typer()

DATETIME_OBJ = datetime.datetime(1970, 1, 1)

DAYS_OF_THE_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

DAY_EMOJIS = {
    "Monday": ":confounded_face:",
    "Tuesday": ":smirking_face:",
    "Wednesday": ":relieved_face:",
    "Thursday": ":smiling_face_with_smiling_eyes:",
    "Friday": ":winking_face_with_tongue:",
    "Saturday": ":squinting_face_with_tongue:",
    "Sunday": ":woozy_face:",
}

## The function that handles the day command. The day command only accepts a string
## that represents the date in DD/MM/YYYY format. Also adds an emoji at the end based
## on what day the date falls on.


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


def calculate_days_diff(start_date, end_date):
    if end_date.day >= start_date.day:
        return end_date.day - start_date.day
    else:
        return (DAYS_OF_THE_MONTH[start_date.month] - start_date.day) + end_date.day


def calculate_months_diff(start_date, end_date):
    if end_date.month >= start_date.month:
        return end_date.month - start_date.month
    else:
        return (end_date.month + 12) - start_date.month


def calculate_years_diff(start_date, end_date):
    if start_date.month >= end_date.month:
        return end_date.year - start_date.year
    else:
        return end_date.year - start_date.year - 1


## The function that handles the duration command. The duration command accepts two strings
## in DD/MM/YYYY format. The first is the start date and the other is the end date. This
## command outputs the duration between the two dates in terms of days, months and years.


@app.command()
def duration(
    start_date_string: str,
    end_date_string: str,
):
    try:
        start_date, end_date = (
            DATETIME_OBJ.strptime(start_date_string, "%d/%m/%Y"),
            DATETIME_OBJ.strptime(end_date_string, "%d/%m/%Y"),
        )
        diff = end_date - start_date
        if diff.days < 0:
            raise click.BadArgumentUsage(
                f"The start date  must come after the end date"
            )
        days_diff = calculate_days_diff(start_date, end_date)
        months_diff = calculate_months_diff(start_date, end_date)
        years_diff = calculate_years_diff(start_date, end_date)
        print(
            f"The duration between {start_date} and {end_date} is: {years_diff} years, {months_diff} months and {days_diff} days."
        )

    except ValueError:
        raise click.BadArgumentUsage(
            f"Either the START_DATE_STRING argument {start_date_string} or the END_DATE_STRING argument {end_date_string} is not of the expected format DD/MM/YYYY"
        )


if __name__ == "__main__":
    app()

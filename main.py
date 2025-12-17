from pyscript import display, document

# Just a small helper so I don’t repeat code.
# This grabs the value from an input box. If it's empty, I return None
# so I can easily check later if the user forgot something.
def get_value(id):
    value = document.getElementById(id).value
    if value == "":
        return None
    return float(value)

# This is the main function that runs when you click "Calculate GWA".
# It gets all the grades, checks if anything is missing, computes the GWA,
# and then shows everything on the screen.
def general_weighted_average(e):

    # Clear old results so they don’t pile up.
    display("", target="error")
    display("", target="student_info")
    display("", target="summary")
    display("", target="output")

    # Getting all the grades from the input fields.
    # If a field is empty, get_value() will return None.
    fields = {
        "Math": get_value("mathgr"),
        "Science": get_value("scigr"),
        "English": get_value("enggr"),
        "Filipino": get_value("filgr"),
        "Social Studies": get_value("socgr"),
        "ICT": get_value("ictgr"),
        "PE": get_value("pegr")
    }

    # If even one grade is missing, I stop everything and show an error.
    if None in fields.values():
        display("Please enter all grades.", target="error")
        return

    # These are the weights/units for each subject.
    # Basically, the higher the weight, the more it affects your GWA.
    weights = {
        "Math": 5,
        "Science": 5,
        "English": 5,
        "Filipino": 3,
        "Social Studies": 3,
        "ICT": 2,
        "PE": 1
    }

    # Multiply each grade by its weight and add them all together.
    weighted_sum = sum(fields[subj] * weights[subj] for subj in fields)

    # Total number of units (just adding all the weights).
    total_units = sum(weights.values())

    # Final GWA. I round it to 2 decimals so it looks clean.
    gwa = round(weighted_sum / total_units, 2)

    # Show the student's name above the results.
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value
    display(f"Name: {first} {last}", target="student_info")

    # Build the summary box with color-coded grades.
    # Green = high grade, Red = failing grade, everything else is normal.
    summary_html = ""
    for subj, grade in fields.items():
        css_class = "grade-high" if grade >= 90 else "grade-low" if grade < 75 else ""
        summary_html += f"<div class='{css_class}'>{subj}: {round(grade)}</div>"

    document.getElementById("summary").innerHTML = summary_html

    # Show the final GWA at the bottom.
    display(f"Your General Weighted Average is {gwa}", target="output")

# This function runs when you click "Clear".
# It resets all the input boxes and removes everything on the screen.
def clear_all(e):

    # All the input fields I need to reset.
    ids = [
        "first_name", "last_name",
        "mathgr", "scigr", "enggr",
        "filgr", "socgr", "pegr", "ictgr"
    ]

    # Set each input box back to empty.
    for i in ids:
        document.getElementById(i).value = ""

    # Clear all the displayed results.
    display("", target="error")
    display("", target="student_info")
    display("", target="summary")
    display("", target="output")

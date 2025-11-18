from js import document
from pyscript import display

def general_weighted_average(e):
    display("", target="student_info")
    display("", target="summary")
    display("", target="output")

    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

    Science = float(document.getElementById("Science").value)
    Math = float(document.getElementById("Math").value)
    English = float(document.getElementById("English").value)
    Filipino = float(document.getElementById("Filipino").value)
    ICT = float(document.getElementById("ICT").value)
    PE = float(document.getElementById("PE").value)

    # Subject Weights
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
    units_subject = (5, 3, 2, 1)  # for explanation; explicit weights used below

    # Weighted Average
    weighted_sum = (Science * 5 + Math * 5 + English * 5 +
                    Filipino * 3 + ICT * 2 + PE * 1)
    total_units = (5 * 3) + 3 + 2 + 1  # 3 subjects @ 5 + 3 + 2 + 1 = 21
    gwa = weighted_sum / total_units

    # Display Results
    summary = f"""{subjects[0]}: {science:.0f}
{subjects[1]}: {Math:.0f}
{subjects[2]}: {English:.0f}
{subjects[3]}: {Filipino:.0f}
{subjects[4]}: {ICT:.0f}
{subjects[5]}: {PE:.0f}
"""
    display(f'Your general weighted average is {gwa:.2f}', target='output')

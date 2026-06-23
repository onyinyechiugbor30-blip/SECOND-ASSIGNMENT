'''Question 2: Write a function analyze_age(dob_tuple) where dob_tuple = (day, month, year). Inside it :
Calculate exact age in years, months, and days(as of current date- hardcore today's date)
Use if elif chains to determine life stage(Child, Teen, Young, Adult, Senior, etc)
Return a detailed report string
Create another function
compare_ages(person_list)that takes a list of(name, dob_tuple)
and finds the oldest and youngest person using loops
Test with at least 5 family members'''
#date of birth stored as a tuple in the format(day, month and year)
date_of_birth = (10, 3, 2005)
birth_date = 10
birth_month = 3
birth_year = 2005
#hardcoded current date
current_date = 21
current_month = 6
current_year = 2026

# This function calculates a person's age
def analyze_age(dob_tuple):
    # Take the day, month and year from the DOB tuple
    day, month, year = dob_tuple
    # Find the difference in years, months and days
    age_years = current_year - year
    age_months = current_month - month
    age_days = current_date - day
    # If months become negative,  borrow 1 year and turn it into 12 months
    if age_months < 0:
        age_years = age_years - 1
        age_months = age_months + 12
    # If days become negative, borrow 1 month and use 30 days(just to be on the safe side even though month is 30 or 31
    # except february
    if age_days < 0:
        age_months = age_months - 1
        age_days = age_days + 30
    # Decide the life stage
    if age_years <= 12:
        stage = "Child"
    elif age_years <= 19:
        stage = "Teen"
    elif age_years <= 35:
        stage = "Young Adult"
    elif age_years <= 60:
        stage = "Adult"
    else:
        stage = "Senior"
    # Send back the result of the analyzed age
    return (
        f"Age: {age_years} years, "
        f"{age_months} months, "
        f"{age_days} days\n"
        f"Life Stage: {stage}"
    )
# This function finds the oldest and youngest person
def compare_ages(person_list):
    # Start by assuming the first person
    # is both the oldest and youngest
    oldest = person_list[0]
    youngest = person_list[0]
    # Check everybody in the list
    for name, dob in person_list:
        # Take out the birth year
        day, month, year = dob
        # Smaller year means older person
        if year < oldest[1][2]:
            oldest = (name, dob)
        # Bigger year means younger person
        if year > youngest[1][2]:
            youngest = (name, dob)
    return oldest, youngest

#list of Family members
family = [
    ("Martha", (10, 5, 1970)),
    ("Isaac", (25, 7, 1975)),
    ("Grace", (12, 3, 2000)),
    ("Justice", (5, 11, 2010)),
    ("Emeka", (10, 8, 2016))
]

# Show age report for everybody
for name, dob in family:
    print("Name:", name)
    print(analyze_age(dob))
    print()
# Find oldest and youngest
oldest, youngest = compare_ages(family)
print("Oldest Person:", oldest[0])
print("Youngest Person:", youngest[0])
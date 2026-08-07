# preptrack-Yaswanth
# PrepTrack — Placement Preparation Performance Analyzer

## Project Overview

PrepTrack is a Python console application that analyses a single student's placement-preparation performance. It collects the student's profile details, attendance, project-completion status, profile-verification status, and seven days of coding-practice scores. The program validates every input, classifies each attempted score, tracks passed/failed/attempted/absent days, identifies the highest and lowest scores along with the first critical score, and calculates the total and average performance. Based on all of this, it evaluates whether the student is ready for a placement mock interview and displays the first major blocker along with the recommended next action.

## Features Implemented

- Student-profile input (name, registration number, graduation year)
- Student name validation (rejects empty input using a `while` loop)
- Attendance validation (accepts only 0–100)
- Yes/no input validation for project-completion and profile-verification status
- Seven-day practice score processing using a single `for` loop
- Score validation (accepts `-1` for absent, or `0`–`100`)
- Absent-day handling using `continue`
- Score classification into Strong / Satisfactory / Needs Improvement / Critical
- Passed and failed day counting
- Highest and lowest attempted score detection (with correct tie-breaking to the first occurrence)
- First critical score detection (day and value)
- Total score accumulation and average calculation with division-by-zero prevention
- Placement-readiness evaluation using combined Boolean conditions
- First-major-blocker detection using a prioritized `if`/`elif` chain
- Complete final report with student profile, practice summary, performance analysis, critical score information, and final decision

## Python Concepts Used

- `input()`, `int()`, `float()`
- Variables and meaningful variable names
- Strings, integers, floating-point values, Booleans
- Arithmetic, assignment, relational, and logical operators
- Boolean expressions
- f-strings
- `if`, `elif`, `else`
- Compound and nested conditions
- `while` loops for input validation
- `for` loop with `range()` for repeated input
- `break` after valid input
- `continue` to skip absent practice days
- Counters and accumulator variables

## How to Run

```bash
python main.py
```

Depending on your system configuration, you may need to use:

```bash
python3 main.py
```

## Test-Result Summary

| Test ID | Scenario | Expected Result | Actual Result | Status |
|---------|----------|------------------|----------------|--------|
| TC-01 | All requirements satisfied | Ready for Mock Interview | Ready for Mock Interview | ✅ Pass |
| TC-02 | One score below 40 | Critical Support Required | Critical Support Required | ✅ Pass |
| TC-03 | Fewer than six attempted days | Practice Incomplete | Practice Incomplete | ✅ Pass |
| TC-04 | Fewer than four passed days | Insufficient Passed Practices | Insufficient Passed Practices | ✅ Pass |
| TC-05 | Average below 70 | Practice Improvement Required | Practice Improvement Required | ✅ Pass |
| TC-06 | Attendance below 75 | Attendance Improvement Required | Attendance Improvement Required | ✅ Pass |
| TC-07 | Graduation year not eligible | Graduation Criteria Not Met | Graduation Criteria Not Met | ✅ Pass |
| TC-08 | Project incomplete | Application On Hold | Application On Hold | ✅ Pass |
| TC-09 | Profile not verified | Application On Hold | Application On Hold | ✅ Pass |
| TC-10 | All seven days absent | Practice Not Evaluated | Practice Not Evaluated | ✅ Pass |
| TC-11 | Invalid score below -1 | Input rejected | Input rejected | ✅ Pass |
| TC-12 | Invalid score above 100 | Input rejected | Input rejected | ✅ Pass |
| TC-13 | Exact boundary scores | Correct classifications | Correct classifications | ✅ Pass |
| TC-14 | Multiple failed requirements | First major blocker displayed | First major blocker displayed | ✅ Pass |

### Sample Program Output

**Test Case 1 — All requirements satisfied (TC-01)**

```
==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: yaswanth
Enter registration number: 102
Enter graduation year: 2026
Enter attendance percentage: 85
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent: 80
Day 1 Result : Strong
Enter Day 2 score (0-100) or -1 for absent: 75
Day 2 Result : Strong
Enter Day 3 score (0-100) or -1 for absent: 72
Day 3 Result : Satisfactory
Enter Day 4 score (0-100) or -1 for absent: 78
Day 4 Result : Strong
Enter Day 5 score (0-100) or -1 for absent: 90
Day 5 Result : Strong
Enter Day 6 score (0-100) or -1 for absent: 70
Day 6 Result : Satisfactory
Enter Day 7 score (0-100) or -1 for absent: 82
Day 7 Result : Strong

==================================================
              PREPTRACK REPORT
==================================================

STUDENT PROFILE

Student Name             : yaswanth
Registration Number      : 102
Graduation Year          : 2026
Attendance               : 85.0%
Project Completed        : Yes
Profile Verified         : Yes

PRACTICE SUMMARY

Total Practice Days      : 7
Attempted Days           : 7
Absent Days              : 0
Passed Days              : 7
Failed Days              : 0

Strong Days              : 5
Satisfactory Days        : 2
Needs Improvement Days   : 0
Critical Days            : 0

PERFORMANCE ANALYSIS

Total Score              : 547
Average Score            : 78.14
Highest Score            : 90

CRITICAL SCORE INFORMATION

Critical Score Found     : No
First Critical Day       : Not Applicable
First Critical Score     : Not Applicable

FINAL DECISION

Final Status             : Ready for Mock Interview
Primary Blocker          : None
Next Action              : Proceed to placement mock interviews
==================================================
```

**Test Case 2 — Critical score detected (TC-02)**

```
==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: yaswanth
Enter registration number: 102
Enter graduation year: 2026
Enter attendance percentage: 85
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent: 75
Day 1 Result : Strong
Enter Day 2 score (0-100) or -1 for absent: 35
Day 2 Result : Critical
Enter Day 3 score (0-100) or -1 for absent: 80
Day 3 Result : Strong
Enter Day 4 score (0-100) or -1 for absent: 70
Day 4 Result : Satisfactory
Enter Day 5 score (0-100) or -1 for absent: 72
Day 5 Result : Satisfactory
Enter Day 6 score (0-100) or -1 for absent: 76
Day 6 Result : Strong
Enter Day 7 score (0-100) or -1 for absent: 68
Day 7 Result : Satisfactory

==================================================
              PREPTRACK REPORT
==================================================

STUDENT PROFILE

Student Name             : yaswanth
Registration Number      : 102
Graduation Year          : 2026
Attendance               : 85.0%
Project Completed        : Yes
Profile Verified         : Yes

PRACTICE SUMMARY

Total Practice Days      : 7
Attempted Days           : 7
Absent Days              : 0
Passed Days              : 6
Failed Days              : 1

Strong Days              : 3
Satisfactory Days        : 3
Needs Improvement Days   : 0
Critical Days            : 1

PERFORMANCE ANALYSIS

Total Score              : 476
Average Score            : 68.00
Highest Score            : 80
Highest Score Day        : Day 3
Lowest Score             : 35
Lowest Score Day         : Day 2

CRITICAL SCORE INFORMATION

Critical Score Found     : Yes
First Critical Day       : Day 2
First Critical Score     : 35

FINAL DECISION

Final Status             : Critical Support Required
Primary Blocker          : Critical score found on Day 2
Next Action              : Revise the concepts from the first critical day
==================================================
```

**Test Case 3 — Practice Incomplete (TC-03)**

```
==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: yaswanth
Enter registration number: 102
Enter graduation year: 2026
Enter attendance percentage: 85
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent: 80
Day 1 Result : Strong
Enter Day 2 score (0-100) or -1 for absent: -1
Day 2 Result : Absent
Enter Day 3 score (0-100) or -1 for absent: 75
Day 3 Result : Strong
Enter Day 4 score (0-100) or -1 for absent: -1
Day 4 Result : Absent
Enter Day 5 score (0-100) or -1 for absent: 90
Day 5 Result : Strong
Enter Day 6 score (0-100) or -1 for absent: 70
Day 6 Result : Satisfactory
Enter Day 7 score (0-100) or -1 for absent: -1
Day 7 Result : Absent

==================================================
              PREPTRACK REPORT
==================================================

STUDENT PROFILE

Student Name             : yaswanth
Registration Number      : 102
Graduation Year          : 2026
Attendance               : 85.0%
Project Completed        : Yes
Profile Verified         : Yes

PRACTICE SUMMARY

Total Practice Days      : 7
Attempted Days           : 4
Absent Days              : 3
Passed Days              : 4
Failed Days              : 0

Strong Days              : 3
Satisfactory Days        : 1
Needs Improvement Days   : 0
Critical Days            : 0

PERFORMANCE ANALYSIS

Total Score              : 315
Average Score            : 78.75
Highest Score            : 90
Highest Score Day        : Day 5
Lowest Score             : 70
Lowest Score Day         : Day 6

CRITICAL SCORE INFORMATION

Critical Score Found     : No
First Critical Day       : Not Applicable
First Critical Score     : Not Applicable

FINAL DECISION

Final Status             : Practice Incomplete
Primary Blocker          : Fewer than six practices attempted
Next Action              : Complete at least six practice days
==================================================
```

**Test Case 4 — All seven days absent (TC-04)**

```
==================================================
              PREPTRACK APPLICATION
==================================================
Enter student name: yaswanth
Enter registration number: 102
Enter graduation year: 2026
Enter attendance percentage: 85
Has the student completed the required project? (yes/no): yes
Is the student profile verified? (yes/no): yes
Enter Day 1 score (0-100) or -1 for absent: -1
Day 1 Result : Absent
Enter Day 2 score (0-100) or -1 for absent: -1
Day 2 Result : Absent
Enter Day 3 score (0-100) or -1 for absent: -1
Day 3 Result : Absent
Enter Day 4 score (0-100) or -1 for absent: -1
Day 4 Result : Absent
Enter Day 5 score (0-100) or -1 for absent: -1
Day 5 Result : Absent
Enter Day 6 score (0-100) or -1 for absent: -1
Day 6 Result : Absent
Enter Day 7 score (0-100) or -1 for absent: -1
Day 7 Result : Absent

==================================================
              PREPTRACK REPORT
==================================================

STUDENT PROFILE

Student Name             : yaswanth
Registration Number      : 102
Graduation Year          : 2026
Attendance               : 85.0%
Project Completed        : Yes
Profile Verified         : Yes

PRACTICE SUMMARY

Total Practice Days      : 7
Attempted Days           : 0
Absent Days              : 7
Passed Days              : 0
Failed Days              : 0

Strong Days              : 0
Satisfactory Days        : 0
Needs Improvement Days   : 0
Critical Days            : 0

PERFORMANCE ANALYSIS

Total Score              : 0
Average Score            : 0.00
Highest Score            : Not Available

CRITICAL SCORE INFORMATION

Critical Score Found     : No
First Critical Day       : Not Applicable
First Critical Score     : Not Applicable

FINAL DECISION

Final Status             : Practice Not Evaluated
Primary Blocker          : No practice attempted
Next Action              : Attempt the required coding practices
==================================================
```

## Individual Contribution

| Field | Details |
|-------|---------|
| Name | Yaswanth Yuva Kiran N |
| Repository URL | https://github.com/YaswanthN28/preptrack-Yaswanth.git |
| My Main Contribution | Built the complete PrepTrack application, including student profile input and validation, seven-day coding practice processing, score classification, performance analysis, placement readiness evaluation, and the final report generation. |
| Features I Implemented | Student name validation, attendance validation, project-completion and profile-verification input validation, seven-day practice score processing with a single loop, absent-day handling, score classification, passed/failed day counting, highest and lowest score detection, first critical score detection, average score calculation with division-by-zero prevention, placement-readiness evaluation, and the complete final report. |
| Python Concepts I Used | Variables, strings, integers, floats, Boolean expressions, if-elif-else, while loops, for loops, break, continue, range(), counters, accumulators, relational operators, logical operators, and f-strings. |
| Most Difficult Logic | Getting the final-status priority order right so that only the first major blocker is displayed when multiple eligibility conditions fail at once. |
| Problem I Faced | Making sure absent practice days did not affect the total score, average score, or the highest/lowest score tracking. |
| How I Solved It | Used continue to skip absent days before any accumulation happened, and initialized the highest/lowest score tracking only on the first valid attempted score. |

## Code Review Completed

| Reviewed Member | Repository Link | What Was Done Well | Issue Identified | Suggested Improvement |
|------------------|------------------|---------------------|--------------------|--------------------------|
| Manoj Kumar | https://github.com/manojmanu916/preptrack-Manoj-Kumar| The program was easy to follow, with proper input validation and a well-formatted final report. The placement status logic was implemented correctly.| The score validation message was not specific enough about the valid input values. | Replace the message with: "Invalid score. Please enter -1 or a value from 0 to 100." |

## Feedback Received

| Field | Details |
|-------|---------|
| Reviewed By | Manoj Kumar |
| Feedback Received | The validation message should clearly mention the valid score range so users know what values are accepted. |
| Was the Feedback Valid? | Yes |
| Change Made | Modified the validation message to: "Invalid score. Please enter -1 or a value from 0 to 100." |
| Commit Message Used | Refine score validation message based on peer review feedback |


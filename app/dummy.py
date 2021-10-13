ctc = 5
ctc = round(ctc * 100000 / 12) - 2050
months = {
    "$EMP_CTC": ctc,
    "$LETTER_DATE": "01-01-2021",
    "$EMP_NAME": "soham parekh",
    "$EMP_ADDRESS": "line1\nline2\nline3",
    "$JOINING_DATE": "01-01-2021",
    "$EMP_DESIGNATION": "engineer",
    "$MONTH-BASIC": round(ctc * 0.4),
    "$MONTH-CITY": round(ctc * 0.18),
    "$MONTH-SPECIAL": round(ctc * 0.22),
    "$MONTH-CONVEY": 800,
    "$MONTH-MEDIC": 1250,
}
months["$MONTH-HRA"] = round(months["$MONTH-BASIC"] / 2)
months["$MONTH-SUM"] = months["$MONTH-BASIC"]
+months["$MONTH-HRA"]
+months["$MONTH-CITY"]
+months["$MONTH-SPECIAL"]
+months["$MONTH-CONVEY"]
+months["$MONTH-MEDIC"]
years = {
    "$YEAR-BASIC": months["$MONTH-BASIC"] * 12,
    "$YEAR-HRA": months["$MONTH-HRA"] * 12,
    "$YEAR-CITY": months["$MONTH-CITY"] * 12,
    "$YEAR-SPECIAL": months["$MONTH-SPECIAL"] * 12,
    "$YEAR-CONVEY": months["$MONTH-CONVEY"] * 12,
    "$YEAR-MEDIC": months["$MONTH-MEDIC"] * 12,
    "$YEAR-SUM": months["$MONTH-SUM"] * 12,
}
variables = {**months, **years}
print(variables)

import sqlite3
from queries import (
    create_hike,
    drop_hike,
    insert_hike,
    select_hike,
    create_offer,
    drop_offer,
    insert_offer,
    select_offer,
    create_relieve,
    drop_relieve,
    insert_relieve,
    select_relieve,
    create_resign,
    drop_resign,
    insert_resign,
    select_resign,
    create_experience,
    drop_experience,
    insert_experience,
    select_experience,
    create_payslip,
    drop_payslip,
    insert_payslip,
    select_payslip,
    create_jrhr,
    drop_jrhr,
    insert_jrhr,
    select_jrhr,
    create_srhr,
    drop_srhr,
    insert_srhr,
    select_srhr,
)

# For testing in RAM
# con = sqlite3.connect(":memory:")

# CAUTION: FOR MAIN DB
con = sqlite3.connect("db/hr.db")

print("DB connected")
input(
    "CAUTION: This will drop any existing tables and start fresh. Please take backup if you need to. Continue?"
)

with con:
    c = con.cursor()

    c.execute(drop_payslip)
    c.execute(create_payslip)
    # c.execute(insert_payslip)
    # c.execute(insert_payslip)

    for row in c.execute(select_payslip):
        print(row)

    c.execute(drop_experience)
    c.execute(create_experience)
    # c.execute(insert_experience)

    for row in c.execute(select_experience):
        print(row)

    c.execute(drop_resign)
    c.execute(create_resign)
    c.execute(insert_resign)

    for row in c.execute(select_resign):
        print(row)

    c.execute(drop_relieve)
    c.execute(create_relieve)
    # c.execute(insert_relieve)

    for row in c.execute(select_relieve):
        print(row)

    c.execute(drop_offer)
    c.execute(create_offer)
    # c.execute(insert_offer)

    for row in c.execute(select_offer):
        print(row)

    c.execute(drop_hike)
    c.execute(create_hike)
    # c.execute(insert_hike)

    for row in c.execute(select_hike):
        print(row)

    c.execute(drop_srhr)
    c.execute(create_srhr)
    c.execute(insert_srhr)

    for row in c.execute(select_srhr):
        print(row)

    c.execute(drop_jrhr)
    c.execute(create_jrhr)
    c.execute(insert_jrhr)
    c.execute(insert_jrhr)
    c.execute(insert_jrhr)
    c.execute(insert_jrhr)
    # c.execute(insert_jrhr2)

    for row in c.execute(select_jrhr):
        print(row)

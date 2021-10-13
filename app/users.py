from fastapi import Request, APIRouter
from databases import Database
from collections import defaultdict

user_router = APIRouter()
database = Database("sqlite:///db/hr.db")


@user_router.get("/test")
async def fetch_data():
    query = "SELECT * FROM SRHR"
    results = await database.fetch_all(query=query)
    return results


@user_router.on_event("startup")
async def database_connect():
    try:
        await database.connect()
    except Exception as e:
        print(e)
    print("DB connected")


@user_router.post(
    "/register",
)
async def register_exec(payload: Request):
    data = await payload.json()
    username, emailid, passwd, type = (
        data["username"],
        data["emailid"],
        data["passwd"],
        data["type"],
    )
    print(username, passwd, type)
    try:
        if type == "admin":
            exist_query = f'SELECT * FROM SRHR WHERE name="{username}"'
            exists = await database.fetch_one(exist_query)
            if exists != None:
                print("Username exists")
                return {"msg": "Username Exists"}
            query = (
                f'INSERT INTO SRHR VALUES(null, "{username}","{passwd}","{emailid}");'
            )
            await database.execute(query)
        elif type == "junior":
            exist_query = f'SELECT * FROM JRHR WHERE name="{username}"'
            exists = await database.fetch_one(exist_query)
            if exists != None:
                return {"msg": "Username Exists"}
            query = (
                f'INSERT INTO JRHR VALUES(null, "{username}","{passwd}","{emailid}");'
            )
            await database.execute(query)
    except Exception as e:
        print("Register failed", e)
        return {"msg": "Failed"}
    return {"msg": "Success"}


@user_router.post("/login")
async def root(payload: Request):
    data = await payload.json()
    username, type = data["username"], data["type"]
    if type == "admin":
        q1 = f'SELECT * FROM SRHR WHERE name="{username}";'
        user = await database.fetch_one(q1)
        if user == None:
            print("Wrong creds")
            return {}
        user_data = {"name": user[1], "passwd": user[2], "emailid": user[3]}
        print(user_data)
        return user_data

    else:
        q1 = f'SELECT * FROM JRHR WHERE name="{username}";'
        user = await database.fetch_one(q1)
        if user == None:
            print("Wrong creds")
            return {}
        user_data = {"name": user[1], "passwd": user[2], "emailid": user[3]}
        print(user_data)
        return user_data


# called when jr hr submits form
@user_router.post("/submit-form")
async def submit_form(payload: Request):
    data_raw = await payload.json()
    print(data_raw)
    type = data_raw["type"]
    data = defaultdict(lambda: "-", data_raw["data"])
    if type == "offer":
        insert_query = """INSERT INTO OFFER VALUES(
        {},
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        {})""".format(
            data["hr_id"],
            data["letter_date"],
            data["emp_address"],
            data["emp_name"],
            data["emp_designation"],
            data["joining_date"],
            data["emp_ctc"],
        )
    elif type == "hike":
        insert_query = """INSERT INTO HIKE VALUES(
        {},
        '{}',
        '{}',
        '{}',
        '{}',
        {},
        '{}')""".format(
            data["hr_id"],
            data["letter_date"],
            data["emp_id"],
            data["emp_name"],
            data["emp_designation"],
            data["emp_ctc"],
            data["effective_date"],
        )
    elif type == "experience":
        insert_query = """INSERT INTO EXPERIENCE VALUES(
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}')""".format(
            data["hr_id"],
            data["curr_date"],
            data["emp_name"],
            data["emp_id"],
            data["emp_designation"],
            data["emp_dept"],
            data["join_date"],
            data["leave_date"],
        )
    elif type == "relieving":
        insert_query = """INSERT INTO RELIEVE VALUES(
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}')""".format(
            data["hr_id"],
            data["curr_date"],
            data["emp_name"],
            data["emp_id"],
            data["letter_date"],
            data["resig_date"],
        )
    elif type == "register":
        insert_query = """INSERT INTO EMPLOYEE VALUES(
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}')""".format(
            data["hr_id"],
            data["emp_id"],
            data["emp_name"],
            data["emp_designation"],
            data["emp_dept"],
            data["emp_gender"],
            data["emp_pan"],
            data["emp_dob"],
            data["emp_father"],
            data["emp_qualification"],
            data["emp_perm_address"],
            data["emp_curr_address"],
            data["emp_email"],
            data["emp_phone"],
            data["emp_whatsapp"],
            data["emp_referrer"],
            data["emp_institute"],
            data["offer_date"],
            data["offer_desig"],
            data["offer_ctc"],
            data["resig_date"],
            data["company_name"],
            data["tech"],
            data["new_company"],
            data["bank_acc"],
            data["join_date"],
            data["curr_desig"],
            data["curr_ctc"],
            data["rel_date"],
            data["location"],
            data["pf_acc"],
            data["bank_name"],
        )
    elif type == "payslip":
        insert_query = """INSERT INTO PAYSLIP VALUES(
        {},
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}',
        '{}')""".format(
            data["hr_id"],
            data["letter_month"],
            data["letter_year"],
            data["emp_name"],
            data["emp_id"],
            data["emp_band"],
            data["emp_dept"],
            data["emp_designation"],
            data["emp_dob"],
            data["emp_pan"],
            data["emp_doj"],
            data["location"],
            data["nwd"],
            data["dw"],
            data["lop"],
            data["esi"],
            data["pf"],
            data["emp_ctc"],
        )
    await database.execute(insert_query)
    print(insert_query)
    print("Inserted to db")
    return {"msg": "Success"}


@user_router.post("/fetch-employee")
async def submit_form(payload: Request):
    try:
        data_raw = await payload.json()
        print(data_raw)
        result = {}
        emp_id = data_raw["emp_id"]
    except:
        emp_id = "EQDPP"
    select_query = f"SELECT * FROM EMPLOYEE WHERE emp_id='{emp_id}'"
    pragma_query = "PRAGMA table_info(EMPLOYEE)"
    result = []
    data = await database.fetch_all(select_query)
    if data != -1:
        res = await database.fetch_all(pragma_query)
        headers = [row[1] for row in res]
        for row in data:
            d = {}
            for index, value in enumerate(row):
                d[headers[index]] = value
            d["type"] = "EMPLOYEE"
            result.append(d)
    print(result)
    return result


@user_router.get("/check-form")
async def check_form():
    result = []
    tables = ["HIKE", "EXPERIENCE", "OFFER", "RELIEVE", "PAYSLIP", "EMPLOYEE"]
    for table in tables:
        select_query = "SELECT * FROM "
        pragma_query = "PRAGMA table_info("
        select_query += table
        pragma_query += table + ")"
        data = await database.fetch_all(select_query)
        if data != -1:
            res = await database.fetch_all(pragma_query)
            headers = [row[1] for row in res]
            for row in data:
                d = {}
                for index, value in enumerate(row):
                    d[headers[index]] = value
                d["type"] = table
                result.append(d)
    print(result)
    return result


@user_router.get("/home")
def send_home():
    return {"msg": "Up"}

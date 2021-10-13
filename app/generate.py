import os
from fastapi import Request, APIRouter, BackgroundTasks
from .doc import DocumentGenerator
from .utils import generate_string, cleanup
from fastapi.responses import FileResponse

generate_router = APIRouter()


@generate_router.post(
    "/generate-letter",
    responses={
        200: {
            "content": {"application/pdf": {}},
            "description": "Return the pdf.",
        }
    },
)
async def generate(payload: Request, background_tasks: BackgroundTasks):
    try:
        # called normally
        data = await payload.json()
        type = data["type"]
        details = data["data"]
    except:
        # this means it was run from /docs for testing
        details = {}
        type = "payslip"

    print(f"Generating {type} letter......")
    doc_name = "templates/" + generate_string() + ".docx"
    pdf_name = doc_name.replace(".docx", ".pdf")

    if type == "relieving":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_rel_letter(doc_name, details)
    elif type == "offer":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_offer_letter(doc_name, details)
    elif type == "resignation":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_resignation_letter(doc_name, details)
    elif type == "hike":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_hike_letter(doc_name, details)
    elif type == "experience":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_exp_letter(doc_name, details)
    elif type == "payslip":
        letter = DocumentGenerator("templates/experience_letter.docx")
        letter.generate_payslip_letter(doc_name, details)

    letter.generate_pdf(doc_name, pdf_name)
    background_tasks.add_task(cleanup, [doc_name, pdf_name])
    print("Sending response")
    return FileResponse(pdf_name, media_type="application/pdf")


@generate_router.post("/ctc")
async def submit_form(payload: Request):
    data = await payload.json()
    ctc = float(data["ctc"])
    ctc = round(ctc * 100000 / 12) - 2050
    months = {
        "EMP_CTC": ctc,
        "M_BASIC": round(ctc * 0.4),
        "M_CITY": round(ctc * 0.18),
        "M_SPECIAL": round(ctc * 0.22),
        "M_CONVEY": 800,
        "M_MEDIC": 1250,
    }
    months["M_HRA"] = round(months["M_BASIC"] / 2)
    months["M_SUM"] = (
        months["M_BASIC"]
        + months["M_HRA"]
        + months["M_CITY"]
        + months["M_SPECIAL"]
        + months["M_CONVEY"]
        + months["M_MEDIC"]
    )
    years = {
        "Y_BASIC": months["M_BASIC"] * 12,
        "Y_HRA": months["M_HRA"] * 12,
        "Y_CITY": months["M_CITY"] * 12,
        "Y_SPECIAL": months["M_SPECIAL"] * 12,
        "Y_CONVEY": months["M_CONVEY"] * 12,
        "Y_MEDIC": months["M_MEDIC"] * 12,
        "Y_SUM": months["M_SUM"] * 12,
    }
    variables = {**months, **years}
    return variables

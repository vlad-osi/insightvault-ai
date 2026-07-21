from pathlib import Path

from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.document_service import create_document
from app.schemas.document import DocumentResponse

from app.services.document_service import (
    create_document,
    get_documents
)

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post(
    "/upload",
    response_model=DocumentResponse
)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    document = create_document(
        db=db,
        filename=file.filename,
        content_type=file.content_type,
        size=file_path.stat().st_size
    )

    return document

@router.get(
    "",
    response_model=list[DocumentResponse]
)
def list_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)
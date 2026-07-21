from sqlalchemy.orm import Session

from app.models.document import Document


def create_document(
    db: Session,
    filename: str,
    content_type: str,
    size: int
):
    document = Document(
        filename=filename,
        content_type=content_type,
        size=size,
        status="uploaded"
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return document

def get_documents(db: Session):
    return db.query(Document).all()
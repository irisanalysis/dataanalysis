from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.models import Document
from app.schemas.schemas import Document as DocumentSchema, DocumentCreate

router = APIRouter()

@router.get("/", response_model=List[DocumentSchema])
def read_documents(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    documents = db.query(Document).filter(Document.is_active == True).offset(skip).limit(limit).all()
    return documents

@router.post("/", response_model=DocumentSchema)
def create_document(document: DocumentCreate, db: Session = Depends(get_db)):
    db_document = Document(**document.dict())
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

@router.get("/{document_id}", response_model=DocumentSchema)
def read_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id, Document.is_active == True).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.put("/{document_id}", response_model=DocumentSchema)
def update_document(document_id: int, document: DocumentCreate, db: Session = Depends(get_db)):
    db_document = db.query(Document).filter(Document.id == document_id, Document.is_active == True).first()
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    
    for key, value in document.dict().items():
        setattr(db_document, key, value)
    
    db.commit()
    db.refresh(db_document)
    return db_document

@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    db_document = db.query(Document).filter(Document.id == document_id, Document.is_active == True).first()
    if db_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    
    db_document.is_active = False
    db.commit()
    return {"message": "Document deleted successfully"}
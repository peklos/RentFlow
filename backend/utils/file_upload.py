import os
import uuid
from typing import List
from fastapi import UploadFile
import shutil


UPLOAD_DIR = "uploads"
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
ALLOWED_DOCUMENT_EXTENSIONS = {".pdf", ".doc", ".docx"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


async def save_upload_file(upload_file: UploadFile, upload_dir: str = UPLOAD_DIR) -> str:
    """
    Save uploaded file and return the file path
    """
    # Create upload directory if it doesn't exist
    os.makedirs(upload_dir, exist_ok=True)

    # Generate unique filename
    file_extension = os.path.splitext(upload_file.filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join(upload_dir, unique_filename)

    # Save file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return file_path


async def save_property_photos(photos: List[UploadFile]) -> List[str]:
    """
    Save multiple property photos and return list of file paths
    """
    photo_paths = []

    for photo in photos:
        # Validate file extension
        file_extension = os.path.splitext(photo.filename)[1].lower()
        if file_extension not in ALLOWED_IMAGE_EXTENSIONS:
            continue

        # Save photo
        photo_path = await save_upload_file(photo, os.path.join(UPLOAD_DIR, "properties"))
        photo_paths.append(photo_path)

    return photo_paths


async def save_document(document: UploadFile, document_type: str = "general") -> str:
    """
    Save document file (passport, contract, etc.)
    """
    file_extension = os.path.splitext(document.filename)[1].lower()

    if file_extension not in ALLOWED_DOCUMENT_EXTENSIONS:
        raise ValueError(f"File type {file_extension} not allowed")

    upload_dir = os.path.join(UPLOAD_DIR, "documents", document_type)
    return await save_upload_file(document, upload_dir)


def delete_file(file_path: str) -> bool:
    """
    Delete a file
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")
        return False

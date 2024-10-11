from fastapi import APIRouter, HTTPException, status

from data_store import receipts_storage, points_storage
from api.helpers.receipt_points import retrieve_receipt, get_my_points

router = APIRouter()


@router.get("/api/v1/receipts/{id}/points")
def get_receipt_points(id: str):
    my_receipt = retrieve_receipt(id, receipts_storage)

    if not my_receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No receipt found for that id",
        )

    if not points_storage.get(id):
        points = get_my_points(my_receipt)
        points_storage[id] = points

    return {"points": points_storage[id]}

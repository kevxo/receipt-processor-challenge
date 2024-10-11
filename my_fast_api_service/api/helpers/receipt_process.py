import uuid
from pydanctic_models.receipt_process import ReceiptProcessCreate, ReceiptProcess


def new_receipt_process(
    receipt_process_req: ReceiptProcessCreate, receipt_process: ReceiptProcess
) -> ReceiptProcess:
    receipt_process.id = str(uuid.uuid4())
    receipt_process.retailer = receipt_process_req.retailer
    receipt_process.purchaseDate = receipt_process_req.purchaseDate
    receipt_process.purchaseTime = receipt_process_req.purchaseTime
    receipt_process.items = receipt_process_req.items
    receipt_process.total = receipt_process_req.total

    return receipt_process

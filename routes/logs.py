from fastapi import Body, APIRouter, Query, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from typing import List
from models.logs import Logs, LogsData
from beanie.operators import  And, RegEx

router = APIRouter()

@router.post("/ingest")
async def ingest_logs(logs: List[Logs] = Body(...)):
    try:
        _ = await Logs.insert_many(logs)
        return JSONResponse(content={'message': 'success'}, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        return JSONResponse(content={'message': str(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/query")
async def fetch_logs(start: int = Query(...), end: int = Query(...), text: str =  Query(...)):
    try:
        log_data = await Logs.find_many(
            And(Logs.time >= start, Logs.time <= end, RegEx(Logs.log, text)),
            projection_model=LogsData
        ).to_list()
        if log_data:
            return jsonable_encoder(log_data)
        else:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JSONResponse(content={'message': repr(e)}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
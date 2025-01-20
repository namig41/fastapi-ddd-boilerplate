from fastapi import APIRouter

from presentation.api.healthcheck.schemas import HealthcheckResponseSchema



router = APIRouter(prefix='/healthcheck', tags=['Healthcheck'],)


@router.get(
    '',
    description='Application status',
    response_model=HealthcheckResponseSchema,
)
async def get_healthcheck_status() -> HealthcheckResponseSchema:
    return HealthcheckResponseSchema()
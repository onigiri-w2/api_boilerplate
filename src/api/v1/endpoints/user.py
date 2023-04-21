from typing import List

from fastapi import APIRouter, Response, status

from src.api.utils.exception.converter import convert_exception
from src.api.utils.exception.exception import Http400Exception, Http404Exception
from src.api.utils.exception.schema import ErrorResponse
from src.api.utils.logging.route_class import LoggingRoute
from src.api.v1.schema.request import CreateUserRequest, UpdateUserRequest
from src.api.v1.schema.response import UserResponse
from src.model.impl.entity.user.repository import UserMySQLRepository
from src.model.impl.entity.user.user import User
from src.rdb.query.user import UserQuery
from src.utils.exception.exception import NotFoundError, ValidationError

router = APIRouter()
router.route_class = LoggingRoute


@router.get(
    "/all",
    description="get all users",
    status_code=status.HTTP_200_OK,
    response_model=List[UserResponse],
    responses={404: {"model": ErrorResponse}},
)
async def all_user() -> List[UserResponse]:
    query_rslt = UserQuery.all()
    return [UserResponse(**rslt) for rslt in query_rslt]


@router.get(
    "",
    description="get one user",
    status_code=status.HTTP_200_OK,
    response_model=UserResponse,
    responses={404: {"model": ErrorResponse}, 422: {"model": ErrorResponse}},
)
@convert_exception(Http404Exception, (NotFoundError,))
async def one_user(name: str = "") -> UserResponse:
    user = UserQuery.one_by_name(name)
    return UserResponse(**user)


@router.post(
    "",
    description="create user",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    responses={400: {"model": ErrorResponse}, 422: {"model": ErrorResponse}},
)
@convert_exception(Http400Exception, (ValidationError,))
async def create_user(user_request: CreateUserRequest) -> UserResponse:
    repo = UserMySQLRepository(autocommit=True)
    user = User.new(user_request.name, user_request.age, user_request.phone_number)
    repo.save(user)
    return UserResponse(
        id=user.id.id, name=user.name.name, age=user.age.age, phone_number=user.phone_number.phone_number
    )


@router.post(
    "/update",
    description="update user",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={400: {"model": ErrorResponse}, 422: {"model": ErrorResponse}},
)
@convert_exception(Http404Exception, (NotFoundError,))
async def update_user(user_request: UpdateUserRequest) -> Response:
    repo = UserMySQLRepository(autocommit=True)
    user = repo.find(user_request.id)
    user = user.updated(user_request.name, user_request.age, user_request.phone_number)
    repo.save(user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

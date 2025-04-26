import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
MOVIES_STORAGE_FILEPATH = BASE_DIR / "movies.json"


LOG_LEVEL = logging.INFO
LOG_FORMAT = str(
    "[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s"
)

API_TOKENS: frozenset[str] = frozenset(
    {
        "Z3jm9IygwL1SZ590xr1RbA",
        "Nyy22FDbkKqkFVgjUOKxaA",
        "3xOccQrmIBHA-lXAl4AC7A",
    }
)


USERS_DB: dict[str, str] = {
    "bob": "123",
    "admin": "admin",
}

from core.log import LogFactory
from core.properties import properties as prop
import requests as req

logger = LogFactory.getLogger(__name__)

new_user_host = f"{prop['PLANNER_API']}/v1/usuarios/registrar/telegram"


def new_user(user: dict) -> bool:
    logger.debug(f"novo usuário = {user}")

    res = req.post(
        new_user_host,
        json=user,
        headers={'Content-Type': 'application/json'}
    )

    if res.status_code == 201:
        logger.info(f"Novo usuário criado com sucesso: {res.json()}")
        return True
    else:
        logger.error(f"Usuario {user['usuarioTelegram']} não pode ser criado: {res.status_code}")
        logger.error(f"{res.json()}")
        return False

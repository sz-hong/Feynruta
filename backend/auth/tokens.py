import secrets

token_to_user: dict[str, str] = {} #[token: username]
user_to_token: dict[str, str] = {} #[username: token]

async def get_user(token):
    return token_to_user.get(token)

async def revoke(username):
    token = user_to_token[username]
    del token_to_user[token]
    del user_to_token[username]

async def issue_token(username):
    token = secrets.token_urlsafe(32)
    if username in user_to_token:
        del token_to_user[user_to_token[username]]
    user_to_token[username] = token
    token_to_user[token] = username
    return token
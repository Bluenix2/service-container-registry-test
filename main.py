import httpx

res = httpx.get('litecord/api/v9/users/@me', headers={'Authorization': 'Bot ADMIN_TOKEN'})
print(res.json())

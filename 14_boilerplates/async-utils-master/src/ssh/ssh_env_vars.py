import asyncio, asyncssh, sys


async def run_client():
    async with asyncssh.connect('localhost') as conn:
        result = await conn.run('env', env={'LANG': 'en_GB', 'LC_COLLATE': 'C'})
        print(result.stdout, end='')


try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))

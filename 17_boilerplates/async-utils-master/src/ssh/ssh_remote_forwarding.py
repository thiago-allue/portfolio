import sys
import asyncio

import asyncssh


async def run_client():
    async with asyncssh.connect('localhost') as conn:
        listener = await conn.forward_remote_port('', 8080, 'localhost', 80)
        await listener.wait_closed()


try:
    asyncio.get_event_loop().run_until_complete(run_client())
except (OSError, asyncssh.Error) as exc:
    sys.exit('SSH connection failed: ' + str(exc))

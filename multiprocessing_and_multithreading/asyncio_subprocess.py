import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await proc.communicate()

    print(f"{cmd} existed with status code: {proc.returncode}")

    if stdout:
        print(f"STDOUT:\n{stdout.decode('utf-8')}")

    if stderr:
        print(f"STDERR:\n{stderr.decode('utf-8')}")


async def main(commands_param):
    tasks = []
    for cmd in commands_param:
        tasks.append(run(cmd))

    await asyncio.gather(*tasks)


commands = ("ifconfig", "ls", "who", "uname -a")
asyncio.run(main(commands))

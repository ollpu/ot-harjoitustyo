from invoke import task

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/ui/main.py")

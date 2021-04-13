from invoke import task

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/main.py")

@task
def coverage(ctx):
    ctx.run("coverage run -m pytest src", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

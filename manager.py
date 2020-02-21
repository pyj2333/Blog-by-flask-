# 负责启动应用
from factor import  init_db, creat_app
import click  #定义flask命令

app = creat_app()

@click.command(name = "init_db")
def init_db_command():
    init_db(app)
    click.echo("init database successfully")

@click.command(name = "runserver")
def run():
    app.run(debug= True)

app.cli.add_command(init_db_command)
app.cli.add_command(run)


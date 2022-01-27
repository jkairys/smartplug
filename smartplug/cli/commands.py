import click
from smartplug.controllers.list_devices import list_all_plugs
from smartplug.controllers.sync import run_sync, run_forever
from smartplug.controllers.meross_manager import login, MerossManager, MerossHttpClient
from smartplug.controllers.monitor import monitor
import confuse
from loguru import logger
from dataclasses import dataclass
import os


@dataclass()
class CliContext:
    config: confuse.Configuration
    manager: MerossManager
    http_api_client: MerossHttpClient


@click.group()
@click.option('--config-file', default=None, help='Path to config.yaml')
@click.pass_context
def cli(ctx, config_file):
    config = confuse.Configuration('smartplug', __name__)
    if config_file is not None:
        logger.info(f'Looking for config file in {config_file}')
        config.set_file(config_file)
    manager, http_api_client = run_sync(login, email=os.environ.get('MEROSS_EMAIL') or config['email'].get(str), password=os.environ.get('MEROSS_PASSWORD') or config['password'].get(str))
    ctx.obj = CliContext(config=config, manager=manager, http_api_client=http_api_client)


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.pass_context
def list_devices(ctx, count):
    cli_context: CliContext = ctx.obj
    plugs = run_sync(list_all_plugs, manager=cli_context.manager, http_api_client=cli_context.http_api_client)
    run_forever(monitor, plugs=plugs)


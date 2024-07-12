
import click

from icx_tool.keystore import ks
from icx_tool.prep import prep


URL_MAP = {
	"local": "http://127.0.0.1:9000/api/v3/icon_dex",
	"mainnet": "https://ctz.solidwallet.io/api/v3/icon_dex",
	"berlin": "https://berlin.net.solidwallet.io/api/v3",
	"lisbon": "https://lisbon.net.solidwallet.io/api/v3",
}

@click.group()
@click.option('--url', type=click.STRING, default='mainnet', envvar='ICON_ENDPOINT_URL',
			  help='JSON-RPC URL. Predefined: "local", "mainnet", "berlin", "lisbon"')
@click.pass_context
def cli(ctx: click.Context, url: str = "mainnet"):
	ctx.ensure_object(dict)
	ctx.obj['URL'] = NET_MAP.get(url, url)


cli.add_command(ks)
cli.add_command(prep)


if __name__ == '__main__':
	cli()

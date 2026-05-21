import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from datetime import datetime

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from bot.logger import setup_logger
from bot.client import client

setup_logger()

console = Console()

app = typer.Typer(
    help="PrimeTrade Binance Futures Trading Bot"
)

@app.command()
def health():

    console.print(
        Panel.fit(
            "[bold green]SYSTEM HEALTH CHECK[/bold green]",
            border_style="green"
        )
    )

    try:

        server_time = client.get_server_time()

        table = Table(
            title="System Status",
            box=box.ROUNDED
        )

        table.add_column(
            "Service",
            style="cyan"
        )

        table.add_column(
            "Status",
            style="green"
        )

        table.add_row(
            "Binance API",
            "ONLINE"
        )

        table.add_row(
            "Server Time",
            str(server_time["serverTime"])
        )

        table.add_row(
            "Environment",
            "TESTNET"
        )

        table.add_row(
            "Checked At",
            str(datetime.now())
        )

        console.print(table)

    except Exception as e:

        console.print(
            f"[bold red]Health Check Failed:[/bold red] {e}"
        )

@app.command()
def trade(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    try:

        side = validate_side(side)

        order_type = validate_order_type(
            order_type
        )

        quantity = validate_quantity(
            quantity
        )

        if (
            order_type == "LIMIT"
            and price is None
        ):
            raise ValueError(
                "LIMIT order requires price."
            )

        console.print(
            Panel.fit(
                "[bold cyan]PRIMETRADE FUTURES BOT[/bold cyan]",
                border_style="cyan"
            )
        )

        summary = Table(
            title="Order Summary",
            box=box.ROUNDED
        )

        summary.add_column(
            "Field",
            style="cyan"
        )

        summary.add_column(
            "Value",
            style="green"
        )

        summary.add_row(
            "Symbol",
            symbol.upper()
        )

        summary.add_row(
            "Side",
            side
        )

        summary.add_row(
            "Order Type",
            order_type
        )

        summary.add_row(
            "Quantity",
            str(quantity)
        )

        summary.add_row(
            "Execution Time",
            str(datetime.now())
        )

        if price:
            summary.add_row(
                "Price",
                str(price)
            )

        console.print(summary)

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        result = Table(
            title="Execution Result",
            box=box.DOUBLE
        )

        result.add_column(
            "Key",
            style="magenta"
        )

        result.add_column(
            "Value",
            style="yellow"
        )

        result.add_row(
            "Order ID",
            str(response.get("orderId"))
        )

        result.add_row(
            "Status",
            str(response.get("status"))
        )

        result.add_row(
            "Executed Qty",
            str(response.get("executedQty"))
        )

        result.add_row(
            "Client Order ID",
            str(response.get("clientOrderId"))
        )

        console.print(result)

        console.print(
            "\n[bold green]ORDER EXECUTED SUCCESSFULLY[/bold green]"
        )

    except Exception as e:

        console.print(
            f"\n[bold red]ERROR:[/bold red] {str(e)}"
        )

if __name__ == "__main__":
    app()

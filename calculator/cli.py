import click as clk

from calculator.model import Calculator

@clk.group()
@clk.pass_context

def calc(ctx: clk.Context):
    """"A simple calculator"""

    ctx.obj = {"calculator object", Calculator()}

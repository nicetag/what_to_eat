#! /usr/bin/env python
# -*- coding=utf-8 -*-

import __init__
import random
import click
import StoreData

store_list = StoreData.store_list

@click.command()
@click.option('--dec', prompt='to eat(1) or eaten(2)', help='Choise the logical module')
def choice_module(dec):
    dec = int(dec)
    if dec == 1:
        i = random.randint(0, len(StoreData.store_list))
        click.echo(StoreData.store_list[i])

    if dec == 2:
        slist = input_store_name()
        print(slist)

@click.command()
@click.option('--store_name', prompt='what is store name?', help='enter store name')
def input_store_name(store_name):
    a = StoreData.store_init()
    a.name(store_name)
    StoreData.add(a.name)

if __name__ == '__main__':
    choice_module()
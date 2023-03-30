import os
import sys
import json
import click
import prompt
from models.model_fetcher import ModelFetcher

BASE_PROMPTER_PATH = os.path.expanduser('~/.pa/')
BASE_PROMPT_PATH = os.path.join(BASE_PROMPTER_PATH, 'prompts')
BASE_HISTORY_PATH = os.path.join(BASE_PROMPTER_PATH, 'history')


@click.group()
def prompter():
    """LLM is a command utility that allows building on top of llms"""
    pass


@click.command()
@click.argument('action', required=True)
@click.argument('input_text', nargs=-1, required=False)
@click.option('-j', '--json', 'json_input', is_flag=True, help='Specify input as a JSON string.')
@click.option('-v', '--verbose', count=True, help='Specify input as a JSON string.')
@click.option('-m', '--model', 'model_identifier', help='Identifier for the model')
def run(action, input_text, json_input, verbose, model_identifier):
    if not input_text:
        input_text = sys.stdin.read().strip().split()
    else:
        input_text = ' '.join(input_text)

    prompt_variables = json.loads(input_text) if json_input else {'prompter.content': input_text}
    prompt_variables['prompter.verbosity'] = verbose

    parsed_prompt = prompt.run(BASE_PROMPT_PATH, action, prompt_variables)
    fetcher = ModelFetcher()
    model = fetcher.fetch_model(model_identifier)

    click.echo(model.call(parsed_prompt))


@click.command()
def list_prompts():
    click.echo("\n".join(prompt.list_prompts(BASE_PROMPT_PATH)))


prompter.add_command(run)
prompter.add_command(list_prompts)

if __name__ == '__main__':
    prompter()


import os
import sys
import json
from typing import List
import click
import prompt
from models.model_fetcher import ModelFetcher

BASE_PROMPTER_PATH = os.path.expanduser('~/.pa/')
BASE_PROMPT_PATH = os.path.join(BASE_PROMPTER_PATH, 'bin')
BASE_HISTORY_PATH = os.path.join(BASE_PROMPTER_PATH, 'history')


@click.group()
def promp_actions():
    """PromptActions is a command utility that allows building on top of llms"""
    pass

@promp_actions.command('run')
@click.argument('action', required=True)
@click.argument('input_text', nargs=-1, required=False)
@click.option('-p', '--pipe', 'pipe_input', is_flag=True, help='Reads input from stdin.')
@click.option('-j', '--json', 'json_input', is_flag=True, help='Specify input as a JSON string.')
@click.option('-v', '--verbose', count=True, help='Specify input as a JSON string.')
@click.option('-m', '--model', 'model_identifier', help='Identifier for the model')
def run(action: str, input_text: List[str], pipe_input: bool, json_input: bool, verbose: int, model_identifier: str) -> None:
    """Runs the command-line interface.

    Args:
        action: The action to perform.
        input_text: The input text to run the action on.
        json_input: Whether the input is a JSON string.
        verbose: The verbosity level.
        model_identifier: The model identifier.

    """
    if pipe_input:
        input_text = sys.stdin.read().strip().split()
    else:
        input_text = ' '.join(input_text)

    prompt_variables = json.loads(input_text) if json_input else {'prompter.content': input_text}
    prompt_variables['prompter.verbosity'] = verbose

    parsed_prompt = prompt.generate(BASE_PROMPT_PATH, action, prompt_variables)

    fetcher = ModelFetcher()

    model = fetcher.fetch_model(model_identifier)

    result = model.call(parsed_prompt)
    
    prompt.save_history(BASE_HISTORY_PATH, action, parsed_prompt, result)
    
    click.echo(result)


@click.command()
def ls():
    click.echo("\n".join(prompt.list_prompts(BASE_PROMPT_PATH)))


promp_actions.add_command(run)
promp_actions.add_command(ls)

if __name__ == '__main__':
    promp_actions()


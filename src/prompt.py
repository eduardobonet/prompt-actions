import os
from jinja2 import Environment, FileSystemLoader


def list_prompts(path):
    """List all available prompts in the BASE_AI_PATH."""

    prompts = []
    for root, dirs, files in os.walk(path):
        relative_root = os.path.relpath(root, path)
        for file in files:
            prompt_path = file if relative_root == '.' else os.path.join(relative_root, file)
            prompts.append(prompt_path)
    return prompts


def run(base_path, prompt_name, prompt_variables):
    template_path = os.path.join(base_path, prompt_name)
    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Prompt was not found (looking for {template_path})")

    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    print(prompt_variables)
    return template.render(**prompt_variables)




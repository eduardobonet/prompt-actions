# AI - A Prompt manager for LLMs

AI a is a command-line utility that provides an easy interface for LLM (Language Model API) services, coupled to a 
git backed prompt management functionality. It aims to make prompts shareable and reusable, while serving as a backend
for applications that want to use LLMs.

## Core Design Goals

1. `ai` is a utility to manage and consume prompts: it shouldn't have functionality that is already covered by other tools (eg fetching urls except the API calls to LLMs)
2. Prompts are code artifacts: As such, prompts need to be versioned and code reviewed
3. Bring your own LLM API: `ai` should work with whatever LLM the user wants to use

## Getting Started

To get started with AI, you'll need to install the utility on your system. AI is distributed as a Bash script, so you can simply download the latest release and run it from the command line. You can also clone the AI repository from GitHub and build it from source if you prefer.

```bash
pip install prompt-manager
```

To create the folders:

```bash
ai init
```

To list backends:

```
ai list-backends
```

To setup a backend:

```bash
ai setup-model some-model
```

Once you have AI installed, you can start using it right away. Simply run the ai command from the terminal to launch the utility.

## Prompts

In `ai`, a prompt is a text file that can be templated using [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/), making
prompts very flexible. Here's a prompt example:

```
//~/.ai/prompt/arr
Say the following phrase: {{some_phrase}}. Then, write the following as a pirate:
```

You can then call the prompt by setting the value to some_phrase 

### Creating a prompt

To create a prompt, simply add a text file to `~/.ai/prompts`. You can use Jinja2 to define variables. The name of the file
will be the name of the ai command. For example:

```bash
> tree ~/.prompter/prompts
~/.prompter/prompts
├── arr
└── helpers
    └── capitalize
    
> ai list
ai arr
ai helper/capitalize
```


### Calling prompts

#### Passing arguments to the command line 

```bash
ai arr --some_phrase "Hello Pirate" "Hi friend, how was your weekend?"
```

#### Passing arguments as json

```bash
cat /path/to/my/json | ai arr --json 
```

#### Piping

When piping, the input will be appended to the end of the prompt. It doesn't support additional options.

```bash
curl 'https://my_page' | ai arr
```

#### Interactive (_Not Implemented Yet_)

```bash
ai arr -i
> some_phrase
Hello Pirate
> Prompt input
Hi friend, how was your weekend?
```

#### Chat (_Not Implemented Yet_)

```bash
ai chat

/arr some_phrase="Hello Pirate" Hi friend, how was your weekend?
```

#### Other options

- `--help` show help about the command

### Prompt Versioning

If a prompt is in a git repo, you can use the option `--git` and pass the hash or a tag to a specific version of the prompt.

```bash
ai arr --hash='SOME_HASH'
```

```bash
ai arr --tag='SOME_TAG'
```

## History

`ai` stores the history of calls to LLMs, attaching the prompt alongside it. You can find the logs at `.ai/history/`, where
each command has it's own folder and each file is a call to the api.

## For the future

- [ ] Chat (`ai chat`)
- [ ] Pass a module with a new custom backend `ai arr --backed=my_module`
- [ ] Multiple prompt paths 
- [ ] Load a prompt from an URI `ai cmd --prompt=http://my_prompt`
- [ ] Lifecycle callbacks (before populating a prompt, after populating a prompt)
- [ ] Default prompt options
- [ ] Add metadata to prompts 
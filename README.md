# tap-mode

`tap-mode` is a Singer tap for [Mode API](https://mode.com/developer/api-reference/).

This package is NOT officially supported by Mode. Users are welcome to open issues or pull requests to improve the tap.

Extracts the following resources from [Mode API](https://mode.com/developer/api-reference/):
- [Collections/Spaces](https://mode.com/developer/api-reference/management/collections/)
- [Reports](https://mode.com/developer/api-reference/analytics/reports/)

Built with the Meltano [SDK](https://gitlab.com/meltano/sdk) for Singer Taps.

## Installation

```bash
pipx install  git+https://github.com/franloza/mode-tap.git
```

## Configuration

### Accepted Config Options

The following configuration options are available:

- auth_token (required): The public component of the credential. See how to obtain it from Mode [here](https://mode.com/developer/api-reference/authentication/)
- password (required): The private component of the credential. See how to obtain it from Mode [here](https://mode.com/developer/api-reference/authentication/)
- workspace (required): Name of the Mode workspace
- user_agent (optional): It should be set to something that includes the name of your app, and a contact email address should the API provider need to contact you for any reason.
- start_date (optional): Fetch only entities created/updated after that date.

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-mode --about
```

## Usage

You can easily run `tap-mode` by itself or in a pipeline using [Meltano](www.meltano.com).

### Executing the Tap Directly

```bash
tap-mode --version
tap-mode --help
tap-mode --config CONFIG --discover > ./catalog.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `mode/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-mode` CLI interface directly using `poetry run`:

```bash
poetry run tap-mode --help
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

<div align="center">
    <h1>Taxi demand predictor service</h1>
    <i>Author: Jose Caloca </i>
</div>

<br />
<div align="center">
    <sub>Let's connect 🤗</sub>
    <br />
    <a href="https://www.linkedin.com/in/josecaloca/">LinkedIn</a> 
    <br />
</div>

## Quick setup

1. Install [Python Poetry](https://python-poetry.org/)
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. cd into the project folder and run
    ```
    $ poetry install
    ```

3. Activate the virtual env that you just created with
    ```
    $ poetry shell
    ```

4. Open free accounts at Hopsworks and CometML and copy your project names and API keys in an .env file
    ```
    $ cp .env.sample .env
    # paste your 2 values there
    ```

5. Backfill the feature group with historical data
    ```
    $ make backfill
    ```

6. Run the training pipeline
    ```
    $ make training
    ```

7. Run the feature pipeline for the last hour
    ```
    $ make features
    ```

8. Run the inference pipeline to generate predictions for the last hour
    ```
    $ make inference
    ```

## Wanna see it in action?

- [Live Dashboard with model predictions](https://taxi-demand-nyc.streamlit.app/)
- [Live Dashboard with model monitoring ](https://taxi-demand-model-monitoring.streamlit.app/)

## Extra set up for Mac M1/M2 chips

```bash
$ brew update
$ brew install libomp librdkafka
```

Add the following lines to your `~/.bashrc` or `~/.zshrc` file:

```bash
export C_INCLUDE_PATH=/opt/homebrew/Cellar/librdkafka/2.2.0/include
export LIBRARY_PATH=/opt/homebrew/Cellar/librdkafka/2.2.0/libexport PYENV_ROOT="$HOME/.pyenv"
```

# Dev/Container Overhaul

- First Test Deploy QA.
  - Can we trim down the app.rb file???
- Make sure "Next Steps" in project's README make sense.
  - How should we do `SECRET_KEY_BASE` now with Crypteia?
- Update Lamby Site & Guides

## Dotenv Rake Task

```
echo "== Environments & Configuration =="
# ./bin/rails \
#   -rlamby \
#   lamby:ssm:dotenv \
#   LAMBY_SSM_PARAMS_PATH="/{% include "_cctmp/file_name.txt" %}/${RAILS_ENV}/env"
```

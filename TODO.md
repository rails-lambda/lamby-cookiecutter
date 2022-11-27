# Dev/Container Overhaul

- First Test Deploy QA.
  - Can we try Function URLs vs `HttpApiProxy`.
  - Best practice for creating a /app directory or something like /var/task in Ruby image?
  - Can we trim down the app.rb file???
  - Is lamby:ssm:dotenv still good and how about Dotenv? Use Crypteia.
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

# Dev/Container Overhaul

- How can I mimic project folder name in dev container?
- What should I do in bin/setup if not ./bin/yarn
- Test SAM init with Docker again. Can be done with branch?
- Make sure "Next Steps" in project's README make sense.
- Go vanilla, especially for bin scripts. Delete run, server, bootstrap, etc.
- Is lamby:ssm:dotenv still good and how about Dotenv? Use Crypteia.
- Can we trim down the app.rb file???
- Add Devcontainer stuff to both READMEs.
- Best practice for creating a /app directory or something like /var/task in Ruby image?
- Can we try Function URLs vs `HttpApiProxy`.
- Should we set `SAM_CLI_TELEMETRY=0` again?
- Do we use dev containers in the deploy and test?
- How should we do `SECRET_KEY_BASE` now with Crypteia?

## ECR Repo Creation!

So SAM does this automatically now create the ECR repo? Or should I put this back in someplace?

```shell
aws ecr create-repository \
  --repository-name {% include "_cctmp/dash_name.txt" %} \
  --image-tag-mutability MUTABLE \
  --image-scanning-configuration scanOnPush=true \
  --region "$AWS_DEFAULT_REGION" || true
```

## Dotenv Rake Task

```
echo "== Environments & Configuration =="
# ./bin/rails \
#   -rlamby \
#   lamby:ssm:dotenv \
#   LAMBY_SSM_PARAMS_PATH="/{% include "_cctmp/file_name.txt" %}/${RAILS_ENV}/env"
```

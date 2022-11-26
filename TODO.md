# Dev/Container Overhaul

- First Test Deploy QA.
  - Can we try Function URLs vs `HttpApiProxy`.
  - Best practice for creating a /app directory or something like /var/task in Ruby image?
  - Can we trim down the app.rb file???
  - Is lamby:ssm:dotenv still good and how about Dotenv? Use Crypteia.
- What should I do in bin/setup if not ./bin/yarn
- Make sure "Next Steps" in project's README make sense.
  - How should we do `SECRET_KEY_BASE` now with Crypteia?
- Update Lamby Site & Guides
 
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

# Lamby Cookiecutter

<a href="https://lamby.custominktech.com"><img src="https://user-images.githubusercontent.com/2381/59363668-89edeb80-8d03-11e9-9985-2ce14361b7e3.png" alt="Lamby: Simple Rails & AWS Lambda Integration using Rack." align="right" width="300" /></a>

An [AWS SAM cookiecutter](https://technology.customink.com/blog/2020/03/13/using-aws-sam-cookiecutter-project-templates-to-kickstart-your-ambda-projects/) project template to quickly create a new Rails application for AWS Lambda. Details:

- Rails v6.x on Ruby 2.7 runtime.
- Integrated JavaScript development.
- Compiles CSS/JS assets with LibSass & Webpacker.
- No ActiveRecord. Read our [Database Options](https://lamby.custominktech.com/docs/database_options) guides.

**[Lamby: Simple Rails & AWS Lambda Integration using Rack.](https://lamby.custominktech.com)**

## Usage

⚠️ Please reference the full [Quick Start](https://lamby.custominktech.com/docs/quick_start) guide on the Lamby site for details. Basic usage is:

### SAM Init

If you have the [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) already installed, use the first command. If not, use the second Docker based command.

```shell
$ sam init --location "gh:customink/lamby-cookiecutter"
```

```shell
$ docker run \
  --rm \
  --interactive \
  --volume "${PWD}:/var/task" \
  public.ecr.aws/sam/build-ruby2.7 \
  sam init --location "gh:customink/lamby-cookiecutter"
```

### Setup & Deploy (within project)

```shell
$ ./bin/bootstrap
$ ./bin/setup
$ ./bin/deploy
```

## Contributing

This starter project is 100% scripted within Docker using the scripts in the `bin` directory. To build run the following commands.

```shell
./bin/bootstrap
./bin/build
```

## Code of Conduct

Everyone interacting in the Lamby project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/customink/lamby/blob/master/CODE_OF_CONDUCT.md).

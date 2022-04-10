# Lamby Cookiecutter

<a href="https://lamby.custominktech.com"><img src="https://raw.githubusercontent.com/customink/lamby/master/images/social2.png" alt="Lamby: Simple Rails & AWS Lambda Integration using Rack." align="right" width="450" style="margin-left:1rem;margin-bottom:1rem;" /></a>

An [AWS SAM cookiecutter](https://technology.customink.com/blog/2020/03/13/using-aws-sam-cookiecutter-project-templates-to-kickstart-your-ambda-projects/) project template to quickly create a new Rails application for AWS Lambda. Details:

- Rails v7.x on Ruby 3.1 runtime.
- Integrated JavaScript & CSS Development.

**[Lamby: Simple Rails & AWS Lambda Integration using Rack.](https://lamby.custominktech.com)**

## Usage

⚠️ Please reference the full [Quick Start](https://lamby.custominktech.com/docs/quick_start) guide on the Lamby site for details. Basic usage is:

### SAM Init

If you have the [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) already installed, use the following command.

```shell
$ sam init --location "gh:customink/lamby-cookiecutter"
```

You can avoid installing the SAM CLI locally by using this Docker command.

```shell
$ docker run \
  --rm \
  --interactive \
  --volume "${PWD}:/var/task" \
  ghcr.io/customink/lamby-cookiecutter \
  "gh:customink/lamby-cookiecutter"
```

### Setup & Deploy (within project)

```shell
$ ./bin/setup
$ ./bin/deploy
```

## Contributing

This starter project is 100% scripted within Docker using the scripts in the `bin` directory. To build run the following commands.

```shell
./bin/build
```

## Code of Conduct

Everyone interacting in the Lamby project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/customink/lamby/blob/master/CODE_OF_CONDUCT.md).

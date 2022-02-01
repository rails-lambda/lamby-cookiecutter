# {% include "_cctmp/class_name.txt" %}

<a href="https://lamby.custominktech.com"><img src="https://user-images.githubusercontent.com/2381/59363668-89edeb80-8d03-11e9-9985-2ce14361b7e3.png" alt="Lamby: Simple Rails & AWS Lambda Integration using Rack." align="right" width="300" /></a>

Made with [Lamby's](https://lamby.custominktech.com/docs/quick_start) quick start to create a new Rails application for AWS Lambda. Details:

- Rails v6.x on Ruby 2.7 runtime.
- Integrated JavaScript development.
- Compiles CSS/JS assets.
- No ActiveRecord. Read our [Database Options](https://lamby.custominktech.com/docs/database_connections) guides.

**[Lamby: Simple Rails & AWS Lambda Integration using Rack.](https://lamby.custominktech.com)**

## Setup & Deploy

```shell
$ ./bin/bootstrap
$ ./bin/setup
$ ./bin/deploy
```

## Next Steps

- Provide a new value for the `SECRET_KEY_BASE`. Alternatively, you can set this using Dotenv & SSM Parameter Store in the [Environments & Configuration](https://lamby.custominktech.com/docs/environment_and_configuration) section of your build file.
- Using JavaScript? everything is setup and ready to go.

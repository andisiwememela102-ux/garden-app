# Garden App Docker Practical

This submission containerizes the Garden App Python console project. It asks for a month and hemisphere, then prints seasonal gardening advice.

## Build and run

```console
docker build -t andisiwememela102/garden-advice:latest .
docker run -it --rm andisiwememela102/garden-advice:latest
```

The `-it` flags attach a terminal so you can answer the app's prompts.

## Docker Hub

The public image is published at:

https://hub.docker.com/r/andisiwememela102/garden-advice

Pull and run it with:

```console
docker pull andisiwememela102/garden-advice:latest
docker run -it --rm andisiwememela102/garden-advice:latest
```

The `latest` tag was pushed successfully from Killercoda on 2026-11-12. The Docker Hub Tags page shows the published `linux/amd64` image.

## Verify from another machine

Play with Docker (PWD), named in the course PDF, has been retired. Killercoda provides a browser-based Ubuntu playground at https://killercoda.com/playgrounds/scenario/ubuntu. In a fresh Docker-enabled machine or playground, run the `docker pull` and `docker run` commands above. The image is interactive: enter a month (for example `11`) and hemisphere (`south`) when prompted.

## Files

- `Dockerfile`: builds from the official Python 3.11 slim image and starts the console app.
- `.dockerignore`: excludes local cache and Git metadata from the build context.
- `garden_advice.py`: application source required by the image.
- `test_garden_advice.py`: existing project tests, included as source material but not required at runtime.
- `docker1.txt`: required Docker Hub repository link.

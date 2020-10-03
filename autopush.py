import docker
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
versions = ["3.6", "3.7"]
latest_version = "3.7"
repo = "mosajjal/pypy"

if __name__ == "__main__":
    client = docker.from_env()

    for item in versions:
        print(f"pypy {item} will be built")
        print("building the new image")

        img = client.images.build(path=current_dir+f"/{item}")
        print(f"pypy f{item} image built successfully, tagging the image")
        img[0].tag(f"{repo}:{item}")

        print("pushing the repository to docker hub")
        client.images.push(repository=repo, tag=f"{item}")

    latest_image = client.images.get(f"{repo}:{latest_version}")
    latest_image.tag(f"{repo}:latest")
    client.images.push(repository=repo, tag="latest")

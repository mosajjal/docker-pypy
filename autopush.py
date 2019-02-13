import docker
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
versions = ["2.7", "3.5", "3.6"]

if __name__ == "__main__":
    client = docker.from_env()

    for item in versions:
        print(f"pypy {item} will be built")
        print("building the new image")
        
        img = client.images.build(path=current_dir+f"/{item}")
        print("pypy f{item} image built successfully, tagging the image")
        img[0].tag(f"mosajjal/pypy:{item}")

        print("pushing the repository to docker hub")
        client.images.push(repository="mosajjal/pypy", tag=f"{item}")

FROM tatsushid/tinycore:11.0-x86_64

ARG PYTHON_PIP_VERSION=20.2.3
ARG RELEASE=100507-ecc38af111bd
ARG VERSION=3.6

# Install dependencies
RUN tce-load -wic openssl-1.1.1 expat2 libffi bzip2-lib ncursesw

# Download release binary and uncompress it in /usr/local/
RUN sudo wget http://buildbot.pypy.org/nightly/py${VERSION}/pypy-c-jit-${RELEASE}-linux64.tar.bz2 -O pypy.tar.bz2
RUN sudo tar -xjC /usr/local --strip-components=1 -f pypy.tar.bz2

# Remove temp
RUN sudo rm -rf /tmp/tce/optional/* pypy.tar.bz2

# Necessery symlinks to get it to run
RUN sudo ln -s /usr/local/lib/libbz2.so /usr/local/lib/libbz2.so.1
RUN sudo ln -s /lib /lib64


# Install Pip
RUN set -ex; \
	\
	sudo wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py'; \
	\
	sudo pypy3 get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		"pip==$PYTHON_PIP_VERSION" \
	; \
	pip --version; \
	\
    sudo rm -f get-pip.py

ENTRYPOINT [ "pypy3" ]

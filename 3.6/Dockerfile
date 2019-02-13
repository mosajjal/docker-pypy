FROM tatsushid/tinycore:10.0-x86_64

ENV PYTHON_PIP_VERSION 19.0.2

# Download latest 3.6 Version binary and unzip it in /usr/local/
RUN sudo wget http://buildbot.pypy.org/nightly/py3.6/pypy-c-jit-latest-linux64.tar.bz2 -O pypy.tar.bz2
RUN sudo tar -xjC /usr/local --strip-components=1 -f pypy.tar.bz2

# Install dependencies
RUN tce-load -wic openssl expat2 libffi bzip2-lib ncurses

# Remove temp
RUN sudo rm -rf /tmp/tce/optional/* pypy.tar.bz2

# Necessery symlinks to get it to run
RUN sudo ln -s /usr/local/lib/libtinfo.so.6.0 /usr/local/bin/libtinfo.so.5
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

FROM mcr.microsoft.com/devcontainers/anaconda:0-3

ADD .devcontainer/.zshrc /home/vscode/.
ADD .devcontainer/git-prompt.sh /home/vscode/.
ADD .devcontainer/.oh-my-zsh/custom/themes/sully.zsh-theme /home/vscode/.oh-my-zsh/custom/themes/.

ENV SHELL /bin/zsh

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

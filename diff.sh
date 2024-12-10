for f in $(git diff --name-only main test-dev ./clean); do git diff main test-dev ${f} | kompare -o - ; done

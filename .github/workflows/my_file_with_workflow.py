name: Shell commands
on: [push]
jobs:
  run-shell-command:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, ubuntu-20.04]
    steps:
      - name: echo a string
        run: echo "Hello world"
      - name: multiline script
        run: |
          python3 -V
          touch my_file_with_workflow.py
          ls -l

# dataflow-python-setup-pipelines

Suggest example pipelines with --setup_file options.

* [single-file-pipeline](single-file-pipeline): All pipeline code in single
  file. The setup.py and `--setup_file` option are unnecessary.
* [utils-file-pipeline](utils-file-pipeline): A pipeline having a pipeline file
  and an util file separately. Use [`py_modules`](utils-file-pipeline/setup.py)
  in setup.py to recognize the file module in Dataflow jobs.
* [utils-dir-pipeline](utils-dir-pipeline): A pipeline having a pipeline file
  and an util package directory. Use [`packages`](utils-dir-pipeline/setup.py)
  in setup.py to recognize the directory module in Dataflow jobs.

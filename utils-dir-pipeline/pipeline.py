import logging

from apache_beam import Create
from apache_beam import DoFn
from apache_beam import ParDo
from apache_beam import Pipeline
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

from utils_dir.mymath import mysqrt


class PrintSqrtDoFn(DoFn):
  def process(self, element):
    logging.info('x:%s, sqrt(x):%s', element, mysqrt(element))


def main():
  options = PipelineOptions()
  options.view_as(SetupOptions).save_main_session = True

  p = Pipeline(options=options)

  (p
   | Create([0, 1, 2])
   | 'PrintSqrt' >> ParDo(PrintSqrtDoFn()))

  p.run()


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  main()

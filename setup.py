#!/usr/bin/env python

from distutils.core import setup

setup(name='notifier',
      version='0.0',
      description='Notify build status via leds',
      author='Michael Daffin',
      author_email='michael.daffin@swtchconcepts.com',
      data_files=['/usr/lib/systemd/system', ['notifier.service']],
      scripts=['notifier'],
     )

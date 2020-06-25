from setuptools import setup

package_name = 'sound_system'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'sound_speak1',
    ],
    install_requires=['setuptools'],
    data_files=[
        ('lib/' + package_name, ['package.xml']),
        ('lib/' + package_name+'/module',
         ['module/module_pico.py',
          ]),
        ('lib/sound_system/beep/',
         ['beep/speech.wav',
          'beep/start.wav',
          'beep/stop.wav'
          ]),
        ('lib/sound_system/log',
            ['log/log.txt'])
    ],
    zip_safe=True,
    author='HiroseChihiro',
    author_email='rr0111fx@ed.ritsumei.ac.jp',
    maintainer='HiroseChihiro',
    maintainer_email='rr0111fx@ed.ritsumei.ac.jp',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='sound package for final',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sound_speak1 = sound_speak1:main',
        ],
    },
)

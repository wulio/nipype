# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..extractskeleton import ExtractSkeleton


def test_ExtractSkeleton_inputs():
    input_map = dict(InputImageFileName=dict(argstr='%s',
    position=-2,
    ),
    OutputImageFileName=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    args=dict(argstr='%s',
    ),
    dontPrune=dict(argstr='--dontPrune ',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    numPoints=dict(argstr='--numPoints %d',
    ),
    pointsFile=dict(argstr='--pointsFile %s',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    type=dict(argstr='--type %s',
    ),
    )
    inputs = ExtractSkeleton.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ExtractSkeleton_outputs():
    output_map = dict(OutputImageFileName=dict(position=-1,
    ),
    )
    outputs = ExtractSkeleton.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

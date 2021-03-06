# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..minc import Reshape


def test_Reshape_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    clobber=dict(argstr='-clobber',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    input_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    output_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    name_source=['input_file'],
    name_template='%s_reshape.mnc',
    position=-1,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    verbose=dict(argstr='-verbose',
    ),
    write_short=dict(argstr='-short',
    ),
    )
    inputs = Reshape.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Reshape_outputs():
    output_map = dict(output_file=dict(),
    )
    outputs = Reshape.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

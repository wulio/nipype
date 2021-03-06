# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Axialize


def test_Axialize_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    axial=dict(argstr='-axial',
    xor=['coronal', 'sagittal'],
    ),
    coronal=dict(argstr='-coronal',
    xor=['sagittal', 'axial'],
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    copyfile=False,
    mandatory=True,
    position=-2,
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    orientation=dict(argstr='-orient %s',
    ),
    out_file=dict(argstr='-prefix %s',
    name_source='in_file',
    name_template='%s_axialize',
    ),
    outputtype=dict(),
    sagittal=dict(argstr='-sagittal',
    xor=['coronal', 'axial'],
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    verb=dict(argstr='-verb',
    ),
    )
    inputs = Axialize.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Axialize_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Axialize.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

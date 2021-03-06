# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..base import WatershedBEM


def test_WatershedBEM_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    atlas_mode=dict(argstr='--atlas',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(deprecated='1.0.0',
    nohash=True,
    usedefault=True,
    ),
    overwrite=dict(argstr='--overwrite',
    usedefault=True,
    ),
    subject_id=dict(argstr='--subject %s',
    mandatory=True,
    ),
    subjects_dir=dict(mandatory=True,
    usedefault=True,
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    volume=dict(argstr='--volume %s',
    usedefault=True,
    ),
    )
    inputs = WatershedBEM.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_WatershedBEM_outputs():
    output_map = dict(brain_surface=dict(loc='bem/watershed',
    ),
    cor_files=dict(altkey='COR',
    loc='bem/watershed/ws',
    ),
    fif_file=dict(altkey='fif',
    loc='bem',
    ),
    inner_skull_surface=dict(loc='bem/watershed',
    ),
    mesh_files=dict(),
    outer_skin_surface=dict(loc='bem/watershed',
    ),
    outer_skull_surface=dict(loc='bem/watershed',
    ),
    )
    outputs = WatershedBEM.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

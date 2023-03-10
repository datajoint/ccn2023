from . import dj_config, pipeline


def test_generate_pipeline(pipeline):
    subject = pipeline["subject"]
    imaging = pipeline["imaging"]
    scan = pipeline["scan"]
    session = pipeline["session"]
    Equipment = pipeline["Equipment"]

    subject_tbl, *_ = session.Session.parents(as_objects=True)

    # test elements connection from lab, subject to Session
    assert subject_tbl.full_table_name == subject.Subject.full_table_name

    # test elements connection from Session to scan, imaging
    session_tbl, equipment_tbl, _ = scan.Scan.parents(as_objects=True)
    assert session_tbl.full_table_name == session.Session.full_table_name
    assert equipment_tbl.full_table_name == Equipment.full_table_name
    assert "mask_npix" in imaging.Segmentation.Mask.heading.secondary_attributes
    assert "activity_trace" in imaging.Activity.Trace.heading.secondary_attributes

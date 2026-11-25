import pytest
import av.anc_filter as mod

CASES = [
    ("anc_sample_clock_unify", (1,)),
    ("anc_step_size_adapt", (1,)),
    ("secondary_path_identify", (1,)),
    ("binaural_joint_constraint", (1,)),
    ("anc_state_hold", (1,)),
    ("mode_switch_fade", (1,)),
    ("load_anc_session", (1,)),
    ("capture_reference", (1,)),
    ("update_filter", (1,)),
    ("present_anc", (1,)),
    ("validate_anc", (1,)),
    ("metrics_anc", (1,)),
    ("audit_anc", (1,)),
    ("fallback_anc", (1,)),
    ("determinism_anc", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

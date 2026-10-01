# REV005 F04-X02 — DESTINATION PARITY ROOT CAUSE

## Outcome

F04-X02 correctly stopped at:

`BLOCKED_F04_X02_DESTINATION_PARITY`

Canonical Blend/GLB remained unchanged.

## Direct visual finding

X02 A/B renders use the correct historical cameras and a correct 59-object destination selection, but they do not reproduce archived V05 A/B because the historical V05 renderer did not simply show all 59 selected objects.

The historical V05 renderer applies an additional shell-occluder visibility rule.

Historical function:
`render_rev005_interior_remediation_v05.py::show_only(objs)`

Rule:

Any object whose name contains one of:
- `_LEFT`
- `_RIGHT`
- `_BACK`
- `_SOFFIT`
- `_CEILING_BEAM`

is hidden from the QA render even if that object belongs to the selected facility object set.

## F04-specific impact

The accepted 59-object F04 destination contains:

- `RM_WELFARE_SHOWER_BACK_0`
- `RM_WELFARE_SHOWER_BACK_1`
- `RM_WELFARE_SHOWER_BACK_2`
- `RM_WELFARE_SHOWER_BACK_3`

These four objects match the historical shell-occluder token `_BACK`.

X02 incorrectly forced all 59 selected F04 objects visible, so these four large gray shower-back panels were rendered.

Direct visual comparison confirms these panels are the dominant structural difference between:
- X02 A/B
and
- archived V05 A/B.

The archived V05 images omit those four back-wall objects by design.

## Conclusion

This is an evidence-generation semantics mismatch, not an F04 model-geometry defect.

Do NOT modify the canonical F04 model.

Do NOT delete or hide these four objects in the saved canonical scene.

For X03, reproduce the original V05 `show_only()` behavior exactly as temporary QA visibility only.

## Locked canonical state

Blend:
`DA65C2F0F32E2108A2805AEFC94199A7733F4A813953403F8B8F0FD6B2CB888D`

GLB:
`812E252E57CDEE17AC09AD270F543C04D7CD53816D0C0E4D2FAC46D6B331EC5C`

These must remain unchanged.

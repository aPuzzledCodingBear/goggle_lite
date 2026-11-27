#!/usr/bin/env python3
"""Generate the electrical draft and full-scale control-center trial sheet."""

import json
from pathlib import Path
from uuid import NAMESPACE_URL, uuid5


ROOT = Path(__file__).resolve().parents[1]
MODEL = json.loads((ROOT / "interface.json").read_text(encoding="utf-8"))
LIBRARY = "GoggleControls"
SWITCH_PINS = ["CONTACT_1", "CONTACT_2", "CONTACT_1", "CONTACT_2"]


def q(value):
    return json.dumps(value, ensure_ascii=False)


def uid(*items):
    key = "/".join(str(item) for item in items)
    return str(uuid5(NAMESPACE_URL, f"goggle-lite/control-panel/P2/{key}"))


def xy(x, y):
    return f"{x:.4f} {y:.4f}"


def prop(name, value, x, y, *, hidden=False):
    hide = " (hide yes)" if hidden else ""
    return f'(property {q(name)} {q(value)} (at {xy(x, y)} 0) (effects (font (size 1.27 1.27)){hide}))'


class Symbol:
    def __init__(self, name, rows, *, reference="J", odd_even=False):
        self.name = name
        self.reference = reference
        self.height = (len(rows) - 1) * 1.27 + 2.54
        self.pins = []
        for index, row in enumerate(rows):
            y = (len(rows) - 1) * 1.27 - index * 2.54
            if odd_even:
                self.pins.append((2 * index + 1, row[0], False, y))
                self.pins.append((2 * index + 2, row[1], True, y))
            else:
                self.pins.append((index + 1, row, False, y))

    def definition(self, prefix=""):
        props = "\n".join([
            prop("Reference", self.reference, 0, self.height + 5.08),
            prop("Value", self.name, 0, self.height + 2.54),
            prop("Footprint", "", 0, 0, hidden=True),
            prop("Datasheet", "", 0, 0, hidden=True),
        ])
        pins = []
        for number, name, right, y in self.pins:
            x, angle = (21.59, 180) if right else (-21.59, 0)
            pins.append(f'''(pin passive line (at {xy(x, y)} {angle}) (length 5.08)
              (name {q(name)} (effects (font (size 1.016 1.016))))
              (number {q(str(number))} (effects (font (size 1.016 1.016)))))''')
        return f'''(symbol {q(prefix + self.name)} (pin_names (offset 1.016))
          (exclude_from_sim no) (in_bom yes) (on_board yes)
          {props}
          (symbol {q(self.name + '_0_1')}
            (rectangle (start {-16.51} {self.height}) (end {16.51} {-self.height})
              (stroke (width 0.254) (type default)) (fill (type background))))
          (symbol {q(self.name + '_1_1')} {''.join(pins)}))'''


def pin_map(connector):
    if "pins" in connector:
        return dict(enumerate(connector["pins"], 1))
    return {int(number): net for number, net in connector["physical_pin_nets"].items()}


def place(project, root_id, symbol, reference, device, x, y):
    wires, pin_ids = [], []
    nets = pin_map(device)
    for pin, _, right, pin_y in symbol.pins:
        at_y = y - pin_y
        edge_x = x + (21.59 if right else -21.59)
        net = nets.get(pin)
        if net is None:
            wires.append(f'(no_connect (at {xy(edge_x, at_y)}) (uuid {uid(project, reference, pin, "nc")}))')
        else:
            tail_x = edge_x + (12.7 if right else -12.7)
            justify = "right" if right else "left"
            wires.extend([
                f'''(wire (pts (xy {xy(edge_x, at_y)}) (xy {xy(tail_x, at_y)}))
                  (stroke (width 0) (type default)) (uuid {uid(project, reference, pin, "wire")}))''',
                f'''(label {q(net)} (at {xy(tail_x, at_y)} 0)
                  (effects (font (size 1.27 1.27)) (justify {justify} bottom))
                  (uuid {uid(project, reference, pin, "label")}))''',
            ])
        pin_ids.append(f'(pin {q(str(pin))} (uuid {uid(project, reference, pin, "pin")}))')
    # Component footprint assignments await mechanical source data.
    return f'''(symbol (lib_id {q(LIBRARY + ':' + symbol.name)}) (at {xy(x, y)} 0) (unit 1)
      (exclude_from_sim no) (in_bom yes) (on_board yes) (dnp no) (uuid {uid(project, reference)})
      {prop('Reference', reference, x, y - symbol.height - 5.08)}
      {prop('Value', device['part'], x, y - symbol.height - 2.54)}
      {prop('Footprint', '', x, y, hidden=True)}
      {prop('Datasheet', '', x, y, hidden=True)}
      {''.join(pin_ids)}
      (instances (project {q(project)} (path {q('/' + root_id)} (reference {q(reference)}) (unit 1)))))\n'''+"\n".join(wires)


def note(project, number, value, x, y):
    return f'''(text {q(value)} (at {xy(x, y)} 0)
      (effects (font (size 1.27 1.27)) (justify left)) (uuid {uid(project, 'note', number)}))'''


def schematic(project, components, notes):
    root_id = uid(project)
    unique_symbols = {symbol.name: symbol for symbol, _, _, _, _ in components}
    embedded = "\n".join(symbol.definition(LIBRARY + ":") for symbol in unique_symbols.values())
    placed = "\n".join(place(project, root_id, *component) for component in components)
    annotations = "\n".join(note(project, index, *item) for index, item in enumerate(notes))
    return f'''(kicad_sch (version 20250114) (generator eeschema)
      (uuid {root_id}) (paper "A4")
      (title_block (title {q('Goggle Lite - ' + project)}) (rev "DRAFT P2")
        (comment 1 "Electrical draft. No manufacturing footprint approval."))
      (lib_symbols {embedded})
      {placed}
      {annotations}
      (sheet_instances (path "/" (page "1"))))\n'''


def trial_template():
    layout = MODEL["panel_layout_mm"]
    width, height = layout["outline_trial"]
    elements = []
    for key, name, radius in [("x_center", "X", 9), ("y_center", "Y", 9), ("back_center", "BACK", 5)]:
        x, y = layout[key]
        x, y = x + 15, y + 25
        elements.append(f'''<circle cx="{x}" cy="{y}" r="{radius}" stroke-dasharray="1 1" />
  <path d="M {x-3} {y} h 6 M {x} {y-3} v 6" />
  <text x="{x}" y="{y+15}" text-anchor="middle">{name}</text>''')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="137mm" height="130mm" viewBox="0 0 137 130">
<title>Goggle Lite control panel position trial</title>
<style>text {{ fill:#111; stroke:none; font:3px sans-serif; }}</style>
<g stroke="#111" stroke-width="0.22" fill="none">
  <text x="15" y="10">Goggle Lite - front view - position trial only</text>
  <text x="15" y="15">Print 100%. Verify both 100 mm rulers. Do not drill from this sheet.</text>
  <rect x="15" y="25" width="{width}" height="{height}" stroke-dasharray="2 1" />
  {''.join(elements)}
  <path d="M 15 91 v -4 m 0 2 h 100 m 0 2 v -4" />
  <text x="65" y="96" text-anchor="middle">100 mm horizontal calibration</text>
  <path d="M 120 20 h 4 m -2 0 v 100 m -2 0 h 4" />
  <text x="127" y="74" transform="rotate(-90 127 74)" text-anchor="middle">100 mm vertical calibration</text>
  <text x="15" y="105">Dashed circles are placeholders for knobs and cap, not hole sizes.</text>
  <text x="15" y="111">Dashed outline is a trial face, not the PCB or enclosure outline.</text>
</g>
</svg>\n'''


def project_file(name):
    return json.dumps({"meta": {"filename": f"{name}.kicad_pro", "version": 1}}, indent=2) + "\n"


def main():
    panel = MODEL["control_panel"]
    pi = MODEL["pi_adapter"]
    pa = Symbol("PA_8", panel["J1"]["pins"])
    encoder = Symbol("EBF410448V1R0", ["B", "C", "A", "SW", "GND", "VCC"])
    button = Symbol("Tactile_NO_4Pin", SWITCH_PINS, reference="SW")
    pi_gpio = Symbol("Pi_GPIO_2x20", [
        ("3V3", "5V"), ("BCM2", "5V"), ("BCM3", "GND"), ("BCM4", "BCM14"),
        ("GND", "BCM15"), ("BCM17", "BCM18"), ("BCM27", "GND"), ("BCM22", "BCM23"),
        ("3V3", "BCM24"), ("BCM10", "GND"), ("BCM9", "BCM25"), ("BCM11", "BCM8"),
        ("GND", "BCM7"), ("BCM0", "BCM1"), ("BCM5", "GND"), ("BCM6", "BCM12"),
        ("BCM13", "GND"), ("BCM19", "BCM16"), ("BCM26", "BCM20"), ("GND", "BCM21"),
    ], odd_even=True)
    files = {
        "panel.kicad_sch": schematic("panel", [
            (pa, "J1", panel["J1"], 76.2, 63.5),
            (encoder, "J2", panel["J2"], 165.1, 50.8),
            (encoder, "J3", panel["J3"], 165.1, 88.9),
            (button, "SW1", panel["SW1"], 165.1, 127),
        ], [
            ("J2/J3 numbering: knob-side view, side-exit pins down; left to right 1 to 6.", 38.1, 151.13),
            ("SW1: terminals 1/3 are one contact; 2/4 are the other. Verify physical pin assignment.", 38.1, 156.21),
            ("Use 3.3 V only. Confirm mounting, pin pitch and reach before laying out.", 38.1, 161.29),
        ]),
        "pi-adapter.kicad_sch": schematic("pi-adapter", [
            (pa, "J1", pi["J1"], 76.2, 63.5),
            (pi_gpio, "J2", pi["J2"], 165.1, 76.2),
        ], [
            ("J2 numbers are Pi physical pin numbers. 5 V pins have no electrical connection.", 38.1, 123.19),
            ("J1 interfaces are numbered identically at both ends; cable straight-through by circuit number.", 38.1, 128.27),
            ("Install and verify with power disconnected. Mechanical pre-alignment fixture pending.", 38.1, 133.35),
        ]),
        "GoggleControls.kicad_sym": '(kicad_symbol_lib (version 20231120) (generator kicad_symbol_editor)\n'
                                  + '\n'.join(symbol.definition() for symbol in [pa, encoder, button, pi_gpio]) + ')\n',
        "sym-lib-table": '(sym_lib_table\n  (version 7)\n'
                         '  (lib (name "GoggleControls")(type "KiCad")(uri "${KIPRJMOD}/GoggleControls.kicad_sym")(options "")(descr "Goggle Lite control draft"))\n)\n',
        "panel.kicad_pro": project_file("panel"),
        "pi-adapter.kicad_pro": project_file("pi-adapter"),
        "panel-position-trial.svg": trial_template(),
    }
    for name, content in files.items():
        (ROOT / name).write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
